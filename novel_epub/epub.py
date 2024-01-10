import os
import re
from ebooklib import epub

class NovelEpub:
    book = epub.EpubBook()
    nav_css = epub.EpubItem(
        uid="style_nav",
        file_name="style/nav.css",
        media_type="text/css",
        content="BODY {color: white;}",
    )
    
    def __init__(self, novel):
        self.novel = novel
        self.book.set_title(novel.title)
        self.book.add_author(novel.author)
        self.book.set_language("en")
        self.book.spine = ["nav"]
        if os.path.exists("cover.jpg"):
            self.book.set_cover("cover.jpg", open("cover.jpg", "rb").read())
        
        self.set_chapters()
        
    
    def set_chapters(self):
        if not self.novel.chapters:
            self.novel.get_chapters()
            
        for chapter_number in range(self.novel.start_chapter, self.novel.end_chapter + 1):
            filename = f"chapter_{chapter_number}.xhtml"
            chapter = self.novel.chapters[chapter_number - 1]
            print(chapter)
            
            paragraphs = chapter.paragraphs.split("\n")
            chapter_text = "".join(["<p>" + p + "</p>" for p in paragraphs])
            chapter_text = "<h3>" + chapter.title + "</h3>" + chapter_text

            chapter = epub.EpubHtml(title=chapter.title, file_name=filename, lang="en")
            chapter.content = chapter_text
            
            self.book.toc.append(epub.Link(filename, chapter.title, "chapter"))
            self.book.spine.append(chapter)
            self.book.add_item(chapter)
            
        self.book.add_item(epub.EpubNcx())
        self.book.add_item(epub.EpubNav())
        
        nav_css = epub.EpubItem(
        uid="style_nav",
        file_name="style/nav.css",
        media_type="text/css",
        content="BODY {color: white;}",
        )
        
        self.book.add_item(nav_css)
        epub.write_epub(f"{self.novel.title.replace(' ', '_')}.epub", self.book, {})
        