#import time
import streamlit as st
#import streamlit_authenticator as stauth
#Base de donnée
import mysql.connector
from mysql.connector import Error
#password
import hashlib

st.set_page_config(page_title="Metrics", page_icon="📈", layout="wide")

#------ Login ------

# Connect to the MySQL database
try:
    connection = mysql.connector.connect(
        host='xaviermerle.fr',
        database='MSPR',
        user='root',
        password='IHVX23!'
    )
    cursor = connection.cursor()
except Error as e:
    st.error("Erreur impossible de se connecter à la base de donnée: {}".format(e))

username = st.text_input("Username")
password = st.text_input("Password", type='password')

if st.button('Submit'):
    # Hash the password
    password_hash = hashlib.sha256(password.encode()).hexdigest()

    # Check if the user is in the MySQL database
    query = "SELECT * FROM utilisateur WHERE nom_utilisateur = %s AND mot_de_passe = %s"
    cursor.execute(query, (username, password_hash))
    result = cursor.fetchone()

    if result:
        user_id, username, _ = result
        # Log the user in
        st.success('Bienvenue %s' % (username))
    else:
        st.error('nom d\'utilisateur ou mot de passe incorrect')