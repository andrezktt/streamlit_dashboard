import pandas as pd
from dataset import df

def format_number(value, prefix):
    for unit in ['', 'mil']:
        if value < 1000:
            return f'{prefix} {value:.2f} {unit}'
        value /= 1000
    return f'{prefix} {value:.2f} milhões'

# print(df.columns)

# 1 - Dataframe - Receita por Estado
df_state_income = df.groupby('Local da compra')[['Preço']].sum()
df_state_income = (df.drop_duplicates(subset='Local da compra')[['Local da compra', 'lat', 'lon']]
                   .merge(df_state_income, left_on='Local da compra', right_index=True)
                   .sort_values('Preço', ascending=False))
# print(df_state_income)

# 2 - Dataframe - Receita por Mês
df_month_income = (df.set_index('Data da Compra')
                   .groupby(pd.Grouper(freq='ME'))['Preço']
                   .sum().reset_index())
df_month_income['Ano'] = df_month_income['Data da Compra'].dt.year
df_month_income['Mês'] = df_month_income['Data da Compra'].dt.month_name()
# print(df_month_income)

# 3 - Dataframe - Receita por Categoria
df_category_income = df.groupby('Categoria do Produto')[['Preço']].sum().sort_values('Preço', ascending=False)
# print(df_category_income)