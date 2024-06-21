

## Introduction

Ce projet consiste en une application web développée en Python avec Flask, permettant de chiffrer et déchiffrer des courriels en utilisant l'algorithme de chiffrement AES en mode CBC (Cipher Block Chaining). L'application offre une interface utilisateur simple et intuitive pour saisir, chiffrer, déchiffrer et copier des messages.

## Fonctionnalités

- **Chiffrement des messages** : Utilisation de l'algorithme AES en mode CBC pour garantir la sécurité des messages.
- **Déchiffrement des messages** : Possibilité de déchiffrer les messages chiffrés avec la clé appropriée.
- **Gestion sécurisée des clés** : Génération, stockage temporaire et suppression des clés de chiffrement pour chaque session.
- **Interface utilisateur intuitive** : Pages HTML avec formulaires pour saisir et afficher les messages chiffrés/déchiffrés.
- **Navigation facilitée** : Menu de navigation pour passer entre les pages de chiffrement et de déchiffrement.

## Prérequis

- Python 3.x
- Flask
- PyCryptodome

## Installation

1. Clonez le dépôt :

    ```bash
    git clone https://github.com/votre-utilisateur/email-encryption-app.git
    cd email-encryption-app
    ```

2. Créez et activez un environnement virtuel :

    ```bash
    python -m venv env
    source env/bin/activate  # Sur Windows: env\Scripts\activate
    ```

3. Installez les dépendances :

    ```bash
    pip install -r requirements.txt
    ```

## Utilisation

1. Lancez l'application :

    ```bash
    python app.py
    ```

2. Ouvrez votre navigateur et accédez à l'adresse suivante :

    ```
    http://127.0.0.1:5000
    ```

3. Utilisez le menu pour naviguer entre les pages de chiffrement et de déchiffrement :

    - **Page de Chiffrement** : Saisissez le message à chiffrer et cliquez sur "Chiffrer". Copiez le message chiffré et l'identifiant de clé.
    - **Page de Déchiffrement** : Saisissez le message chiffré et l'identifiant de clé, puis cliquez sur "Déchiffrer". Copiez le message déchiffré.

## Arborescence du Projet

```
email-encryption-app/
│
├── app.py
├── key_manager.py
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── encrypt.html
│   ├── decrypt.html
├── static/
│   ├── style.css
├── requirements.txt
├── README.md
```

- `app.py` : Script principal de l'application Flask.
- `key_manager.py` : Gestion des clés de chiffrement (génération, stockage, récupération, suppression).
- `templates/` : Dossier contenant les fichiers HTML pour l'interface utilisateur.
- `static/` : Dossier contenant les fichiers CSS pour le style de l'application.
- `requirements.txt` : Liste des dépendances Python nécessaires au projet.
- `README.md` : Ce fichier.

## Captures d'Écran

### Page d'Accueil

![Page d'Accueil](demo_screenshots/home_page.png)

### Page de Chiffrement

![Page de Chiffrement](demo_screenshots/encryption_page.png)

### Page de Déchiffrement

![Page de Déchiffrement](demo_screenshots/decryption_page.png)

### Copie du Résultat

![Copie du Résultat](demo_screenshots/copy_result.png)

## Auteurs

- SANOGO Sy Rachid Guy (syrachidsanogo78@gmail.com)

## Licence
open source


Merci d'utiliser notre application de chiffrement de mails. Pour toute question ou suggestion, n'hésitez pas à nous contacter.
