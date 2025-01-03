import streamlit as st #Cria o App
import pandas as pd #manipula dados e tabelas
import plotly.express as px

df_reviews = pd.read_csv(".github/workflows/dados_projeto/customer reviews.csv")
df_top_100_books = pd.read_csv(".github/workflows/dados_projeto/Top-100 Trending Books.csv")
st.header("Top 100 Bestselling Book Reviews on Amazon")
price_max = df_top_100_books["book price"].max()  #crio um var e defino que ela recebera um metodo pandas que lee a coluna de preço e logo utilizo um metodo para procurar com maior valor, faço o mesmo com a metodo min
price_min = df_top_100_books["book price"].min()
max_price = st.sidebar.slider("Preços dos Livros",price_min,price_max,price_max) #siderbar https://docs.streamlit.io/develop/api-reference/widgets/st.slider
df_books = df_top_100_books[df_top_100_books["book price"] <= max_price] # Variavel procura dentro da coluna book price o maior o igual valor. isso o pandas manipula a tapela 
df_books

gafico_1 = px.bar(df_books["year of publication"].value_counts()) 
gafico_2 = px.histogram(df_books["book price"].value_counts()) 

st.plotly_chart(gafico_1)
st.plotly_chart(gafico_2)
