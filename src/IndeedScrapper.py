from bs4 import BeautifulSoup
import pycurl
from StringIO import StringIO
from urllib import urlencode


class IndeedScrapper:
    def __init__(self, location, position):
        self.location = '+'.join(location.split())
        self.position = '+'.join(position.split())

    def get_page(self):
        buffer = StringIO()
        curl = pycurl.Curl()
        curl.setopt(curl.URL, 'https://www.indeed.com/jobs?q=linux+engineering&l=')
        curl.setopt(curl.WRITEDATA, buffer)
        curl.setopt(curl.FOLLOWLOCATION, True)
        curl.perform()
        curl.close()

        body = buffer.getvalue()
        # Body is a string in some encoding.
        # In Python 2, we can print it without knowing what the encoding is.
        return body

    def post_page(self):
        c = pycurl.Curl()
        c.setopt(c.URL, 'http://pycurl.io/tests/testpostvars.php')

        post_data = {'field': 'value'}
        # Form data must be provided already urlencoded.
        postfields = urlencode(post_data)
        # Sets request method to POST,
        # Content-Type header to application/x-www-form-urlencoded
        # and data to send in request body.
        c.setopt(c.POSTFIELDS, postfields)

        c.perform()
        c.close()

