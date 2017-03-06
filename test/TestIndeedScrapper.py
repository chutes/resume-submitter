from unittest import TestCase

from src.IndeedScrapper import IndeedScrapper


class TestIndeedScrapper(TestCase):
    def test_init(self):
        indeed_scrapper = IndeedScrapper(location='Irivng, Tx', position='Software Engineer')

        self.assertIsInstance(indeed_scrapper, IndeedScrapper)
        self.assertIsInstance(indeed_scrapper, IndeedScrapper)