# FlaskApi

### Introduction

Le but de ce projet est de trouver une corrélation entre la concentration des polluants / les informations météorologiques et le nombre d'entrée à l'hopital.
Nous avons donc choisi de créer une api qui servira d'IHM pour récupérer les résultats obtenu avec du machine learning et afficher des statistiques sur l'évolution des données concernant les polluants et les inforamtions météorologique.
Le projet se fera avec les données du CHU HENRI MONDOR chez qui nous avons un contact.

### Retrospective

Lors ce projet, on appris plusieurs choses:

D'une part qu'il était important d'encapsuler son code pour éviter d'éventuel conflit avec certains programmes ayant une fonction simmilaire qui ferai planter l'application. Cette condition est d'autant plus importantes si l'on veut que son application soit utilisable sur n'importe quel machine.

D'autre part, le choix de la technologie est importante. Une recherche préalable sur les compatibilités entre différentes technologies est utile afin d'éviter d'avoir à refaire le projet à cause d'une incompatibilité au sein même de l'application.

Nous avons décidé que pour ce projet nous aurions besoin de faire 2 choses:

- créer er entrainer plusieurs modèles de machine learning pour faire des prédictions respectivements pour les jours J, J+1, ..., J+n a a partir des données relevé les jours J-1, J-2, ..., J-n'.

- créer une api qui affichera les résultats de ces modèles de machine learning.

Il est donc nécessaire de mettre à jour une base de données pour que les modèle de machine learning puisse prédire tous les jours le nombre d'entrée pour les jours futurs.

Après avoir fait des recherches sur différents sites météorologiques et sur la mesure de polluants, nous avons décidé d'utiliser du web scaping pour récupérer ces données plutot que de fabriquer un capteur.

### Technologie


#### Gestion espace disque

##### Docker

##### VMware Player

##### Oracle VirtualBox

##### Choix
Tout d'abord nous avons décidé d'utiliser Docker plutot qu'une VM pour encapsuler notre projet.
D'une part parce que la VM fait que l'application ne marche que sur les machines sur lesquels ont a préalablement installé un logiciel (VMware player, Oracle VirtualBox, etc ...) qui peut créer une VM à partir d'une image (.iso, .
Tandis que Docker permet de créer son conteneur et d'y installer les prérequis nécessaire à la bonne éxecution du code, généralement via la commande "sudo docker-compose up" si le fichier docker compose a été fait dans le projet, sous condition que Docker soit installer sur la machine.


#### Langage de programmation

##### Python

##### Javascript

##### C++

##### Java

##### Choix
Au cours de nos études nous avons été amené la plupart du temps à codé en python, il nous est donc plus facile de codé dans ce langage que d'autre comme Java, Javascript, C++.
De plus python possède une grande communauté très active, ce qui permet d'avoir accès à plus de ressource.


#### API

##### Flask

##### Fastapi

##### Choix
Flask est un framework python. Il est assez pratique pour lancer de petites applications ou site web


#### Base de données

##### Mysql

##### Mongodb

##### Choix


#### Web scraping

##### BeautifullSoup

##### Selenium

##### Scrappy

##### Choix
