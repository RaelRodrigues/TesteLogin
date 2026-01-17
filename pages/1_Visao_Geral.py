# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 22:37:45 2026

@author: ra-el
"""

# carrega os pacotes
import streamlit as st
from data import load_tips

# proteção
if "logado" not in st.session_state or not st.session_state.logado:
    st.switch_page("Menu.py")
    
# título da página
st.title("Visão Geral")

# carrega o df
df = load_tips()

# mostra a tabela
st.dataframe(df.head())

# botão para sair
if st.sidebar.button("Sair"):
    st.session_state.logado = False
    st.switch_page("Menu.py")