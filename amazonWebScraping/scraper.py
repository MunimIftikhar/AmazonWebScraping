from scrapy.crawler import CrawlerProcess
from scrapy import settings

from amazonWebScraping.spiders.amazon_Spider import amazonSpider


if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(amazonSpider)

    # Start the crawling
    process.start()

