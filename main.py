import asyncio
import aiohttp
from functools import lru_cache


class WebScraper:
    def __init__(self, max_concurrency=5):
        self.max_concurrency = max_concurrency

    @lru_cache(maxsize=1000)
    async def fetch_url(self, url):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url, timeout=5) as response:
                    return await response.text()
            except Exception as e:
                print(f"Failed {url}: {e}")
                raise

    async def scrape(self, urls):
        semaphore = asyncio.Semaphore(self.max_concurrency)
        async def worker(url):
            async with semaphore:
                return await self.fetch_url(url)
        return await asyncio.gather(*[worker(url) for url in urls], return_exceptions=True)


# Example usage:
async def main():
    scraper = WebScraper()
    urls = ["https://example.com", "https://python.org"]
    results = await scraper.scrape(urls)
    print(results)


asyncio.run(main())