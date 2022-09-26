from parsel import Selector
import requests


URL_BASE = "http://books.toscrape.com/catalogue/"

response = requests.get(URL_BASE + "page-1.html")
selector = Selector(text=response.text)

book_link = selector.css(".product_pod h3 a::attr(href)").get()
detailed_page_url = URL_BASE + book_link

detailed_response = requests.get(detailed_page_url)
detailed_selector = Selector(text=detailed_response.text)

description = detailed_selector.css("#product_description ~ p::text").get()
print(description)
