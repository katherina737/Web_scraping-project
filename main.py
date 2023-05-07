#-----------------getting price from Amazon:
from bs4 import BeautifulSoup
import requests

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
accept_language = "gzip, deflate"
headers={
    "User-Agent":user_agent,
    "Accept-Language": accept_language,
}
amazon_url ="https://www.amazon.co.uk/Lechuza-13384-CUBE-Planter-Pot/dp/B019GV8D3E/ref=sr_1_10?keywords=self%2Bwatering%2Bpots%2Bfor%2Bplants%2Bindoors&qid=1645398801&sprefix=selfwatering%2Bpot%2Caps%2C132&sr=8-10&th=1"

response = requests.get(url=amazon_url,headers=headers)
web = response.text

soup = BeautifulSoup(web, "html.parser")
price = soup.find("span", class_="a-offscreen")
price_text = price.getText()
price = price_text[1:6]
price_float = float(price)

print(f"The price of item is £{price_float}")

