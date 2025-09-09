import plotly.express as px
from utils import df_state_income, df_month_income

# 1 - Receita por Estado (Mapa)
chart_state_income_geo = px.scatter_geo(
    data_frame=df_state_income,
    lat='lat',
    lon='lon',
    scope='south america',
    size='Preço',
    template='seaborn',
    hover_name='Local da compra',
    hover_data={'lat': False, 'lon': False},
    title='Receita por Estado'
)

# 2 - Receita por Mês
chart_month_income = px.line(
    data_frame=df_month_income,
    x='Mês', y='Preço',
    markers=True,
    range_y=(0, df_month_income.max()),
    color='Ano',
    line_dash='Ano',
    title='Receita Mensal'
)
chart_month_income.update_layout(yaxis_title = 'Receita')