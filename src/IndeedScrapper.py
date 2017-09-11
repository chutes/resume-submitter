from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import requests
import urllib.parse


class IndeedScrapper:
    def __init__(self, location, position):
        self.location = '+'.join(location.split())
        self.position = '+'.join(position.split())

    def get_job_urls(self):
        response = requests.get('https://www.indeed.com/jobs?q={}&l={}'.format(self.position, self.location),
                                allow_redirects=True)

        soup = BeautifulSoup(response.text, 'lxml')

        jobs = soup.find('table', {'id': 'resultsBody'}).find_all('div', {'class': re.compile(r'result')})

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
        driver.implicitly_wait(20)

        # Click the apply button and allow the Ajax form to load
        driver.find_element_by_class_name('indeed-apply-button').click()
        # try:  # Currently does not work. trying to find a way to access the continue button using css selector.`
        #     driver.find_element_by_css_selector('a.button_content.form-page-next').click()
        # finally:
        #     driver.close()

    def get_job_category(self):

        """ Get a list of all the different job categories supported on Indeed. Accounting, Engineering,
        etc. Then we will use those categories to make a get a list of all the different types of jobs for each
        category and start performing text analysis against different job listings. This is so we can start understanding
        the different requirements each industry is most looking for with each job"""
        response = requests.get('https://www.indeed.com/find-jobs.jsp')

        soup = BeautifulSoup(response.text, 'lxml')

        category_table = soup.find('table', {'id': 'categories'}).find_all('td')

        job_categories = []
        for row in category_table:
            for item in row:
                element = item.getText()
                job_categories.append(element)

        return job_categories

    def get_list_of_jobs(self, job_categories):
        """Get a list of each job title for each job category"""
        job_titles = []
        for job in job_categories:
            encoded_job = urllib.parse.urlencode({'cat': job})
            response = requests.get('https://www.indeed.com/find-jobs.jsp?{}'.format(encoded_job))

            soup = BeautifulSoup(response.text, 'lxml')

            job_title_table = soup.find('table', {'id': 'titles'}).find_all('td')

            for row in job_title_table:
                for element in row.find_all('a', {'class': 'jobTitle'}):
                    job_titles.append(element.getText())

        print(job_titles)
        return job_titles

indeed_scrapper = IndeedScrapper(location='Irving Tx', position='Software Engineer')
categories = indeed_scrapper.get_job_category()
indeed_scrapper.get_list_of_jobs(categories)













