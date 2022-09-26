from parsel import Selector
import requests


# response = requests.get("http://books.toscrape.com")
# selector = Selector(text=response.text)
# titles = selector.css(".product_pod h3 a::attr(title)").getall()

# next_page_url = selector.css(".next a::attr(href)").get()

# for title in titles:
#     print(title)

# print(next_page_url)

URL_BASE = "http://books.toscrape.com/catalogue/"
next_page_url = 'page-1.html'

while next_page_url:
    response = requests.get(URL_BASE + next_page_url)
    selector = Selector(text=response.text)

    products = selector.css(".product_pod")

    for product in products:
        title = product.css("h3 a::attr(title)").get()
        price = product.css(".price_color::text").get()
        print(title, price)

    next_page_url = selector.css(".next a::attr(href)").get()
