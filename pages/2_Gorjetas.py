# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 22:42:08 2026

@author: ra-el
"""

# carrega os pacotes
import streamlit as st
from data import load_tips

# proteção
if "logado" not in st.session_state or not st.session_state.logado:
    st.switch_page("Menu.py")
    
# título da página
st.title("Gorjeta")

# carrega o df
df = load_tips()

# criando uma nova coluna
df["tip_pct"] = df["tip"] / df["total_bill"] * 100

# criando uma tabela
tabela_gen = (df.groupby("sex", as_index = False)["tip_pct"].mean()
              .rename(columns = {"sex": "Gênero", "tip_pct": "Média das Gorjetas"})
              )



# mostra a tabela
tabela_gen



# botão para sair
if st.sidebar.button("Sair"):
    st.session_state.logado = False
    st.switch_page("Menu.py")
    
    
    
    
    
    
    
    
    
    
    
    
    
    