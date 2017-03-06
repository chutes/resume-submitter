from unittest import TestCase

from src import IndeedScrapper


class TestIndeedScrapper(TestCase):
    def test_init(self):
        indeed_scrapper = IndeedScrapper()