# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import bs4


from bs4 import BeautifulSoup

def extraire_texte(html):
    """
    Fonction pour extraire le texte d'un bloc HTML en utilisant BeautifulSoup.

    Args:
    html (str): Une chaîne contenant le code HTML.

    Returns:
    str: Le texte brut extrait du HTML.
    """
    # Créer un objet BeautifulSoup à partir du HTML
    soup = BeautifulSoup(html, 'html.parser')
    
    # Extraire le texte brut
    texte = soup.get_text()
    
    return texte


class EmploieDakarPipeline:
    # def __init__(self):
    #     self.intitule_offre = set()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter.get("intitule_offre"):
            # if adapter["intitule_offre"] in self.intitule_offre:
            #     raise DropItem(f"intitule_offre existe déjà: {adapter["intitule_offre"]}")
            # else:
            adapter["intitule_offre"] = adapter["intitule_offre"].strip()
                # self.ids_seen.add(adapter["intitule_offre"])
        
        if adapter.get("competences"):
            adapter["competences"] = adapter["competences"].strip()
        if adapter.get('region'):
            adapter["region"] = adapter["region"].strip()
        if adapter.get('type_offre'):
            adapter["type_offre"] = adapter["type_offre"].strip()
        if adapter.get('date_publication'):
            adapter["date_publication"] = adapter["date_publication"].strip()
        if adapter.get('detail_offre'):
            adapter["detail_offre"] = extraire_texte(adapter["detail_offre"]).strip()
        if adapter.get('referenciel'):
            adapter["referenciel"] = adapter["referenciel"].strip()
        if adapter.get('entreprise'):
            adapter["entreprise"] = adapter["entreprise"].strip()
        if adapter.get('email_rh'):
            adapter["email_rh"] = adapter["email_rh"].strip()
        if adapter.get('url_offre'):
            adapter["url_offre"] = adapter["url_offre"].strip()
        

        return item
