from abc import ABC, abstractmethod


class IWebScraper(ABC):
    @abstractmethod
    def scrape(self, *args, **kwargs) -> None:
        pass
