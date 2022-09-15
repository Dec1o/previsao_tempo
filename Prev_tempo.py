import requests

API_KEY = 'Enter your key'
Cidade = str(input('\nDigite o nome da cidade que você deseja saber a temperatura: '))
Link = f'https://api.openweathermap.org/data/2.5/weather?q={Cidade}&appid={API_KEY}'

Requisicao = requests.get(Link)
Requisicao_dic = Requisicao.json()
Temperatura = Requisicao_dic['main']['temp'] - 273.15
print(f"\nA temperatura de {Cidade} é: {Temperatura:.1f}ºC")
