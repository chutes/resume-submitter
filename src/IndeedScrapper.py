from bs4 import BeautifulSoup
import pycurl
from StringIO import StringIO


class Scrapper:
    def __init__(self, location, position):
        self.location = location
        self.position = position


    def get_page(self):
        buffer = StringIO()
        c = pycurl.Curl()
        c.setopt(c.URL, 'http://pycurl.io/')
        c.setopt(c.WRITEDATA, buffer)
        c.perform()
        c.close()

        body = buffer.getvalue()
        # Body is a string in some encoding.
        # In Python 2, we can print it without knowing what the encoding is.
        print(body)

