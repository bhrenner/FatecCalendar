import pandas as pd

geral = 'FatecCalendar/cursos/geral.csv'
df_geral = pd.read_csv(geral)
#df_g = df_geral.set_axis(['Semestre','Dia','Horário','Sala','Curso','Disciplina','Nome','Professor'], axis=1, inplace=False)

path = 'FatecCalendar/grade/' + 'segunda' + '.csv'
df = pd.read_csv(path)
if 'Unnamed: 0' in df.columns:
    df.drop(['Unnamed: 0'], axis=1, inplace=True)
    tabela = df.set_axis(['Horário', 'Disciplina', 'Turma'], axis=1, inplace=False)
    m = pd.merge( tabela, df_geral, on = ['Disciplina', 'Horário'], how='left')
if 'Unnamed: 0' not in df.columns:
    tabela = df.set_axis(['Horário', 'Disciplina', 'Turma'], axis=1, inplace=False)
    m = pd.merge( tabela, df_geral, on = ['Disciplina', 'Horário'], how='left')
#m.drop(["Horário_y"], axis=1, inplace=True)
#df = m.rename({'Horário_x': 'Horário'}, axis = 1)
#df2 = df.drop_duplicates()

#result = pd.merge(tabela, df2, on = ['Horário'], how='left')

#m = pd.merge( tabela, df_geral, left_on=[tabela.iloc[:, [0,1]]], right_on=[df_geral.iloc[:, [2,5]]],how='left')
#a1 = pd.concat([tabela, df2], axis=1)
#m = pd.concat([tabela, df_geral], axis=1).dropna()
#df2 = m.T.drop_duplicates().T

#m = tabela.merge(df_geral, lon=[tabela.iloc[:, [0,1]]])
#m.to_csv("FatecCalendar/teste/teste_merge.csv", encoding="UTF-8", sep=",", index=False)
print(tabela)
print('//////////////////////////////////')
print(df_geral)
print('//////////////////////////////////')
print(m)