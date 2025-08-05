import streamlit as st
import dados

st.title("Filmes")

# Defina o formulário com 'st.form'
with st.form("form_adicionar_filme"):
    nome = st.text_input("Nome")
    ano = st.number_input("Ano do Filme", min_value=1900, max_value=2025, step=1)
    nota = st.slider("Nota", min_value=0.0, max_value=10.0, step=0.1)
    
    # Botão para submeter dentro do formulário
    submit = st.form_submit_button("Adicionar Filme")

# Ação após submeter o formulário
if submit:
    dados.inserir_dados(nome, ano, nota)
    st.success("Filme adicionado com sucesso!")

# Mostrar a lista de filmes
filmes = dados.obter_dados()
st.header("Lista de Filmes")
st.table(filmes)
