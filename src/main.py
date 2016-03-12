from scrapy.crawler import CrawlerProcess

from google_translate import GoogleTranslateSpider

process = CrawlerProcess({
    'LOG_LEVEL': 'WARNING'
})
process.crawl(GoogleTranslateSpider)
process.start()
