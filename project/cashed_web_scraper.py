from project.contracts.INeedConcurrency import INeedConcurrency
from project.contracts.IWebScraper import IWebScraper


class CashedWebScraper(IWebScraper, INeedConcurrency):
    @property
    def concurrency(self) -> int:
        pass

    def scrape(self, *args, **kwargs) -> None:
        print('scrape')
