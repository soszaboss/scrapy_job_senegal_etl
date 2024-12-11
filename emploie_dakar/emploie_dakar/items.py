# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EmploieDakarItem(scrapy.Item):
    # define the fields for your item here like:
    intitule_offre = scrapy.Field(serialize=str)
    competences = scrapy.Field(serialize=str)
    region = scrapy.Field(serialize=str)
    type_offre = scrapy.Field(serialize=str)
    date_publication = scrapy.Field()
    detail_offre = scrapy.Field(serialize=str)
    referenciel = scrapy.Field(serialize=str)
    entreprise = scrapy.Field(serialize=str)
    email_rh = scrapy.Field()
    url_offre = scrapy.Field()