import requests
from bs4 import BeautifulSoup
import lxml
import smtplib


def send_mail():
    user_mail = "sonuasif174@gmail.com"
    password = "ksajxrwvsaoubyev"

    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=user_mail,password=password)
    connection.sendmail(from_addr=user_mail,to_addrs=user_mail,msg=f"subject:Hurry up price is down!!\n\nGo and Buy now your, {product_name} is at your affordable price\n\n{URL}")
    connection.close()

URL = "https://www.amazon.in/HP-K500F-Gaming-Keyboard-7ZZ97AA/dp/B08498D67S/ref=sr_1_9?crid=2MOA8KAP92XXB&keywords=keyboard&qid=1689574380&sprefix=key%2Caps%2C240&sr=8-9"
affordable_price = 900.0


header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,hi;q=0.8"
}

try:
    response = requests.get(URL, headers=header)
    web_page = response.text
except:
    print("Response Not Get")
    exit(-1)

soup = BeautifulSoup(web_page, "lxml")
price = float(soup.find(name="span",class_="a-offscreen").text[1:])
product_name = soup.find(name="span",id="productTitle").text.strip(" ")

if affordable_price >= price:
    send_mail()
    print("Mail send")