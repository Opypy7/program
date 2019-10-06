import pandas as pd
import requests
from bs4 import BeautifulSoup

class Reader:
    def __init__(self, url):
        self._url = url
        if(is_link_ok(self._url) == False):
            return None
        page = requests.get(self._url)
        self._soup = BeautifulSoup(page.content, 'html.parser')

    def links_to_articles_reader(self):
        a_tags = self._soup.find_all('a')
        link_list = [link.get('href') for link in a_tags if is_link_ok(link.get('href'))]
        link_list = [clean_link(link) for link in link_list ]
        return link_list

    def read_comments_authors(self):
        p_tags = self._soup.find_all('p', class_='author')
        link_list = [link.get('author') for link in p_tags if is_link_ok(link.get('author'))]
        return link_list


def is_link_ok(link):
   if( type(link)==str ):
            return (( len(link)>6) & ( link.startswith('http://') | link.startswith('https://')))
   return False
       
def clean_link(url):
    if(is_link_ok(url) == False):
        return None
    else:
        index = str(url).find("#")
        new_url = url[0:index]
        return new_url


