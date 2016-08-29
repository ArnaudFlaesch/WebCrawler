# WebCrawler

Codacy (Code Quality / Coverage)

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/0b17840fc7424e8f931ca326d887cddb)](https://www.codacy.com/app/arnaudflaesch/WebCrawler?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ArnaudFlaesch/WebCrawler&amp;utm_campaign=Badge_Grade) [![Codacy Badge](https://api.codacy.com/project/badge/Coverage/0b17840fc7424e8f931ca326d887cddb)](https://www.codacy.com/app/arnaudflaesch/WebCrawler?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ArnaudFlaesch/WebCrawler&amp;utm_campaign=Badge_Coverage)

Travis CI (Continuous Integration)

[![Build Status](https://travis-ci.org/ArnaudFlaesch/WebCrawler.svg?branch=master)](https://travis-ci.org/ArnaudFlaesch/WebCrawler)

Coveralls (Coverage)

[![Coverage Status](https://coveralls.io/repos/github/ArnaudFlaesch/WebCrawler/badge.svg?branch=master)](https://coveralls.io/github/ArnaudFlaesch/WebCrawler?branch=master)

Scrutinizer (Code Quality / Continuous Integration / Coverage)

[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/ArnaudFlaesch/WebCrawler/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/ArnaudFlaesch/WebCrawler/?branch=master) [![Build Status](https://scrutinizer-ci.com/g/ArnaudFlaesch/WebCrawler/badges/build.png?b=master)](https://scrutinizer-ci.com/g/ArnaudFlaesch/WebCrawler/build-status/master) [![Code Coverage](https://scrutinizer-ci.com/g/ArnaudFlaesch/WebCrawler/badges/coverage.png?b=master)](https://scrutinizer-ci.com/g/ArnaudFlaesch/WebCrawler/?branch=master)

Landscape (Code Quality)

[![Code Health](https://landscape.io/github/ArnaudFlaesch/WebCrawler/master/landscape.svg?style=flat)](https://landscape.io/github/ArnaudFlaesch/WebCrawler/master)

Ce fichier décrit les différentes étapes nécessaires pour faire marcher le Crawler et le
fonctionnement de ce dernier, veuillez le lire avec précaution.

Le programme est un 'Crawler' destiné à récupérer le titre, la description, les mots-clés
et les liens contenus dans une page Web à partir de son URL puis à parcourir
ces derniers suivant un nombre de fois spécifié (ou par défaut égal à 2) par l'utilisateur.
Les données récupérées seront stockées dans un fichier au format JSON (un fichier par lien).

I) PRÉ-REQUIS

Ce programme est compatible avec Windows et la distribution de Linux Debian 7.

Il faut donc avoir installé :

- Python 3
- Le gestionnaire de paquet PIP (avec la commande apt-get install python-pip sous Debian)
- Les bibliothèques BeautifulSoup4 et Requests avec la commande pip install beautifulsoup4 requests depuis un terminal

Vous pourrez ensuite lancer le programme en tapant la commande crawler.py (précédé de "./" sous Debian) [--option1 --option2 ...etc] [ADRESSE_DU_SITE_WEB].
L'adresse du site web est obligatoire pour permettre au script de s'exécuter.

II) OPTIONS DU PROGRAMME

Le script peut prendre jusqu'à trois options donc les détails sont décrits ci-dessous.

1) L'option --depth

Cette option définie le nombre de fois où le programme doit parcourir les pages Web.
Si la valeur de 'depth' vaut 0, seule l'URL de départ sera parcourue.
Si la valeur de 'depth' vaut 1, l'URL de départ et les liens qu'elle contient seront parcourus.
Si la valeur de 'depth' vaut 2, l'URL de départ, ses liens et les liens contenus dans ses liens seront parcourus,etc.

Par défaut cette option est égale à 2.

2) L'option --output

'Output' désigne le dossier dans lequel seront stockés les fichiers JSON contenant les informations récupérées à partir des pages Web.
Si le dossier spécifié n'existe pas, il sera créé.
Par défaut cette option stocke les fichiers dans un dossier 'results'.