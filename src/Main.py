from src.IndeedScrapper import IndeedScrapper


class Main:

    def run(self):
        indeed_scrapper = IndeedScrapper(
            location='Irving Texas',
            position='Software Engineer'
        )

        soup = indeed_scrapper.get_job_urls()



