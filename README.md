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

![Modèle Machine Learning](https://www.bing.com/images/search?view=detailV2&ccid=5b64FIK6&id=2C7DC7863646EFD1D8948BC9C4472C8CDCD3E740&thid=OIP.5b64FIK60Ov6i_zYVNS9KgHaEo&mediaurl=https%3a%2f%2fmk0wittysparksm75pi6.kinstacdn.com%2fwp-content%2fuploads%2f2017%2f08%2fMachine-Learning-1024x640.jpg&exph=640&expw=1024&q=image+machine+learning&simid=608003813052583360&ck=FD034DB3FF06599B82E971FF7DF93247&selectedIndex=2&FORM=IRPRST)

### Technologie

A développer

Langage programmation:
- Python
- Java script

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
