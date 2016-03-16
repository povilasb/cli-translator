import json

import scrapy
from scrapy.http.headers import Headers

RENDER_HTML_URL = 'http://127.0.0.1:8050/render.html'

class GoogleTranslateSpider(scrapy.Spider):
    name = 'Google Translate Spider'
    start_urls = ['https://translate.google.com/#en/lt/']

    def __init__(self, translate_this, *args, **kwargs):
        super(GoogleTranslateSpider, self).__init__(*args, **kwargs)

        self.translate_this = translate_this
        self.start_urls[0] += translate_this

    def start_requests(self):
        for url in self.start_urls:
            body = json.dumps({'url': url, 'wait': 0.5})
            headers = Headers({'Content-Type': 'application/json'})
            yield scrapy.Request(RENDER_HTML_URL, self.parse, method='POST',
                                 body=body, headers=headers)

    def parse(self, response):
        translations = response.css('.gt-baf-word-clickable::text').extract()
        print('"%s" to LT:' % self.translate_this)
        for t in translations:
            print('\t%s' % t)
