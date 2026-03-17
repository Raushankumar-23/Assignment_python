import requests
from bs4 import BeautifulSoup


class PriceTracker:

    def __init__(self, url):
        self.url = url
        self.soup = None

    def fetch_data(self):
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
                "Accept-Language": "en-IN,en;q=0.9"
            }

            response = requests.get(self.url, headers=headers)

            if response.status_code == 200:
                # changed parser to lxml (more reliable)
                self.soup = BeautifulSoup(response.text, "lxml")
            else:
                print("Error: Unable to fetch page", response.status_code)

        except Exception as e:
            print("Request Error:", e)

    def get_title(self):
        try:
            title = self.soup.find("span", id="productTitle")
            if title:
                return title.text.strip()
            else:
                return "Title not found"
        except:
            return "Error getting title"

    def get_price(self):
        try:
            # UPDATED: Amazon mostly uses a-offscreen
            price = self.soup.find("span", class_="a-offscreen")

            if price:
                return price.text.strip()
            else:
                return "Price not found"

        except:
            return "Error getting price"

    def convert_price(self, price_str):
        try:
            # remove ₹ and comma
            price = price_str.replace("₹", "").replace(",", "")
            return float(price)
        except:
            return 0.0

    def compare_price(self, current_price, target_price):
        if current_price == 0:
            print("Price not available for comparison")
        elif current_price <= target_price:
            print("Price dropped! Buy now!")
        else:
            print("Price is still high")


# -------- MAIN PROGRAM -------- #

url = "https://www.amazon.in/gp/product/B0G3X99DLF"

tracker = PriceTracker(url)

tracker.fetch_data()

title = tracker.get_title()
price_str = tracker.get_price()

print("Product:", title)
print("Price:", price_str)

price_value = tracker.convert_price(price_str)

# Set your target price
target_price = 15000

tracker.compare_price(price_value, target_price)