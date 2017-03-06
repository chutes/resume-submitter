from bs4 import BeautifulSoup
import pycurl
from StringIO import StringIO
from urllib import urlencode
import re


class IndeedScrapper:
    def __init__(self, location, position):
        self.location = '+'.join(location.split())
        self.position = '+'.join(position.split())

    def get_jobs(self):
        buffer = StringIO()

        curl = pycurl.Curl()

        curl.setopt(curl.URL, 'https://www.indeed.com/jobs?q={}&l={}'.format(self.position, self.location))
        curl.setopt(curl.WRITEDATA, buffer)
        curl.setopt(curl.FOLLOWLOCATION, True)

        curl.perform()
        curl.close()

        body = buffer.getvalue()
        # Body is a string in some encoding.
        # In Python 2, we can print it without knowing what the encoding is.

        soup = BeautifulSoup(body, 'lxml')

        results_body = soup.find('table', {'id': 'resultsBody'})

        jobs = results_body.find_all('div', {'class': re.compile(r'result')})

        job_urls = []
        for job in jobs:
            easily_apply = job.find_all('span', {'class': 'iaLabel'})

            if easily_apply:
                links = job.find_all('a', {'data-tn-element': 'jobTitle'}, href=True)
                for link in links:
                    job_urls.append(link['href'])

        return job_urls


