from bs4 import BeautifulSoup
import cloudscraper
import re
import time
import requests
import os

def scrap_book_data(url):
    scraper = cloudscraper.create_scraper(browser={'browser': 'firefox','platform': \
        'windows','mobile': False})

    html = scraper.get(url).content
    soup = BeautifulSoup(html, "html5lib")
    print(get_title(soup))
    print(get_author(soup))
    get_cover(soup)
    
    if os.path.exists("cover.jpg"):
        os.remove("cover.jpg")
        print(f"Cover file has been successfully removed.")

def get_title(novel_soup):
    return novel_soup.find("h3", class_="title").text

def get_author(novel_soup):
    author_element = novel_soup.find("h3", text="Author:")
    return author_element.find_next_sibling('a').text

def get_cover(novel_soup):
    cover_url = novel_soup.find("div", class_="book").find("img").get("src")
    
    scraper = cloudscraper.create_scraper(browser={'browser': 'firefox','platform': \
        'windows','mobile': False})

    image_data = scraper.get(cover_url).content

    # Specify the local file path where you want to save the image
    local_file_path = "cover.jpg"  # Change this to your desired file path and name

    # Save the image to your local file
    with open(local_file_path, "wb") as file:
        file.write(image_data)

    print(f"Image downloaded and saved to {local_file_path}")
