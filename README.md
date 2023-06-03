# Programme de gestion de tournoi d'échecs
Projet n°4 - Développez un programme logiciel en Python - Auteur : Ciran GÜRBÜZ
Date : Juin 2023

Ce programme est destiné à gérer le déroulement d'un tournoi de jeu d'échecs.

Il est doté de plusieurs fonctionnalités et notamment :

-La création de joueurs & de tournois.

-La gestion du déroulé d'un tournoi.

-L'affichage de rapports divers (attention, il faut avoir généré des données au préalable en utilisant le programme).


Après avoir téléchargé le contenu du repository, veuillez l'extraire dans un dossier spécifique sur votre ordinateur. 
Ensuite, suivez ces étapes dans l'ordre afin de faire fonctionner le programme.

## 1 - Installation des logiciels requis

### 1.1 - Python

Ce programme a été développé en utilisant la version 3.11 de Python que vous pourrez retrouver sur le site officiel de Python : https://www.python.org/downloads/


### 1.2 - Création et activation de l'environnement virtuel

#### a) Ouvrir un terminal de commande et se placer dans le dossier contenant les fichiers du repository.
#### b) Créer l'environnement virtuel avec la ligne de commande suivante : 
```python -m venv "env"```
#### c) Activer l'environnement virtuel avec la ligne de commande suivante : 
```env/Scripts/activate```


### 1.3 - Installation des packages

#### a) Une fois l'environnement virtuel activé, installer les packages avec la commande suivante : 
```pip install -r requirements.txt```


## 2 - Exécution du script

#### a) Toujours dans le dossier contenant les fichiers du repository, veuillez exécuter le fichier ```main.py``` avec la commande suivante :
```python main.py```


## 3 - Notes importantes

#### a) Il est PRIMORDIAL de créer 8 joueurs au préalable avant de créer un tournoi.
#### b) Pour créer les joueurs, sélectionnez l'option [1] dans le menu principal, puis laissez-vous guider.
#### c) Une fois les 8 joueurs créés, il faut créer le tournoi.
#### d) Pour créer un tournoi, revenez dans le menu principal puis sélectionnez l'option [2], puis laissez-vous guider.
#### e) Une fois le tournoi créé, vous pourrez commencer le tournoi en sélectionnant l'option dédiée dans le menu Tournoi.


## 4 - Génération d'un rapport Flake8 - HTML

a) Dans la racine du dossier, veuillez exécuter la commande suivante dans le terminal :
```flake8 --format=html --htmldir=flake8_rapport```



Have fun & good luck !
