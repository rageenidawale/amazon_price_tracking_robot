import requests
from bs4 import BeautifulSoup
import smtplib

my_email = ""
my_password = ""
senders_email = ""

product_link = "https://www.amazon.in/boAt-Smartwatch-Multiple-Monitoring-Resistance/dp/B096VF5YYF/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
response = requests.get(url=product_link, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")
print(soup)

product_title = soup.find(id="productTitle").get_text().strip()
print(product_title)

price = soup.find(name="span", class_="a-price a-text-price a-size-medium apexPriceToPay").getText()
split_price_symbol = price.split("₹")[1]
remove_price_comma = split_price_symbol.replace(",", "")
price = float(remove_price_comma)
print(price)

target_price = 3000

if price <= target_price:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=senders_email,
            msg=f"Subject:Amazon Price Drop Alert!\n\n{product_title} is now ₹{price}!\n{product_link}"
        )
