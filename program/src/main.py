from reader import links_to_articles_reader

# Specify url
url = 'https://www.gazeta.pl/0,0.html'
links_list = links_to_articles_reader(url)
print(links_list)