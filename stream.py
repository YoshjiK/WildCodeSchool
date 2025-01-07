import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

# Nos données utilisateurs doivent respecter ce format
lesDonneesDesComptes = {
    "usernames": {
        "utilisateur": {
            "name": "utilisateur",
            "password": "utilisateurMDP",
            "email": "utilisateur@gmail.com",
            "failed_login_attemps": 0,  # Sera géré automatiquement
            "logged_in": False,  # Sera géré automatiquement
            "role": "utilisateur",
        },
        "root": {
            "name": "root",
            "password": "rootMDP",
            "email": "admin@gmail.com",
            "failed_login_attemps": 0,  # Sera géré automatiquement
            "logged_in": False,  # Sera géré automatiquement
            "role": "administrateur",
        },
    }
}

# Initialisation de l'authentification
authenticator = Authenticate(
    lesDonneesDesComptes,  # Les données des comptes
    "cookie_name",  # Le nom du cookie
    "cookie_key",  # La clé du cookie
    30,  # Durée en jours
)

# Login utilisateur
authenticator.login()

# Gestion de l'état de connexion
if st.session_state.get("authentication_status"):  # Utilisateur connecté
    authenticator.logout("Déconnexion", "sidebar")

    # Menu de navigation
    with st.sidebar:  # Place le menu dans la barre latérale
        menu = option_menu(
            menu_title="Navigation",  # Titre du menu
            options=["Accueil", "Les photo de mes chameaux"],  # Options du menu
            default_index=0,  # Option par défaut sélectionnée
        )

    # Contenu dynamique en fonction de la sélection
    if menu == "Accueil":
        st.title("Page Accueil")
        st.write("Bienvenue sur la page d'accueil.")
    elif menu == "Les photo de mes chameaux":
        st.title("Les photos de mes chameaux")

        # Charger trois images locales ou via URL
        image1 = "https://www.zoologiste.com/images/medium/chameau-tete.jpg"
        image2 = "https://ici.exploratv.ca/upload/site/post/picture/1921/652fe939050ac.1712152059.jpg"
        image3 = "https://www.radiofrance.fr/s3/cruiser-production-eu3/2024/04/9963517f-87ac-4354-997d-b9af69b71952/640x340_sc_chameau2.jpg"

        # Créer des colonnes pour les images
        col1, col2, col3 = st.columns(3)

        # Afficher les images dans chaque colonne
        with col1:
            st.image(image1, caption="Chameau 1", use_column_width=True)

        with col2:
            st.image(image2, caption="Chameau 2", use_column_width=True)

        with col3:
            st.image(image3, caption="Chameau 3", use_column_width=True)

elif st.session_state.get("authentication_status") is False:  # Connexion échouée
    st.error("Le nom d'utilisateur ou le mot de passe est incorrect.")
elif st.session_state.get("authentication_status") is None:  # Champs vides
    st.warning("Veuillez entrer un nom d'utilisateur et un mot de passe.")
