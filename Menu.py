# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 22:25:02 2026

@author: ra-el
"""

# carregando o streamlit
import streamlit as st


# configurando a página
st.set_page_config(page_title="Login", layout="centered")

USUARIOS = {
    "admin": "1234"}

# iniciando um sessão
if "logado" not in st.session_state:
    st.session_state.logado = False
    
# se já estiver logado, vai direto para relatório
if st.session_state.logado:
    st.switch_page("pages/1_Visao_Geral.py")
    
# título da página
st.title("Login")

# cria dois campos
usuario = st.text_input("Usuário")
senha = st.text_input("Senha", type = "password")

# cria botão
if st.button("Entrar"):
    if usuario in USUARIOS and USUARIOS[usuario] == senha:
        st.session_state.logado = True
        st.session_state.usuario = usuario
        st.switch_page("pages/1_Visao_Geral.py")
    else:
        st.error("Usuário ou senha inválidos")






















