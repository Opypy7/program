import pandas as pd
import requests
from bs4 import BeautifulSoup

def links_to_articles_reader(url):
    if(is_link_ok(url) == False):
        return None
    r = requests.get(url)
    html_doc = r.text
    print(html_doc)
    soup = BeautifulSoup(html_doc)
    a_tags = soup.find_all('a')
    link_list = list(str())
    link_list = [link.get('href') for link in a_tags if is_link_ok(link.get('href'))]
    return link_list

def is_link_ok(link):
    if( type(link)==str ):
            return (( len(link)>6) & ( link.startswith('http://') | link.startswith('https://')))
    return False





