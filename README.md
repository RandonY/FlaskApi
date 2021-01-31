# FlaskApi

### Introduction

Le but de ce projet est de trouver une corrélation entre la concentration des polluants / les informations météorologiques et le nombre d'entrées à l'hopital.
Nous avons donc choisi de créer une API qui servira d'IHM pour récupérer les résultats obtenu avec du machine learning et afficher des statistiques sur l'évolution des données concernant les polluants et les informations météorologiques.
Le projet se fera avec les données du CHU HENRI MONDOR chez qui nous avons un contact.

### Retrospective

Lors ce projet, nous avons appris plusieurs choses:

D'une part qu'il était important d'encapsuler son code pour éviter d'éventuels conflits avec certains programmes ayant une fonction simmilaire qui ferai planter l'application. Cette condition est d'autant plus importante si l'on veut que son application soit utilisable sur n'importe quel machine.

D'autre part, le choix de la technologie est importante. Une recherche préalable sur les compatibilités entre différentes technologies est utile afin d'éviter d'avoir à refaire le projet à cause d'une incompatibilité au sein même de l'application.

Nous avons décidé que pour ce projet nous aurions besoin de faire 2 choses:

- créer et entrainer plusieurs modèles de machine learning pour faire des prédictions respectivement pour les jours J, J+1, ..., J+n à partir des données relevées les jours J-1, J-2, ..., J-n'.

- créer une api qui affichera les résultats de ces modèles de machine learning.

Il est donc nécessaire de mettre à jour une base de données pour que les modèles de machine learning puissent prédire tous les jours le nombre d'entrée pour les jours futurs.

Après avoir fait des recherches sur différents sites météorologiques et sur la mesure de polluants, nous avons décidé d'utiliser du web scraping pour récupérer ces données plutot que de fabriquer un capteur.

### Technologie

#### Gestion espace disque

|Technologie|Description|
|----|-----|
|Docker|Docker est un outil qui peut empaqueter une application et ses dépendances dans un conteneur isolé, qui pourra être exécuté sur n'importe quel serveur.|
|VMware Workstation Player|VMware Workstation Player est une application d’hyperviseur des postes de travail, avec des fonctionnalités de virtualisation locale, disponible gratuitement pour une utilisation à titre personnel. Une licence commerciale peut être appliquée pour que Workstation Player puisse exécuter les machines virtuelles restreintes créées par VMware Workstation Pro et Fusion Pro.|
|Oracle VirtualBox|Oracle VM VirtualBox, le logiciel de virtualisation multiplateforme à code source ouvert le plus populaire au monde, permet aux développeurs de fournir du code plus rapidement en exécutant plusieurs systèmes d’exploitation sur un seul terminal.|

##### Choix

Tout d'abord nous avons décidé d'utiliser Docker plutot qu'un logiciel de gestion de VM pour encapsuler notre projet.

D'une part parce que la VM fait que l'application ne marche que sur les machines sur lesquels ont a préalablement installé un logiciel (VMware player, Oracle VirtualBox, etc ...) qui peut créer une VM à partir d'une image (par exemple au format .iso).

Tandis que Docker permet de créer son conteneur et d'y installer les prérequis nécessaire à la bonne éxecution du code, généralement via la commande "sudo docker-compose up" si le fichier docker compose a été fait dans le projet, sous condition que Docker soit installé sur la machine.


#### Langage de programmation

##### Python

Python est un langage de programmation interprété, multi- paradigme et multiplateformes.

Il favorise la programmation impérative structurée, fonctionnelle et orientée objet.

L'un de ces avantages est qu'il possède une grande communauté très active et des codes disponible en open source ce qui permet d'avoir accès à beaucoup de ressource de manière totalement gratuite.

##### Javascript

JavaScript est un langage de programmation de scripts principalement employé dans les pages web interactives et à ce titre est une partie essentielle des applications web.

Avec les technologies HTML et CSS, JavaScript est parfois considéré comme l'une des technologies cœur du World Wide Web.

##### C++

C++ est un langage de programmation compilé permettant la programmation sous de multiples paradigmes, dont la programmation procédurale, la programmation orientée objet et la programmation générique.

Ses bonnes performances, et sa compatibilité avec le C en font un des langages de programmation les plus utilisés dans les applications où la performance est critique.

##### Java

Java est une technique informatique développée initialement par Sun Microsystems puis acquise par Oracle suite au rachat de l'entreprise.

