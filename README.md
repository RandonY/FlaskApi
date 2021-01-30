# FlaskApi

### Introduction

Le but de ce projet est de créer une api permettant de récupérer des données sur la concentration des polluants et les informations météorologiques pour prédire le nombre d'entrée à l'hopital dans les jours a venir. Le projet se fera avec les données du CHU HENRI MONDOR avec qui nous avons un contact.

### Retrospective

Lors ce projet, on appris plusieurs choses:

D'une part qu'il était important d'encapsuler son code pour éviter d'éventuel conflit avec certains programmes ayant une fonction simmilaire qui ferai planter l'application. Cette condition est d'autant plus importantes si l'on veut que son application soit utilisable sur n'importe quel machine.

D'autre part, le choix de la technologie est importante. Une recherche préalable sur les compatibilités entre différentes technologies est utile afin d'éviter d'avoir à refaire le projet à cause d'une incompatibilité au sein même de l'application.

Nous avons décidé que pour ce projet nous aurions besoin de faire 2 choses:

- créer plusieurs modèles de machine learning pour faire des prédictions respectivements pour les jours J, J+1, ..., J+n.

- créer une api qui utilisera ces modèles de machine learning.

Il est donc nécessaire de mettre à jour une base de données pour que les modèle de machine learning puisse prédire tous les jours le nombre d'entrée pour les jours futurs.

Après avoir fait des recherches sur différents sites météorologiques et sur la mesure de polluants, nous avons décidé d'utiliser du web scaping pour récupérer ces données plutot que de fabriquer un capteur.

### Technologie

#### Gestion espace disque

Tout d'abord nous avons décidé d'utiliser docker plutot qu'une VM pour encapsuler notre projet, d'une part parce que

Gestionnaire espace:
- Docker
- VMware Player

#### Langage de programmation

Langage programmation:
- Python
- Java script

#### API

API
- flask
- fastapi

#### Base de données

Database
- mogodb
- mysql
- webscrapping
- mongoose

#### Web scraping

WebScrapping
- beautifullsoup
- selenium

Buffer
- kafka
- rabbitMQ
