import streamlit as st
import plotly.express as px

from dataset import df

st.set_page_config(layout="wide")
st.title('Dashboard de Vendas :shopping_cart:')

tab_01, tab_02, tab_03 = st.tabs(['Dataset', 'Receita', 'Vendedores'])
with tab_01:
    st.dataframe(df)
