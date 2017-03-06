from bs4 import BeautifulSoup
import pycurl
from StringIO import StringIO
from urllib import urlencode
from selenium import webdriver
import re


class IndeedScrapper:
    def __init__(self, location, position):
        self.location = '+'.join(location.split())
        self.position = '+'.join(position.split())

    def get_job_urls(self):
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

    def get_job_page(self, job_url):
        driver = webdriver.Chrome('/usr/local/bin/chromedriver')

        driver.get('https://www.indeed.com/{}'.format(job_url))

        # html = driver.page_source
        # soup = BeautifulSoup(html, 'lxml')
        # element = driver.find_element_by_id('indeed-apply-js').click()

        soup = BeautifulSoup(driver.page_source, 'lxml')

        print soup

        driver.close()



