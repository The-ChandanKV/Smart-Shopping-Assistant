from scraper.amazon import get_amazon_price_link
from scraper.flipkart import get_flipkart_price_link

def get_best_price(item):
    a_price, a_link = get_amazon_price_link(item)
    f_price, f_link = get_flipkart_price_link(item)

    if a_price < f_price:
        return a_price, a_link
    else:
        return f_price, f_link
