from reader import Reader
from explorer import Explorer

# Specify url
url = 'https://www.gazeta.pl/0,0.html'
ex = Explorer(url)
ex.write_to_file("explorer.txt")
ex.explore_links_from_articles("links_to_articles_reader.txt")
ex.explore_authors("authors.txt")