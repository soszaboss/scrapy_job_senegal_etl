import scrapy
from emploie_dakar.spiders.data_offer import DataOfferSpider

class AwsOfferSpider(DataOfferSpider):
    name = "aws_offer"
    url = 'https://www.emploisenegal.com/recherche-jobs-senegal/cloud?f%5B0%5D=im_field_offre_metiers%3A31'
    referenciel = 'AWS'
    
