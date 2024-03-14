# ler o excel
# exel_file = 'faculdade/pi_ciencia_de_dados_e_analytics/ei_01/DNRS2022.xlsx'
# df_xlsx = pd.read_excel(exel_file)
# # acessando colunas na planilha do excel
# idades = df_xlsx['IDADEMAE']
# codResMae = df_xlsx['CODOCUPMAE']
# codSexo = df_xlsx['SEXO']
# # variáveis
# menor_idade = idades  # função que retorna o mínimo/menos
# pessoas = []  # array para armazenar as pessoas

# # iterar cada idades em idades, com o index i
# for i, idade in enumerate(idades):
#     # se a idade for igual a menor idade encontrada
#     if idade == menor_idade:
#         # colocar no array de pessoas
#         pessoas.append((codResMae[i], codSexo[i]))
# # printar resultados
# print('a menor idade é:', menor_idade)
# # para cada residência e sexo em pessoas printar
# for codRes, codSexo in pessoas:
#     print('código do município:', codRes, '\nsexo do bebê:', codSexo)