# Projeto de Extração e Tratamento de Dados da Agenda do Banco Central

Este projeto tem como objetivo extrair e processar dados da agenda de Roberto Campos Neto, presidente do Banco Central do Brasil, a partir do site oficial. Os dados extraídos são salvos em um arquivo CSV e, posteriormente, tratados para gerar um arquivo Excel com informações detalhadas sobre cada reunião.

## Estrutura do Projeto

- `extração_de_dados.py`: Script que utiliza Selenium para navegar e extrair dados do site do Banco Central.
- `tratamentos_de_dados.py`: Script que utiliza Pandas para processar os dados extraídos e salvá-los em um arquivo Excel.
- `requirements.txt`: Lista de dependências necessárias para rodar os scripts.

## Requisitos

- Python 3.7 ou superior
- Google Chrome instalado
- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) compatível com a versão do seu Chrome

## Instalação

1. Clone este repositório:
    ```sh
    git clone https://github.com/seu_usuario/seu_repositorio.git
    cd seu_repositorio
    ```

2. Crie e ative um ambiente virtual:
    ```sh
    python -m venv venv
    source venv/bin/activate # Linux/Mac
    venv\Scripts\activate # Windows
    ```

3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

4. Baixe o [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) e coloque o executável na mesma pasta que os scripts.

## Uso

### Extração de Dados

1. Execute o script `extração_de_dados.py`:
    ```sh
    python extração_de_dados.py
    ```

   Este script irá navegar no site do Banco Central, selecionar as datas desejadas e salvar as informações da agenda de Roberto Campos Neto em um arquivo CSV chamado `agenda_roberto_campos_neto.csv`.

### Tratamento de Dados

2. Execute o script `tratamentos_de_dados.py`:
    ```sh
    python tratamentos_de_dados.py
    ```

   Este script irá processar o arquivo CSV gerado anteriormente e criar um arquivo Excel `processed_agenda.xlsx` com informações detalhadas sobre cada reunião.

## Exemplo de Dados

Os dados extraídos são salvos no seguinte formato:

```csv
Data,Agenda
28/02/2023,"Manhã
11:00 às 12:00 – Reunião com Gilberto Tomazoni, CEO Global, Marcela de Sousa Afonso Rocha, Diretora Executiva de Assuntos Corporativos, e Mauricio José dos Santos Bauer, Diretor de Sustentabilidade da JBS, no Edifício-Sede do Banco Central, em Brasília, para tratar de assuntos institucionais. (fechado à imprensa)
Tarde
14:00 às 14:30 – Reunião com o Ministro do Tribunal de Contas da União, Antonio Anastasia, em Brasília, para tratar de assuntos institucionais. (fechado à imprensa)
15:00 às 15:30 - Reunião com Daniel Rittner, da CNN Brasil, sem previsão de publicação."
...
```

## Contribuição

Sinta-se à vontade para abrir issues e enviar pull requests. Toda contribuição é bem-vinda!

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para obter mais informações.
