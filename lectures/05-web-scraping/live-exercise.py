import requests
import os

import pandas as pd
from bs4 import BeautifulSoup

from collections import defaultdict


if __name__ == "__main__":

    base_url = "http://books.toscrape.com"
    catalogue_url =" http://books.toscrape.com/catalogue"

    next_url = os.path.join(catalogue_url, "page-1.html")

    book_dict = defaultdict(list)

    while next_url:

        print("".join(["-"] * 80))
        print("Scraping page: {}".format(next_url))
        print("".join(["-"] * 80))

        response = requests.get(next_url)
        soup = BeautifulSoup(response.content, "lxml")

        list_of_books = soup.find("ol")

        for book in list_of_books.find_all("li"):

            book_title = book.find("h3").find("a")["title"]

            book_metadata = book.find("div", class_="product_price").find_all("p")

            book_price = book_metadata[0].get_text(strip=True)
            book_price = float(book_price.split("£")[1].strip())

            book_in_stock = book_metadata[1].get_text(strip=True) == "In stock"

            book_cover_link = os.path.join(catalogue_url, book.find("img", class_="thumbnail")["src"])

            book_dict["Book Title"].append(book_title)
            book_dict["Book Price"].append(book_price)
            book_dict["Book In Stock"].append(book_in_stock)
            book_dict["Book Cover Link"].append(book_cover_link)

            print(book_title, book_price, book_in_stock, book_cover_link)

        next_list_item = soup.find("li", {"class": "next"})

        if next_list_item is not None:
            next_link = next_list_item.find("a")["href"]
            next_url = os.path.join(catalogue_url, next_link)
        else:
            break

    book_df = pd.DataFrame(book_dict)
    book_df.to_csv("books.csv", index=False)

    print(book_df)