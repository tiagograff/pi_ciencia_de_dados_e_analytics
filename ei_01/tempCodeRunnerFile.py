file_csv = 'faculdade/pi_ciencia_de_dados_e_analytics/ei_01/tb_municip.csv'
df_csv = pd.read_csv(file_csv, index_col=False)

print(df_csv['CO_MUNICIP'].head(5))