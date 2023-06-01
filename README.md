# Classification de texte avec Python et scikit-learn


Ce projet vise à montrer comment utiliser la bibliothèque Python scikit-learn pour la classification de texte. Nous allons entraîner un modèle de classification pour classer les commentaires Reddit en fonction de leur sujet.

# Installation
Cloner ce dépôt : 

git clone https://github.com/WISSAL-MN/Classification-de-texte-avec-Python-et-scikit-learn/

Aller dans le répertoire du projet : cd classification-texte

Installer les dépendances : pip install -r requirements.txt

# Utilisation

Télécharger le jeu de données : python download_data.py

Prétraiter les données : python preprocess_data.py

Entraîner le modèle : python train_model.py

Évaluer le modèle : python evaluate_model.py
Structure du projet

            .
            ├── data
            │   ├── raw
            │   │   └── reddit_comments.csv
            │   ├── processed
            │   │   ├── reddit_comments_cleaned.csv
            │   │   └── reddit_comments_processed.csv
            │   └── models
            │       └── model.pkl
            ├── src
            │   ├── download_data.py
            │   ├── preprocess_data.py
            │   ├── train_model.py
            │   └── evaluate_model.py
            ├── README.md
            └── requirements.txt

data/raw : Le dossier contenant les données brutes.

data/processed : Le dossier contenant les données prétraitées.

data/models : Le dossier contenant le modèle entraîné.

src/download_data.py : Le script pour télécharger les données.

src/preprocess_data.py : Le script pour prétraiter les données.

src/train_model.py : Le script pour entraîner le modèle.

src/evaluate_model.py : Le script pour évaluer le modèle.

README.md : Le fichier README pour le projet.

# requirements.txt : Le fichier contenant les dépendances du projet.
# Licence
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus d'informations.

# Auteurs

Nom de l'auteur 1  https://github.com/WISSAL-MN

Nom de l'auteur 2  https://github.com/eva-sui
______________________________________________________________________________________________________________________________________________________________
N'hésitez pas à ajouter des sections supplémentaires en fonction de votre projet, telles que des explications sur l'approche de classification utilisée, les performances du modèle, les exemples d'utilisation, etc.
