import requests
from bs4 import BeautifulSoup as BS

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-summary"
querystring = {"region":"IN","lang":"en"}

headers = {
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
    'x-rapidapi-key': "3f07f56135msh68cf7b68f026b15p1edf23jsn407f434efda9"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)