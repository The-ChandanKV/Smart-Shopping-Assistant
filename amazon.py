import requests
from bs4 import BeautifulSoup

def get_amazon_price_link(item):
    headers = {"User-Agent": "Mozilla/5.0"}
    query = item.replace(" ", "+")
    url = f"https://www.amazon.in/s?k={query}"

    try:
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        product = soup.select_one('.s-main-slot .s-result-item')

        price_tag = product.select_one('.a-price-whole')
        link_tag = product.select_one('a.a-link-normal')

        price = int(price_tag.text.replace(",", "")) if price_tag else float('inf')
        link = "https://www.amazon.in" + link_tag['href'] if link_tag else "N/A"

        return price, link
    except:
        return float('inf'), "N/A"
