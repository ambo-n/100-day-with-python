from bs4 import BeautifulSoup
import requests, smtplib, os
from dotenv import load_dotenv
load_dotenv()

PRACTICE_URL = "https://appbrewery.github.io/instant_pot/"
YOUR_EMAIL = os.getenv("EMAIL")
LIVE_URL ="https://www.amazon.com.au/dp/B008IC0Z8Y/ref=sspa_dk_detail_3?pd_rd_i=B008IC0Z8Y&pd_rd_w=ElcU0&content-id=amzn1.sym.1466049c-a1d9-4b3d-b57f-ad4194b25db8&pf_rd_p=1466049c-a1d9-4b3d-b57f-ad4194b25db8&pf_rd_r=NT1Y21JVESEHMB64SXNM&pd_rd_wg=dsRK1&pd_rd_r=0ffad834-de3c-469f-89ec-ddd5dccbaf6c&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWw&th=1"
EMAIL_APP_PASSWORD = os.getenv("EMAIL_APP_PASSWORD")
RECEIVER_EMAIL= os.getenv("RECEIVER_EMAIL")

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
    "Accept-Language": "en-AU,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,vi;q=0.6"
}

response = requests.get(url=LIVE_URL, headers=headers)
response.raise_for_status()

content = response.content
soup = BeautifulSoup(content, 'html.parser')

price = float(soup.find(class_="a-offscreen").get_text().split("$")[1])#type: ignore
discount = soup.find(class_="a-size-large a-color-price savingPriceOverride aok-align-center reinventPriceSavingsPercentageMargin savingsPercentage")
try:
    discount_float = float(soup.find(class_="a-size-large a-color-price savingPriceOverride aok-align-center reinventPriceSavingsPercentageMargin savingsPercentage").get_text().split("%")[0])
except AttributeError:
    discount_float = 0
final_price = round(price*((100+discount_float)/100),2)

item = soup.select_one(selector="h1 span").get_text().encode("UTF-8") # type: ignore

TARGET_PRICE = 150

if final_price < TARGET_PRICE:
    message = f"{item} is on sale for {final_price}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=YOUR_EMAIL,#type: ignore
                        password=EMAIL_APP_PASSWORD) #type: ignore
        connection.sendmail(from_addr=YOUR_EMAIL, #type: ignore
                            to_addrs=RECEIVER_EMAIL, #type: ignore
                            msg=f"Subject: Amazon Price Alert! \n\n {message} \n Buy now: {LIVE_URL}")