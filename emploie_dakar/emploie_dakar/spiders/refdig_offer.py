import scrapy
from emploie_dakar.spiders.data_offer import DataOfferSpider


class RefdigOfferSpider(DataOfferSpider):
    name = "refdig_offer"
    referenciel = "Referent Digital"
    url = "https://www.emploisenegal.com/recherche-jobs-senegal/?f%5B0%5D=im_field_offre_metiers%3A29&f%5B1%5D=im_field_offre_metiers%3A33&f%5B2%5D=im_field_offre_metiers%3A38&f%5B3%5D=im_field_offre_metiers%3A39&f%5B4%5D=im_field_offre_metiers%3A32"

