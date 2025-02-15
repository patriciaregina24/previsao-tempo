from dotenv import load_dotenv
import os
import requests

load_dotenv()

api_key = os.getenv("API_KEY")
if api_key is None:
    print("Erro: A chave da API não foi encontrada no arquivo .env.")
    exit(1)

cidade = input("Digite a cidade desejada: ")

link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&lang=pt_br"

requisicao = requests.get(link)

try:
    if requisicao.status_code == 200:
        dicio_requisicao = requisicao.json()

        if "main" in dicio_requisicao and "weather" in dicio_requisicao:

            chaves = ["temp", "feels_like", "temp_min", "temp_max", "humidity"]

            valores_celsius = [(dicio_requisicao["main"].get(chave, 0) - 273.15) if chave != "humidity" 
                           else dicio_requisicao["main"].get(chave, 0) for chave in chaves]

            descricao = dicio_requisicao["weather"][0]["description"]

except requests.exceptions.RequestException:
    print("Erro ao tentar acessar a API.")

print(f"Hoje faz {descricao} e a temperatura é de {valores_celsius[0]:.0f} graus Celsius.")
print(f"A sensação térmica é de {valores_celsius[1]:.0f} graus Celsius.")
print(f"Mínima de {valores_celsius[2]:.0f} graus e Máxima de {valores_celsius[3]:.0f} graus.")
print(f"A umidade é de {valores_celsius[4]}%.")