from bs4 import BeautifulSoup
import os
import re
from ebooklib import epub

class Chapter:
    
    def __init__(self, novel, number):
        self.chapter_number = number
        self.chapter_url = self.create_chapter_url(novel.url, number)
        self.soup = BeautifulSoup(novel.scraper.get(self.chapter_url).content, "html5lib")
        self.title = self.get_chapter_title()
        self.paragraphs = self.get_chapter_paragraphs()
    
    def __str__(self) -> str:
        return self.title
        
    def create_chapter_url(self, base_url, chapter_number):
        if not base_url.endswith("/"):
            base_url += "/"
        return f"{base_url}chapter-{chapter_number}"
    
    def get_chapter_title(self):
        title = self.soup.find(re.compile("h2|h3|h4")).text.strip()
        return title
    
    def get_chapter_paragraphs(self):
        paragraphs = self.soup.find("div", id=re.compile("chr-content")).find_all("p")
        chapter_text = "".join([p.text for p in paragraphs if "Translator:" not in p.get_text()])
        return chapter_text
