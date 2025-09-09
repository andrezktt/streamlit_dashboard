from dataset import df

def format_number(value, prefix):
    for unit in ['', 'mil']:
        if value < 1000:
            return f'{prefix} {value:.2f} {unit}'
        value /= 1000
    return f'{prefix} {value:.2f} milhões'


df_state_income = df.groupby('Local da compra')[['Preço']].sum()
df_state_income = (df
                   .drop_duplicates(subset='Local da compra')[['Local da compra', 'lat', 'lon']]
                   .merge(df_state_income, left_on='Local da compra', right_index=True)
                   .sort_values('Preço', ascending=False))

print(df_state_income)