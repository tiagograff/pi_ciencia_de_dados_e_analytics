import pandas as pd

# ler o excel
excel_file = 'faculdade/pi_ciencia_de_dados_e_analytics/ei_01/DNRS2022.xlsx'
df_xlsx = pd.read_excel(excel_file)

# acessar colunas da planilha
idades = df_xlsx['IDADEMAE']
codResMae = df_xlsx['CODMUNRES']
codSexo = df_xlsx['SEXO']

# variáveis
# função que retorna o menor valor
menor_idade = idades.min()
# arrays para armazenar valores
pessoas = []
municipios = []
sexos = []

# for index e idade em idades
for i, idade in enumerate(idades):
    # se a idade for igual a menor encontrada
    if idade == menor_idade:
        # armazena informações nos arrays
        pessoas.append(idade)
        municipios.append(codResMae[i])
        sexos.append(codSexo[i])

# imprimir informações obtidas
# itera simultaneamente sobre múltiplas listas
for idade, municipio, sexo in zip(pessoas, municipios, sexos):
    print('idade da mãe:', idade, '\ncódigo do município',
          municipio)

# Ler o CSV com os códigos dos municípios e seus nomes
file_csv = 'faculdade/pi_ciencia_de_dados_e_analytics/ei_01/tb_municip.csv'
# lendo arquivo csv e colocando o delimitador padrão como ; e tirando a coluna index
df_csv = pd.read_csv(file_csv, delimiter=';', index_col=False)
# para codigos de municpio em municipios
for index, codigo_municipio in enumerate(municipios):
    # reservar nome do municipio onde loc [linhas, colunas]
    nome_municipio = df_csv.loc[df_csv['CO_MUNICIP']
                                == codigo_municipio, 'DS_NOME'].iloc[index]
    # printar municipio
    print('municipio:', nome_municipio)
    index += 1

# baseado nos documentos Estrutura SINASC_rev_NOVO.doc
for sexo in sexos:
    if sexo == 0:
        print('sexo: indefinido')
    elif sexo == 1:
        print('sexo: masculino')
    elif sexo == 2:
        print('sexo: feminino')
    else:
        print('não encontrado')
    index += 1
