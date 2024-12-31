import streamlit as st
import pandas as pd

df_reviews = pd.read_csv(".github/workflows/dados_projeto/customer reviews.csv")
df_top_100_books = pd.read_csv(".github/workflows/dados_projeto/Top-100 Trending Books.csv")

df_reviews
df_top_100_books
