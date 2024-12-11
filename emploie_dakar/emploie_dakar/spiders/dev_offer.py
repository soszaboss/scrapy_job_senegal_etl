import scrapy
from emploie_dakar.spiders.data_offer import DataOfferSpider

class DevOfferSpider(DataOfferSpider):
    name = "dev_offer"
    url = "https://www.emploisenegal.com/recherche-jobs-senegal/developer?f%5B0%5D=im_field_offre_metiers%3A31"
    referenciel = "Dev Web/Mobile"

