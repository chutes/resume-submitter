from unittest import TestCase

from src.IndeedScrapper import IndeedScrapper


class TestIndeedScrapper(TestCase):
    def test_init(self):
        indeed_scrapper = IndeedScrapper(location='Irivng, Tx', position='Software Engineer')

        self.assertIsInstance(indeed_scrapper, IndeedScrapper)
        self.assertEqual('Irving,+Tx', indeed_scrapper.location)
        self.assertEqual('Software+Engineer', indeed_scrapper.position)


    def test_get_page(self):
        indeed_scrapper = IndeedScrapper(location='Irivng, Tx', position='Software Engineer')

        page = indeed_scrapper.get_page()

        print page
