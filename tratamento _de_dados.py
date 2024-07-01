import pandas as pd
import os


# Obtenha o caminho completo do chromedriver
path_chromedriver = os.path.join(os.getcwd(), "agenda_roberto_campos_neto.csv")

# Carregar o CSV
df = pd.read_csv(path_chromedriver)

# Função para processar cada linha da agenda
def process_agenda(row):
    # Lista de dicionários para armazenar as reuniões processadas
    meetings = []
    
    # Separar as linhas da agenda
    lines = row.split('\n')
    
    # Variáveis auxiliares
    current_period = ""
    
    for line in lines:
        # Verificar e ignorar as linhas de "Manhã" e "Tarde"
        if line.strip() in ["Manhã", "Tarde"]:
            current_period = line.strip()
            continue
        
        # Dividir as linhas pelo horário e o restante
        if '–' in line:
            time, details = line.split('–', 1)
            time = time.strip()
            details = details.strip()

            # Dividir os detalhes pelo local e assunto
            if 'no' in details:
                subject, location = details.split('no', 1)
                subject = subject.strip()
                location = location.strip().split('para tratar de')[0].strip()
            else:
                subject = details
                location = ""
            
            # Extraindo o órgão e entidade se disponíveis
            orgao, entidade = "", ""
            if "," in subject:
                parts = subject.split(",")
                subject = parts[0].strip()
                orgao_entidade = parts[1].strip().split("da")
                if len(orgao_entidade) > 1:
                    orgao = orgao_entidade[0].strip()
                    entidade = orgao_entidade[1].strip()
            
            # Adicionar a reunião à lista
            meetings.append({
                "Data": row_data,
                "Hora": time,
                "Assunto da Reunião": subject,
                "Local da Reunião": location,
                "Cargo": orgao,
                "Órgão": orgao,
                "Entidade": entidade
            })
    
    return meetings

# Processar cada linha da agenda
processed_data = []
for index, row in df.iterrows():
    row_data = row['Data']
    agenda_data = row['Agenda']
    processed_data.extend(process_agenda(agenda_data))

# Criar um DataFrame com os dados processados
df_processed = pd.DataFrame(processed_data)

# Salvar para um arquivo Excel
df_processed.to_excel("processed_agenda.xlsx", index=False)
