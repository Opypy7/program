import unittest
from src.reader import links_to_articles_reader

class test_links_to_articles_reader(unittest.TestCase):

   def test_for_empty_link(self):
       assert links_to_articles_reader('') is None
       
   def test_for_normal_link(self):
       assert links_to_articles_reader('https://www.gazeta.pl/0,0.html') != []

if __name__ == '__main__':
    unittest.main()
    test_for_empty_link()
    test_for_normal_link()
