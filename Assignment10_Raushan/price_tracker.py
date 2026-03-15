
import requests
from bs4 import BeautifulSoup

class PriceTracker:
    def __init__(self, url):
        self.url = url

        self.user_agent = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9"
        }

        self.response = requests.get(url=self.url, headers=self.user_agent).text
        self.soup = BeautifulSoup(self.response, "lxml")

    def product_title(self):
        title = self.soup.find("span", {"id": "productTitle"})

        if title is not None:
            return title.text.strip()
        else:
            return "Tag Not Found"

    def product_price(self):
        price = self.soup.find("span", {"class": "a-price-whole"}) \
                or self.soup.find("span", {"id": "priceblock_ourprice"}) \
                or self.soup.find("span", {"id": "priceblock_dealprice"})

        if price:
            return price.text.strip()
        return "Price not available"

# device = PriceTracker(
#     url="https://www.amazon.in/Samsung-Galaxy-Storage-Additional-Exchange/dp/B07KXC7QRS"
# )
# print(device.product_title())
# print(device.product_price())

realme = PriceTracker(url="https://www.amazon.in/gp/product/B0G3X99DLF/ref=ewc_pr_img_1?smid=A2FED6VUR4SH7E&th=1")
print(realme.product_title())
print(realme.product_price())