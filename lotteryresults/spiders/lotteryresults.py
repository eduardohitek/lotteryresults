# -*- coding: utf-8 -*-

from scrapy.spider import Spider
from scrapy.selector import Selector


class LotteryResults(Spider):
    name = "lotteryresults"
    start_urls = [
        "http://loterias.caixa.gov.br/wps/portal/loterias/landing/megasena",
        "http://loterias.caixa.gov.br/wps/portal/loterias/landing/lotofacil",
        "http://loterias.caixa.gov.br/wps/portal/loterias/landing/lotomania",
        "http://loterias.caixa.gov.br/wps/portal/loterias/landing/quina",
    ]

    def parse(self, response):
        urls = {u"Lotomania": '//*[@id="resultados"]/div[2]/div/div/table/tr',
                     u"Lotofácil": '//*[@id="resultados"]/div[2]/div/div/table/tbody/tr',
                     "title": '//*[@id="layoutContainers"]/div/div[2]/div[1]/div[1]/section/div[2]/div[2]/h1/text()',
                     "draw_date": '//*[@id="resultados"]/div[1]/div/h2/span/text()',
                     "Mega-Sena": '//*[@id="resultados"]/div[2]/div/div/ul/li',
                     "Quina": '//*[@id="resultados"]/div[2]/div/div/ul/li', }

        sel = Selector(response)
        title = sel.xpath(urls["title"]).extract()
        draw_date = sel.xpath(urls["draw_date"]).extract()  
        print title[0]
        print draw_date[0]
        items = []

        if title[0] in ("Mega-Sena", "Quina"):
            numbers = sel.xpath(urls[title[0]])
            for number in numbers:
                number_text = number.xpath('text()').extract()
                print number_text[0],
        else:
            table = sel.xpath(urls[title[0]])
            for row in table:
                for value in row.xpath('td'):
                    value_text = value.xpath('text()').extract()
                    print value_text[0],
        print '\n' * 2
        return items
