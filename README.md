# FlaskApi

### Introduction

Le but de ce projet est de créer une api permettant de récupérer des données sur la concentration des polluants et les informations météorologiques pour prédire le nombre d'entrée à l'hopital dans les jours a venir. Le projet se fera avec les données du CHU HENRI MONDOR avec qui nous avons un contact.

### Retrospective

Lors ce projet, on appris plusieurs chose:

D'une part qu'il était important d'encapsuler son programme pour éviter d'éventuelle conflit entre notre programme et certains programmes ayant une fonctions simmilaire qui ferrai planté l'application. Cette condition est d'autant plus importantes si l'on veut que son application soit utilisable sur n'importe quel machine.

D'autre part, le choix de la technologie est importante. Une recherche préalable sur les compatibilités entre différentes technologies est utile afin d'éviter de refaire le projet à cause d'une incompatibilité au sein même de l'application entre celles-ci.

Nous avons décidé que pour ce projet nous allions aurions besoin de faire 2 choses:

- créer plusieurs modèle de machine learning pour faire des prédictions respectivement pour les jours J, J+1, ..., J+n.

- créer une api qui utilisera ces modèles de machine learning.

Il est donc nécessaire de mettre à jour une base de données pour que les modèle de machine learning puisse prédire tous les jours le nombre d'entrée pour les jours futurs.

Après avoir fait des recherches sur différents sites météorologiques et sur la mesure de polluants, nous avons décidé d'utiliser du webscapping pour récupérer ces données plutot que de fabriquer un capteur.

### Technologie

Gestionnaire espace:
- Docker
- VMware Player

Buffer
- kafka
- rabbitMQ

API
- flask
- fastapi

Database
- mogodb
- mysql
- webscrapping
- mongoose

WebScrapping
- beautifullsoup
- selenium
