import streamlit as st

from dataset import df

st.title('Dataset de Vendas')

with st.expander('Colunas'):
    columns = st.multiselect(
        'Selecione as colunas',
        list(df.columns),
        list(df.columns),
    )

st.sidebar.title('Filtros')

with st.sidebar.expander('Categoria do Produto'):
    category = st.multiselect(
        label='Selecione as Categorias',
        options=df['Categoria do Produto'].unique(),
        default=df['Categoria do Produto'].unique()
    )

with st.sidebar.expander('Preço do Produto'):
    price = st.slider(
        label='Selecione o Preço',
        min_value=0,
        max_value=5000,
        value=(0, 5000)
    )

with st.sidebar.expander('Data da Compra'):
    selling_date = st.date_input(
        label='Selecione a Data',
        value=(df['Data da Compra'].min(), df['Data da Compra'].max())
    )

query = '''
    `Categoria do Produto` in @category \
    and @price[0] <= Preço <= @price[1] \
    and @selling_date[0] <= `Data da Compra` <= @selling_date[1]
'''
filtered_data = df.query(query)
filtered_data = filtered_data[columns]

st.dataframe(filtered_data)