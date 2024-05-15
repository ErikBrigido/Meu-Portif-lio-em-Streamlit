import streamlit as st

# Definindo o layout do aplicativo
st.set_page_config(layout="wide")

# Conteúdo principal do aplicativo
st.title("Um pouco sobre mim...")
st.write("""Olá, Seja Bem vindo ao meu portifolio !
         Me chamo Erik brigido, tenho 26 anos de idade""")

# Definindo a barra lateral
st.sidebar.title("Erik Brigido")

st.sidebar.markdown("""
    <span style='font-size: 17px; color: black;'>Background Profissional</span>  
""", unsafe_allow_html=True)

st.sidebar.markdown("""
    <span style='font-size: 13px;'>Auditor da Qualidade</span>  
    <span style='font-size: 13px;'>Analista de Automação</span>  
    <span style='font-size: 13px;'>Analista de Dados - Gestão</span>  
    <span style='font-size: 13px;'>Analista de Dados - E-commerce</span>
""", unsafe_allow_html=True)

st.sidebar.markdown("""
    <span style='font-size: 16px;color: black;'>Experiência por Segmento</span>  
""", unsafe_allow_html=True)

st.sidebar.markdown("""
    <span style='font-size: 13px;'>ACP Plasticos | Industria</span>  
    <span style='font-size: 13px;'>Zaraplast | Industria</span>  
    <span style='font-size: 13px;'>Braspress | Logistica</span>  
    <span style='font-size: 13px;'>Supermercados Nagumo | Varejo</span>
""", unsafe_allow_html=True)

st.sidebar.markdown("""
    <span style='font-size: 16px;color: black;'>Formação</span>  
""", unsafe_allow_html=True)

st.sidebar.markdown("""
    <span style='font-size: 13px;'>Tec.Automação Industrial - IFSP</span>  
    <span style='font-size: 13px;'>Grad.Proc. Gerenciais - ENIAC</span>  
    <span style='font-size: 13px;'>Pós.Eng.da Qualidade - ENIAC</span>  
    <span style='font-size: 13px;'>MBA.Gest.da Qualidade - FM2S</span>
    <span style='font-size: 13px;'>MBA.Data Science- USP</span>
""", unsafe_allow_html=True)