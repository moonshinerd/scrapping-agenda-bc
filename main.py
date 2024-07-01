from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from datetime import datetime, timedelta
import csv

# Obtenha o caminho completo do chromedriver
path_chromedriver = os.path.join(os.getcwd(), "chromedriver")

# Configure o serviço do chromedriver
service = Service(path_chromedriver)

# Configure as opções do Chrome
options = Options()

driver = webdriver.Chrome(service=service, options=options)

# Abra a URL desejada
driver.get("https://www.bcb.gov.br/acessoinformacao/agendaautoridades")

# Função para selecionar uma data
def select_date(driver, day, month, year):
    # Encontre todos os elementos <select> pela classe
    select_elements = driver.find_elements(By.CSS_SELECTOR, "select.form-control.mr-sm-2.mb-2.mb-sm-0")

    # Selecione o dia
    select_day = Select(select_elements[0])
    select_day.select_by_value(str(day))

    # Selecione o mês
    select_month = Select(select_elements[1])
    select_month.select_by_value(month)

    # Encontre o elemento <select> para o ano
    select_year_element = driver.find_element(By.CSS_SELECTOR, "select.form-control:not(.mr-sm-2):not(.mb-2):not(.mb-sm-0)")
    select_year = Select(select_year_element)
    select_year.select_by_value(str(year))

    # Aguarde um pouco para que a seleção tenha efeito
    time.sleep(2)

# Função para extrair as informações do presidente Roberto Campos Neto
def extract_info(driver):
    try:
        # Aguarde até que o elemento desejado esteja presente na página
        wait = WebDriverWait(driver, 10)
        roberto_info = wait.until(EC.presence_of_element_located((By.XPATH, "//h4[contains(text(), 'Roberto Campos Neto')]/ancestor::div[@class='row autoridade no-gutters']")))
        agenda_items = roberto_info.find_elements(By.XPATH, ".//div[@class='col-md-8']//div[contains(@class, 'ExternalClass')]")

        agenda_texts = []
        for item in agenda_items:
            agenda_texts.append(item.text)

        return "\n".join(agenda_texts)
    except Exception as e:
        print(f"Erro ao extrair informações: {e}")
        return None

# Data inicial e final
start_date = datetime(2023, 2, 28)
end_date = datetime(2024, 6, 28)

# Lista de meses com os valores correspondentes no <select>
months = {
    1: 'jan', 2: 'fev', 3: 'mar', 4: 'abr', 5: 'mai', 6: 'jun',
    7: 'jul', 8: 'ago', 9: 'set', 10: 'out', 11: 'nov', 12: 'dez'
}

# Crie e abra o arquivo CSV
with open('agenda_roberto_campos_neto.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Data', 'Agenda'])

    # Iterar pelas datas
    current_date = start_date
    while current_date <= end_date:
        day = current_date.day
        month = months[current_date.month]
        year = current_date.year

        select_date(driver, day, month, year)
        agenda_info = extract_info(driver)
        if not agenda_info:
            agenda_info = "Nenhuma informação encontrada."

        # Escreva a data e as informações no arquivo CSV
        writer.writerow([current_date.strftime('%d/%m/%Y'), agenda_info])

        # Avance para o próximo dia
        current_date += timedelta(days=1)

# Feche o navegador
driver.quit()
