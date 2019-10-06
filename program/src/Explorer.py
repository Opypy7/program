import pandas as pd
import requests
from bs4 import BeautifulSoup
from reader import Reader

class Explorer:

    def __init__(self, url):
        self._reader = Reader(url)
      
    def read_pritty(self):
        print (self._reader._soup.get_text())
        
    def write_to_file(self, file_name):
        text = self._reader._soup.get_text()
        write_text_to_file(file_name,text)

    def explore_links_from_articles(self, file_name):
        list = self._reader.links_to_articles_reader()
        f = open(file_name, "a")
        for element in list:
            f.write(str(element))
            f.write('\n')
        f.close()

    def explore_authors(self, file_name):
        list = self._reader.read_comments_authors()
        if(len(list)>10):
            for i in range(10):
                write_text_to_file(str(i) + file_name, list[i])

def write_text_to_file(file_name, text):
    f = open(file_name, "w")
    f.write(text)
    f.close()


