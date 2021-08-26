import requests, lxml, smtplib, os
from bs4 import BeautifulSoup

ITEM_URL = "https://www.amazon.com/Overclocked-Graphics-Afterburner-Overclocking-DisplayPort/dp/B097NF1CYQ/ref=sr_1_1_sspa?dchild=1&keywords=rtx+3060&qid=1625582023&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzMjNGTU02RExBUTNRJmVuY3J5cHRlZElkPUEwNTI0MTA2MlRFREk4VFNJQjQ0VyZlbmNyeXB0ZWRBZElkPUEwNzM1MTg5MTFYNldUWjhNMk83NCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
header = {
    "Accept-Language": "en-US,en;q=0.9,la;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

response = requests.get(url=ITEM_URL, headers=header)
response.raise_for_status()

soup = BeautifulSoup(response.content, "lxml")

price_info = soup.find(name="span", id="priceblock_ourprice", class_="a-size-medium a-color-price priceBlockBuyingPriceString")
item_price = float(price_info.getText().split("$")[1])
my_price = 399.99


if item_price <= my_price:
    myEmail = 'uzairt321@gmail.com'
    myPassword = os.environ.get("PASS")

    mail_content = f"The RTX 3060 price is now less than ${my_price}. Check the link: {ITEM_URL}."
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=myEmail, password=myPassword)
        connection.sendmail(from_addr=myEmail, to_addrs='usiam@u.rochester.edu',
                            msg=mail_content)
