import streamlit as st
import pandas as pd
from datetime import datetime

# Chargement ou création du fichier CSV pour enregistrer les données
DATA_FILE = "pointage.csv"

def load_data():
    try:
        return pd.read_csv(DATA_FILE)
    except FileNotFoundError:
        return pd.DataFrame(columns=["Nom", "Date", "Heure d'arrivée", "Heure de départ"])

def save_data(data):
    data.to_csv(DATA_FILE, index=False)

# Chargement des données existantes
data = load_data()

# Interface Streamlit
st.title("Système de Pointage Horaire pour Salariés ")

# Saisie du nom de l'employé
nom = st.text_input("Entrez votre nom complet :")

if nom:
    # Afficher les options de pointage
    action = st.radio(
        "Choisissez une action :",
        ("Pointer l'arrivée", "Pointer le départ")
    )

    if st.button("Enregistrer le pointage"):
        now = datetime.now()
        date = now.strftime("%Y-%m-%d")
        heure = now.strftime("%H:%M:%S")

        if action == "Pointer l'arrivée":
            # Enregistrer l'heure d'arrivée
            new_data = pd.DataFrame({"Nom": [nom], "Date": [date], "Heure d'arrivée": [heure], "Heure de départ": [None]})
            data = pd.concat([data, new_data], ignore_index=True)
            st.success(f"Pointage d'arrivée enregistré pour {nom} à {heure}.")
        elif action == "Pointer le départ":
            # Mettre à jour l'heure de départ
            if not data[(data["Nom"] == nom) & (data["Date"] == date) & (data["Heure de départ"].isna())].empty:
                data.loc[(data["Nom"] == nom) & (data["Date"] == date) & (data["Heure de départ"].isna()), "Heure de départ"] = heure
                st.success(f"Pointage de départ enregistré pour {nom} à {heure}.")
            else:
                st.error("Aucun pointage d'arrivée trouvé pour aujourd'hui.")

        # Sauvegarder les données mises à jour
        save_data(data)

# Afficher les données enregistrées
st.subheader("Historique des pointages")
st.dataframe(data)

