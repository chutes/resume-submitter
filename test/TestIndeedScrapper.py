from unittest import TestCase

from src.IndeedScrapper import IndeedScrapper
from src.IndeedResumeAnalyzer import IndeedResumeAnalyzer


class TestIndeedScrapper(TestCase):
    def test_init(self):
        indeed_scrapper = IndeedScrapper(
            location='Irving Tx',
            position='Software Engineer',

        )

        self.assertIsInstance(indeed_scrapper, IndeedScrapper)
        self.assertEqual('Irving+Tx', indeed_scrapper.location)
        self.assertEqual('Software+Engineer', indeed_scrapper.position)

    # def test_get_page(self):
    #     indeed_scrapper = IndeedScrapper(location='Irving Tx', position='Linux Engineer')
    #
    #     job_urls = indeed_scrapper.get_job_urls()
    #
    #     for url in job_urls:
    #         print(url)

    # def test_get_job_page(self):
    #     job_url = '/company/HealthMarkets/jobs/System-Engineer-640d8d8c42babb03?fccid=27dd024b536a1da8'
    #
    #     indeed_scrapper = IndeedScrapper(location='Irving Tx', position='Linux Engineer')
    #
    #     job_page = indeed_scrapper.get_job_page(job_url)
    #
    #     print(job_page)

    # def test_authentication(self):
    #     indeed_scrapper = IndeedScrapper(location='Irving Tx', position='Software Engineer')
    #
    #     cookie = indeed_scrapper.get_cookie()
    #
    #     print(cookie)

    def get_job_categories(self):
        scrapper = IndeedScrapper(location='Irving Tx', position='Software Engineer')
        scrapper.get_job_category()
