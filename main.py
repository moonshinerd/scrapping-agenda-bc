from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time
import os

# Obtenha o caminho completo do chromedriver
path_chromedriver = os.path.join(os.getcwd(), "chromedriver")

# Configure o serviço do chromedriver
service = Service(path_chromedriver)

# Configure as opções do Chrome
options = Options()

driver = webdriver.Chrome(service=service, options=options)

# Abra a URL desejada
driver.get("https://www.bcb.gov.br/acessoinformacao/agendaautoridades")

# Encontre todos os elementos <select> pela classe
select_elements = driver.find_elements("css selector", "select.form-control.mr-sm-2.mb-2.mb-sm-0")

# Crie uma instância de Select passando o primeiro elemento encontrado
select_day = Select(select_elements[0])

# Selecione uma opção pelo valor
select_day.select_by_value("2")  # Altere o valor conforme necessário

# Crie uma instância de Select passando o segundo elemento encontrado
select_month = Select(select_elements[1])

# Selecione o mês "Jan" pelo valor
select_month.select_by_value("jan")

# Encontre o elemento <select> para o ano
select_year_element = driver.find_element("css selector", "select.form-control")

# Crie uma instância de Select passando o elemento encontrado
select_year = Select(select_year_element)

# Selecione o ano "2025" pelo valor
select_year.select_by_value("2023")

# Aguarde alguns segundos antes de fechar o navegador
time.sleep(125)  # Aguarda 125 segundos (você pode ajustar o tempo conforme necessário)

# Feche o navegador
#driver.quit()
