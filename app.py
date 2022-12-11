import streamlit as st
import requests


st.title('Recommandation des articles pour un utilisateur')

id = st.number_input('Entrez l\'id de l\'utilisateur:', 0, 322896)

if id:
    url = 'https://p9recommender.azurewebsites.net/api/hello?userid=' + str(id)
    try:
        response = requests.get(url).json()
    except Exception as e:
        st.error(e)
    st.info("Les résultats sont classés par ordre de pertinence.")
    st.write('Voici les articles recommandés pour l\'utilisateur ' + str(id) + ' :')
    st.write(response)