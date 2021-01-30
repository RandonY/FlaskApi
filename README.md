# FlaskApi

### Introduction

Le but de ce projet est de trouver une corrélation entre la concentration des polluants / les informations météorologiques et le nombre d'entrées à l'hopital.
Nous avons donc choisi de créer une API qui servira d'IHM (Interface Humain Machine) pour récupérer les résultats obtenus avec du machine learning et afficher des statistiques sur l'évolution des données concernant les polluants et les informations météorologiques.
Le projet se fera avec les données du CHU HENRI MONDOR chez qui nous avons un contact.

### Retrospective

Lors ce projet, on appris plusieurs choses:

D'une part qu'il était important d'encapsuler son code pour éviter d'éventuels conflits avec certains programmes ayant une fonction simmilaire qui ferai planter l'application. Cette condition est d'autant plus importante si l'on veut que son application soit utilisable sur n'importe quelle machine.

D'autre part, le choix de la technologie est importante. Une recherche préalable sur les compatibilités entre différentes technologies est utile afin d'éviter d'avoir à refaire le projet à cause d'une incompatibilité au sein même de l'application.

Nous avons décidé que pour ce projet nous aurions besoin de faire 2 choses:

- créer er entrainer plusieurs modèles de machine learning pour faire des prédictions respectivements pour les jours J, J+1, ..., J+n a a partir des données relevées les jours J-1, J-2, ..., J-n'.

- créer une api qui affichera les résultats de ces modèles de machine learning.

Il est donc nécessaire de mettre à jour une base de données pour que les modèle de machine learning puisse prédire tous les jours le nombre d'entrée pour les jours futurs.

Après avoir fait des recherches sur différents sites météorologiques et sur la mesure de polluants, nous avons décidé d'utiliser du web scaping pour récupérer ces données plutot que de fabriquer un capteur.

### Technologie


#### Gestion espace disque

##### Docker

Docker est un outil qui peut empaqueter une application et ses dépendances dans un conteneur isolé, qui pourra être exécuté sur n'importe quel serveur

##### VMware Player



##### Oracle VirtualBox

##### Choix
Tout d'abord nous avons décidé d'utiliser Docker plutot qu'une VM pour encapsuler notre projet.
D'une part parce que la VM fait que l'application ne marche que sur les machines sur lesquelles un logiciel a été préalablement installé (VMware player, Oracle VirtualBox, etc ...) qui peut créer une VM à partir d'une image (.iso, .
Tandis que Docker permet de créer son conteneur et d'y installer les prérequis nécessaires à la bonne éxecution du code, généralement via la commande "sudo docker-compose up" si le fichier docker compose a été fait dans le projet, sous condition que Docker soit installé sur la machine.


#### Langage de programmation

##### Python

##### Javascript

##### C++

##### Java

##### Choix
Au cours de nos études nous avons été amené la plupart du temps à codé en Python, il nous est donc plus facile de coder dans ce langage plutôt que d'en d'autres Java, Javascript, C++.
De plus python possède une grande communauté très active, ce qui permet d'avoir accès à plus de ressources.


#### API

##### Flask

##### Fastapi

##### Choix
Flask est un framework python. Il est assez pratique pour lancer de petites applications ou site web. C'est aussi un outil que l'on considère plus professionnel et donc peut être plus utile d'apprendre.


#### Base de données

##### Mysql

##### Mongodb

##### Choix


#### Web scraping

##### BeautifullSoup

##### Selenium

##### Scrappy

##### Choix
