r'''
base: https://realpython.com/pandas-merge-join-and-concat/

Métodos pra relacionamento entre 2 dataframes:
1) MERGE
Puxa informações de um dataframe para outro com base em 1 coluna em comum em cada dataframe

Sintaxe: 
        df1.merge(df2, on='', how='', suffixes=())

O merge, por padrão, vai juntar todas as colunas dos 2 dataframes
É possível selecionar colunas do df2, passando os nomes das colunas entre colchetes
on: é a coluna presente nos 2 df que se relacionam, pra usar esse parâmetro, as colunas dos 2 df devem ter o mesmo nome
    caso não tenham o mesmo nome, use os parâmetros left_on, com o nome da coluna do df1, e right_on, com o nome da coluna do df2 que são relacionadas
    caso esse parâmetro não seja especificado, ele vai usar as colunas de mesmo nome nos 2 df

how: é a forma como o merge vai funcionar. É semelhante ao join do sql, aceita valores: left, right, outer, inner, etc
    vale lembrar que o left mantém todas as linhas do df1 e o right, do df2 (porém, duplica as linhas no df1 caso haja mais valores repetidos no df2)
    o inner só vai as linhas cujos valores estejam tanto na df1 quanto na df2
    o outer vai juntar tudo, independentemente de tiver nos 2 df
    OBS: o ideal é que df2 seja uma planilha dimensão, ou seja, que os valores sejam distintos. Caso contrário, para cada valor de df1 que tiver 
        duplicado no df2, o merge vai repetir as linhas do df1 que se repetem em df2, cada uma com um valor de df2

suffixes: caso haja colunas nos 2 df com nomes iguais, esse parâmetro aceita uma tupla com 2 elementos onde o 1º elemento é o sufixo do nome das colunas de df1
            que se repetem no df2, e o 2º elemento vai ser o sufixo do nome das colunas de df2 que se repetem em df1. Assim, fica mais fácil distinguir
            de qual df é cada coluna com nome repetido

            
2) JOIN
É o merge com how = left nos indexes (linhas ou colunas). Join permite a junção de mais de 2 df ao mesmo tempo, diferente do merge

Sintaxe:
        df1.join(df2, on=, how=, lsuffix=, rsuffix=)
Apenas o df2 é obrigatório

3) CONCAT
Junta 2 dataframes, um embaixo do outro, ou um do lado do outro

Sintaxe:
        pd.concat(df1,df2,axis=)

axis: 0 por padrão, onde junta as 2 tabelas uma embaixo da outra
      1 junta uma ao lado da outra

Caso axis = 0, ele só vai juntar nas mesmas colunas se os nomes forem idênticos
Caso contrário, ele vai criar as colunas com nomes diferentes, atribuindo NaN no df que não tiver essa coluna
Caso necessário, crie 2 dataframe pelo pd.DataFrame com o parâmetro columns com uma lista dos nomes das colunas desejadas



'''