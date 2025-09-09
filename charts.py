import plotly.express as px
from utils import df_state_income

chart_state_income = px.scatter_geo(
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