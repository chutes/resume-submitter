from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import requests


class IndeedScrapper:
    def __init__(self, location, position):
        self.location = '+'.join(location.split())
        self.position = '+'.join(position.split())

    def get_job_urls(self):
        response = requests.get('https://www.indeed.com/jobs?q={}&l={}'.format(self.position, self.location),
                                allow_redirects=True)

        soup = BeautifulSoup(response.text, 'lxml')

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
        driver.maximize_window() # Maximize Window
        driver.implicitly_wait(10)  # Let the page load for 10 seconds so all elements are there

        driver.get('https://www.indeed.com/{}'.format(job_url))

        # Click the apply button and allow the Ajax form to load
        driver.find_element_by_class_name('indeed-apply-button').click()
        try:  # Currently does not work. trying to find a way to access the continue button using css selector.`
            driver.find_element_by_css_selector('a.button_content.form-page-next').click()
        finally:
            driver.close()

    def get_cookie(self):
        """ Get a session object to pass between requests"""
        pass














