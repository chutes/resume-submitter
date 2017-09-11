from unittest import TestCase

from src.IndeedScrapper import IndeedScrapper


class TestIndeedScrapper(TestCase):
    def test_init(self):
        indeed_scrapper = IndeedScrapper(
            location='Irving Tx',
            position='Software Engineer',

        )

        self.assertIsInstance(indeed_scrapper, IndeedScrapper)
        self.assertEqual('Irving+Tx', indeed_scrapper.location)
        self.assertEqual('Software+Engineer', indeed_scrapper.position)

    def test_get_page(self):
        indeed_scrapper = IndeedScrapper(location='Irving Tx', position='Software Engineer')

        job_urls = indeed_scrapper.get_job_urls()

        for url in job_urls:
            print url

    def test_get_job_page(self):
        job_url = '/company/Enshire-Inc/jobs/Bluetooth-Software-Engineer-e1ad43b2641e7d88?fccid=faf88be40e881896'

        indeed_scrapper = IndeedScrapper(location='Irving Tx', position='Software Engineer')

        job_page = indeed_scrapper.get_job_page(job_url)

        # print job_page

    def test_authentication(self):
        indeed_scrapper = IndeedScrapper(location='Irving Tx', position='Software Engineer')

        cookie = indeed_scrapper.get_cookie()

        print cookie
