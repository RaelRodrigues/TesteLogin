# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 22:46:44 2026

@author: ra-el
"""

# carrega os pacotes
import streamlit as st
from data import load_tips

# proteção
if "logado" not in st.session_state or not st.session_state.logado:
    st.switch_page("Menu.py")
    
# título da página
st.title("Conta média por dia")

# carrega o df
df = load_tips()

# criando uma nova tabela
tabela_dia = (
    df.groupby("day", as_index = False)["total_bill"].mean()
    .rename(columns = {"day": "Dias", "total_bill": "Total da Conta"})
    )


# mostra a tabela
tabela_dia


# botão para sair
if st.sidebar.button("Sair"):
    st.session_state.logado = False
    st.switch_page("Menu.py")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    