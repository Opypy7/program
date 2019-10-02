import pytest
from src.reader import links_to_articles_reader


def test_for_empty_link():
    assert links_to_articles_reader('') is None

def test_for_normal_link():
    assert links_to_articles_reader('https://www.gazeta.pl/0,0.html') != list()


