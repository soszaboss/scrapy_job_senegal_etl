import scrapy
from scraperapi_sdk import ScraperAPIClient
from emploie_dakar.items import EmploieDakarItem


APIKEY = ''

def get_proxy_url(url:str):
    return f'http://api.scraperapi.com/?api_key={APIKEY}&url={url}'

class DataOfferSpider(scrapy.Spider):
    name = "data_offer"
    allowed_domains = ["www.emploisenegal.com", "api.scraperapi.com"]
    url = "https://www.emploisenegal.com/recherche-jobs-senegal/data?f%5B0%5D=im_field_offre_metiers%3A31"
    referenciel = "Data"
    def start_requests(self):
        print("start_requests")
        # yield scrapy.Request(client.scrapyGet(url=url), self.parse)
        yield scrapy.Request(get_proxy_url(self.url), self.parse)

    def parse(self, response):
        relative_links = response.css("div.card-job-detail h3 a::attr(href)").getall()
        print(f'relative_links: {relative_links}')
        for i in range(len(relative_links)):
            relative_links[i] = f'https://www.emploisenegal.com{relative_links[i]}'

        # print(relative_links)
        requests = [scrapy.Request(get_proxy_url(link), callback=self.parse_offer) for link in relative_links]

        # Itérez sur les objets Request
        for request in requests:
            yield request

        # pager-item
        next_page = response.css("li.pager-item.active.pagination-numbers a::attr(href)").get()
        if next_page is not None:
            yield response.follow(f'http://api.scraperapi.com/?api_key={APIKEY}&url=www.emploisenegal.com{next_page}',
                                   self.parse)
    
    def parse_offer(self, response):
        print("Page Element")
        items = EmploieDakarItem()
        qualifications_div = response.css('div.job-qualifications')
        items['intitule_offre'] = response.css('div.container h1.text-center::text').get()
        items['competences'] = ' '.join(qualifications_div.css('ul li::text').getall())
        items['region'] = response.css('li.withicon.location-dot span::text').get()
        items['type_offre'] = response.css('li.withicon.file-signature span::text').get()
        items['date_publication'] = response.css('div.page-application-details p::text').get()
        items['detail_offre'] = response.css('div.job-description').get()
        items['referenciel'] = self.referenciel
        items['entreprise'] = response.xpath('//*[@id="main-content"]/div[2]/div[1]/div[1]/div[1]/div[2]/div/div/ul/li[1]/h3/a/text()').get()
        items['email_rh'] = None
        items['url_offre'] = response.url
        yield items

