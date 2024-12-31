import streamlit as st
import pandas as pd

df_reviews = pd.read_csv(".github/workflows/dados_projeto/customer reviews.csv")
df_top_100_books = pd.read_csv(".github/workflows/dados_projeto/Top-100 Trending Books.csv")

price_max = df_top_100_books["book price"].max()  #crio um var e defino que ela recebera um metodo pandas que lee a coluna de preço e logo utilizo um metodo para procurar com maior valor, faço o mesmo com a metodo min
price_min = df_top_100_books["book price"].min()
max_price = st.sidebar.slider("Preços dos Livros",price_min,price_max,price_max) #siderbar 
df_top_100_books[df_top_100_books["book price"] <= max_price]
