import asyncio
from playwright.async_api import async_playwright
import json
from collections import defaultdict

class DynamicUrlCrawler:
    def __init__(self, urls):
        self.urls = urls
        self.product_urls = defaultdict(list)

    async def start_crawl(self):
        async with async_playwright() as p:
            browser = await p.chromium.launch( headless = True )
            tasks = []
            
            for url in self.urls:
                task = asyncio.create_task(self.crawl_page(browser, url))
                tasks.append(task)
            
            await asyncio.gather(*tasks)
            self.save_results()
            await browser.close()

    async def crawl_page(self, browser, url):
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto(url)
        await self.scrape_page(page,url)

        await context.close()

    async def scrape_page(self, page,url):
        previous_height = None

        while True:
            await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            await page.wait_for_timeout(2000)
            current_height = await page.evaluate("document.body.scrollHeight")
            if current_height == previous_height:
                break
            previous_height = current_height

        product_links = await page.locator('a[href*="/product/"],a[href*="/dp/"], a[href*="/item/"],a[href*="/items/"], a[href*="/p/"], a[href*="/products/"], a[href*="/shop/"], a[href*="/detail/"]').all()
        urls=set()
        for link in product_links:
            url_link = await link.get_attribute("href")
            url_link= url_link.replace(url,'',1)
            if len(url_link)>1:
                if url_link[0]=='/':
                    urls.add(url_link)
                else:
                    urls.add('/'+url_link)
        self.product_urls[url].extend(list(urls))

    def save_results(self):
        with open("product_urls.json", "w") as f:
            json.dump({"product_urls": self.product_urls}, f, indent=4)

if __name__ == "__main__":
    url = ["https://www.amazon.in/s?k=i+phone+15+pro", "https://www.flipkart.com/","https://www.flipkart.com/","https://monkeytype.com","https://zevarking.com/collections/whats-new","https://zevarking.com/collections/best-sellers"]
    crawler = DynamicUrlCrawler(url)
    asyncio.run(crawler.start_crawl())