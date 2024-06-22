import matplotlib.pyplot as plt
import plotly
'''
Criar e mostrar um gráfico:
Redimensionar o tamanho do gráfico:
>>> plt.figure(figsize=(10,6))
Criar o gráfico
>>> plt.plot([coordenadas_x], [coordenadas_y])
Há vários parâmetros pra personalizar esse gráfico no .plot(): color, marker. https://matplotlib.org/2.1.1/api/_as_gen/matplotlib.pyplot.plot.html
>>> plt.title('Título gráfico')
>>> plt.xlabel('Título eixo X')
>>> plt.ylabel('Título eixo Y')
Quando vc quer criar mais de 1 gráfico com subconjuntos da tabela fonte dos dados
>>> plt.subplot(xyz)
Onde x = linha de gráfico, y = coluna de gráfico e z = posição do gráfico


SEABORN as sns
Fazer um gráfico de pontos (x,y)
>>> sns.relplot(x="nome_col_categórica",y="nome_col_numerica", data=df, hue = "coluna_categoria", size="size_coluna")
o hue pinta os pontinhos conforme a categoria
O size deixa o ponto no gráfico proporcional aos valores da coluna indicada
>>> sns.barplot(x='coluna_categórica',y='coluna_numérica',data=df)

'''