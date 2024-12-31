import streamlit as st
import panda as pd

df_reviews = pd.read_csv("dados_projeto/customer reviews.csv")
df_top_100_books = pd.read_csv("dados_projeto/Top-100 Trending Books.csv")

df_reviews
