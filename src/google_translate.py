import json
import re

import scrapy

def fix_json(str_json):
    str_json = re.sub(',+', ',', str_json)
    return re.sub('\[,', '[0,', str_json)

class Translation(scrapy.Item):
    body = scrapy.Field()

class GoogleTranslateSpider(scrapy.Spider):
    name = 'Google Translate Spider'
    start_urls = ['https://translate.google.com/translate_a/single?client=t&sl=en&tl=lt&hl=en&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&otf=2&ssel=0&tsel=0&kc=4&tk=820370.698708&q=cognition']

    def parse(self, response):
        resp_body = response.body_as_unicode()
        resp_body = fix_json(resp_body)
        resp = json.loads(resp_body)

        translations = resp[1][0][2]
        words = [tr[0] for tr in translations]
        for w in words:
            yield Translation(body=w)
