from bs4 import BeautifulSoup
import cloudscraper
import os
import re
from ebooklib import epub

class Novel:
    novel_epub = epub.EpubBook()
    
    def __init__(self, url, title=None, author=None, cover=None):
        self.scraper = cloudscraper.create_scraper(browser={'browser': 'firefox','platform': \
            'windows','mobile': False})
        self.html = self.scraper.get(url).content
        self.soup = BeautifulSoup(self.html, "html5lib")
        
        self.url = url
        self.set_title(title)
        self.set_author(author)
        self.get_cover()
    
    def __str__(self) -> str:
        novel_print = f"Title: {self.title}\n"
        novel_print += f"Author: {self.author}\n"
        novel_print += f"URL: {self.url}"
        return novel_print
            
    def set_title(self, title=None):
        if not title:
            title = self.soup.find("h3", class_="title").text
        self.title = title
        return title
    
    def set_author(self, author=None):
        if not author:
            author = self.soup.find("h3", text="Author:").find_next_sibling('a').text
        self.author = author
        return author
    
    def get_cover(self):
        cover_url = self.soup.find("div", class_="book").find("img").get("src")

        image_data = self.scraper.get(cover_url).content

        local_file_path = "cover.jpg"
        with open(local_file_path, "wb") as file:
            file.write(image_data)

        print(f"Image downloaded and saved to {local_file_path}")
    
    def delete_cover_file(self):
        if os.path.exists("cover.jpg"):
            os.remove("cover.jpg")
            print(f"Cover file has been successfully removed.")
 