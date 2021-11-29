import requests
import json
URL = 'https://www.cbr-xml-daily.ru/daily_json.js'
response = requests.get(URL)
#print(response)
data = json.loads(response.text)
#print(data)
print('Курс USD {} на дату {}'.format(data['Valute']['USD']['Value'], data['Timestamp']))