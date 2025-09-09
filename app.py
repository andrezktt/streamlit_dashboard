import streamlit as st
import plotly.express as px

from dataset import df
from utils import format_number
from charts import (chart_state_income_geo, chart_month_income, chart_state_income,
                    chart_category_income, chart_sellers_income, chart_sellers_qtt)

st.set_page_config(layout="wide")
st.title('Dashboard de Vendas :shopping_cart:')

st.sidebar.title('Filtro de Vendedores')

seller_filter = st.sidebar.multiselect(
    label='Vendedores',
    options=df['Vendedor'].unique(),
)

if seller_filter:
    df = df[df['Vendedor'].isin(seller_filter)]

tab_01, tab_02, tab_03 = st.tabs(['Dataset', 'Receita', 'Vendedores'])
with tab_01:
    st.dataframe(df)
with tab_02:
    column_01, column_02 = st.columns(2)
    with column_01:
        st.metric('Receita Total', format_number(df['Preço'].sum(), 'R$'))
        st.plotly_chart(chart_state_income_geo, use_container_width=True)
        st.plotly_chart(chart_state_income, use_container_width=True)
    with column_02:
        st.metric('Quantidade de Vendas', format_number(df.shape[0], ''))
        st.plotly_chart(chart_month_income, use_container_width=True)
        st.plotly_chart(chart_category_income, use_container_width=True)
with tab_03:
    column_01, column_02  =st.columns(2)
    with column_01:
        st.plotly_chart(chart_sellers_income, use_container_width=True)
    with column_02:
        st.plotly_chart(chart_sellers_qtt, use_container_width=True)