import requests
from bs4 import BeautifulSoup

def get_flipkart_price_link(item):
    headers = {"User-Agent": "Mozilla/5.0"}
    query = item.replace(" ", "%20")
    url = f"https://www.flipkart.com/search?q={query}"

    try:
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        product = soup.select_one('._1AtVbE')

        price_tag = product.select_one('._30jeq3')
        link_tag = product.select_one('a._1fQZEK') or product.select_one('a.IRpwTa')

        price = int(price_tag.text.replace("₹", "").replace(",", "")) if price_tag else float('inf')
        link = "https://www.flipkart.com" + link_tag['href'] if link_tag else "N/A"

        return price, link
    except:
        return float('inf'), "N/A"
