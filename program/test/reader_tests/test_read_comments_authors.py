import unittest
from src.reader import read_comments_authors

class test_read_comments_authors(unittest.TestCase):
       def test_for_empty_link(self):
           assert read_comments_authors('') is None
       
       def test_for_normal_link(self):
           assert read_comments_authors('https://www.gazeta.pl/0,0.html') != []

if __name__ == '__main__':
    unittest.main()
    test_for_empty_link()
    test_for_normal_link()
