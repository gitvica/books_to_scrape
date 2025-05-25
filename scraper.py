import requests
from bs4 import BeautifulSoup

def scrape_books():
    url = "https://books.toscrape.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    books = []

    for article in soup.select("article.product_pod"):
        title = article.h3.a["title"]
        price = article.select_one(".price_color").text
        rating = article.p["class"][1]
        books.append({
            "title": title,
            "price": price,
            "rating": rating
        })

    return books
    