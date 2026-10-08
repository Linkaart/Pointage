# 🕒 Pointage

Application web de pointage horaire des salariés, développée en Python avec **Streamlit**.

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=white)

## Fonctionnalités

- Saisie du nom du salarié
- **Pointage de l'arrivée** : enregistre la date et l'heure
- **Pointage du départ** : complète la ligne d'arrivée du jour, avec message d'erreur si aucune arrivée n'a été pointée
- **Historique** de tous les pointages affiché sous forme de tableau
- Données persistées dans un fichier `pointage.csv` (créé automatiquement)

## Stack technique

- **Python** et **Streamlit** pour l'interface
- **pandas** pour la lecture, la mise à jour et l'écriture du CSV

## Lancer le projet

```bash
git clone https://github.com/Linkaart/Pointage.git
cd Pointage
pip install -r requirements.txt
streamlit run point.py
```

L'application s'ouvre sur `http://localhost:8501`.

Un fichier `.devcontainer` est fourni pour lancer le projet dans GitHub Codespaces.

## Pistes d'amélioration

- Authentification des salariés et espace administrateur
- Export Excel et filtres par période
- Calcul automatique des heures travaillées
