from bs4 import BeautifulSoup
from pycurl import pycurl


class Scrapper:
    def __init__(self, location, position):
        self.location = location
        self.position = position


