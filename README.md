# Projet de Scraping d'Offres d'Emploi

## Description du projet
Ce projet vise à scraper des sites d'offres d'emploi comme **LinkedIn**, **SenegalEmploi**, et **DakarEmploi** afin d'extraire les données liées aux offres d'emploi disponibles. Les données extraites peuvent ensuite être utilisées pour des analyses, des visualisations ou intégrées dans une base de données.

Nous utilisons **Python 3.12** et la bibliothèque **Scrapy** combinée à **Playwright** pour gérer les pages dynamiques.

---

## Fonctionnalités principales
- Extraction d'annonces d'emploi depuis des sites web dynamiques.
- Intégration de **Scrapy** avec **Playwright** pour une gestion optimale des pages interactives (JavaScript).
- Gestion facile des dépendances via un fichier `requirements.txt`.

---

## Pré-requis
Avant de commencer, veuillez vérifier les pré-requis suivants :

### Versions minimales requises
- **Python** >= 3.8 (Recommandé : 3.12)
- **Scrapy** >= 2.0 (Attention : évitez la version 2.4.0)
- **Playwright** >= 1.15

---

## Installation

### 1. Cloner le projet
Commencez par cloner le dépôt du projet :
```bash
git clone <url_du_depot>
cd <nom_du_dossier>
```

### 2. Installer les dépendances
Utilisez `pip` pour installer toutes les dépendances nécessaires :
```bash
pip install -r requirements.txt
```

### 3. Installer les navigateurs Playwright
Playwright nécessite l'installation de navigateurs pour fonctionner. Exécutez la commande suivante pour les installer :
```bash
playwright install
```

Si vous souhaitez installer uniquement un sous-ensemble de navigateurs (par exemple, Firefox et Chromium) :
```bash
playwright install firefox chromium
```

---

## Configuration de Scrapy avec Playwright

### Modifier les gestionnaires de téléchargement
Ajoutez la configuration suivante dans le fichier `settings.py` pour activer le gestionnaire Playwright :
```python
DOWNLOAD_HANDLERS = {
    "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
    "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
}
```

### Activer le réacteur Twisted basé sur asyncio
Ajoutez également cette ligne pour utiliser le réacteur basé sur asyncio dans `settings.py` :
```python
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
```

> **Note** : Ce réacteur est activé par défaut dans les nouveaux projets Scrapy depuis la version 2.7.

---

## Lancer le projet
Une fois la configuration terminée, vous pouvez exécuter le projet Scrapy avec la commande suivante :
```bash
scrapy crawl <nom_du_spider>
```

---

## Ressources supplémentaires
- [Documentation officielle de Scrapy](https://docs.scrapy.org/)
- [Documentation de Playwright](https://playwright.dev/python/)
- [scrapy-playwright sur PyPI](https://pypi.org/project/scrapy-playwright/)

---