Défini à l'origine comme un langage de programmation, Java a évolué pour devenir un ensemble cohérent d'éléments techniques et non techniques.

Ce langage est utilisé dans de nombreux logiciels différents et présent partout dans notre vie.

##### Choix

Au cours de nos études nous avons été amené la plupart du temps à coder en python.

Il nous est donc plus aisé de coder dans ce langage de programmation que d'en d'autres comme Java, Javascript, C++.

De plus, nous avons déjà utilisé certains outils qui nous serons utiles pour le projet tel que sklearn (machine learning) ou selenium(web scraping).

Nous avons donc choisi d'utiliser python comme langage de programmation.


#### API

##### Flask

Flask est un micro framework open-source de développement web en Python.

Il est classé comme microframework car il est très léger.

Flask a pour objectif de garder un noyau simple mais extensible.

Il n'intègre pas de système d'authentification, pas de couche d'abstraction de base de données, ni d'outil de validation de formulaires.

Flask est aussi un outil très utilisé en entreprise, ce qui renferce l'intêret de son apprentissage

##### Fastapi

FastAPI est un framework Python avec de hautes performances, facile à apprendre, rapide à coder et facilement prêt pour la production.

Ce framework propose aussi une documentation automatique avec Swagger UI.

##### Choix

Parmis les membres du projet, la plupart étaient familier avec Flask c'est pourquoi nous avons choisi ce framework pour développer l'api pour ce projet.

#### Base de données

##### Mysql

MySQL est un système de gestion de bases de données relationnelles (SGBDR). Il est distribué sous une double licence GPL et propriétaire.

Il fait partie des logiciels de gestion de base de données les plus utilisés au monde3, autant par le grand public (applications web principalement) que par des professionnels, en concurrence avec Oracle, PostgreSQL et Microsoft SQL Server.

C'est un outil facile à utiliser et à l'avantage de se coder avec des requetes SQL.

##### Mongodb

MongoDB est un système de gestion de base de données orienté documents, répartissable sur un nombre quelconque d'ordinateurs et ne nécessitant pas de schéma prédéfini des données.

Il est écrit en C++. 

Le serveur et les outils sont distribués sous licence SSPL, les pilotes sous licence Apache et la documentation sous licence Creative Commons.

Il utilise des requetes NoSQL.

##### Choix

Les informations que nous allons stocker ne sont pas relationnelles, nous voudriions donc les stocker sous forme de document.

C'est pourquoi nous avons décidé d'utiliser MongoDB qui palie ce besoin.


#### Web scraping

##### BeautifulSoup

Beautiful Soup est une bibliothèque Python d'analyse syntaxique de documents HTML et XML créée par Leonard Richardson.

Elle produit un arbre syntaxique qui peut être utilisé pour chercher des éléments ou les modifier. Lorsque le document HTML ou XML est mal formé (par exemple s'il manque des balises fermantes), Beautiful Soup propose une approche à base d'heuristiques afin de reconstituer l'arbre syntaxique sans générer d'erreurs. 

Cette approche est aussi utilisée par les navigateurs web modernes.

Cette bibliothèque est surtout utile pour scrapper des élements statiques.

##### Selenium

Selenium est un framework de test informatique développé en Java.

Il permet d'interagir avec différents navigateurs web de même que le ferait un utilisateur de l'application. Il entre ainsi dans la catégorie des outils de test dynamique (à l'inverse des tests statiques qui ne nécessitent pas l'exécution du logiciel) facilitant le test fonctionnel. 

Il utilise des drivers afin de récuperer l'information dynamiquement.

##### Scrappy

Scrapy est un framework open-source permettant la création de robots d'indexation. Développé en Python, il dispose d'une forte communauté, offrant de nombreux modules supplémentaires.

L'équipe de développement publie régulièrement de nouvelles versions dans le but d'enrichir le framework en fonctionnalité.

Le framework dispose d'une communauté active, et un support commercial est effectué par plusieurs entreprises.

C'est un outil simple, rapide, robuste et open source

##### Choix

Pour ce projet, le web scraping n'a pas besoin d'être dynamique, de ce fait selenium n'est pas optimisé pour l'utilisation que l'on souhaite en faire.

Dans le cadre de nos études, nous avons déjà utilisé bfs et non scrappy.

De plus bfs est un outil dont les performances suffise pour les besoins du projet.
