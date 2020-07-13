from bs4 import BeautifulSoup
import requests


def souped(url: str, **query) -> BeautifulSoup:
    return BeautifulSoup(requests.get(url).text, 'html.parser')
