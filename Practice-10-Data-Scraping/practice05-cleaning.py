from parsel import Selector
import requests


# retirando sujeira no preço e no final da descrição (..more)
URL_BASE = "http://books.toscrape.com/catalogue/"
next_page_url = 'page-1.html'

while next_page_url:
    response = requests.get(URL_BASE + next_page_url)
    selector = Selector(text=response.text)

    products = selector.css(".product_pod")

    for product in products:
        title = product.css("h3 a::attr(title)").get()
        price = product.css(".price_color::text").re_first(r"£\d+\.\d{2}")
        book_link = product.css("h3 a::attr(href)").get()
        detailed_page_url = URL_BASE + book_link

        detailed_response = requests.get(detailed_page_url)
        detailed_selector = Selector(text=detailed_response.text)
        description = detailed_selector.css(
              "#product_description ~ p::text").get()

        suffix = "...more"
        if description.endswith(suffix):
            description = description[:-len(suffix)]

        print(title, price, description, "\n\n")

    next_page_url = selector.css(".next a::attr(href)").get()
