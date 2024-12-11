import scrapy
from emploie_dakar.spiders.data_offer import DataOfferSpider


class HackeuseOfferSpider(DataOfferSpider):
    name = "hackeuse_offer"
    url = "https://www.emploisenegal.com/recherche-jobs-senegal/?f%5B0%5D=im_field_offre_metiers%3A525&f%5B1%5D=im_field_offre_metiers%3A40"
    referenciel = "Hackeuse"
