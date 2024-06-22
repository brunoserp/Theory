# p valor = área do gráfico pro z valor, ver se tá dentro da área de rejeição: stats.norm.sf(z)

import pandas as pd
import numpy as np
import scipy.stats as stats
''' 
1) Exemplo teste t: peguei uma tabela com diabéticos x índice de massa corporal

df = pd.read_csv('diabetes.csv')
df['Outcome'] = np.where(df['Outcome']==0,'N',"S")
# print(df.shape[0]) >> 768 linhas, diabetes = 268 sim, 500 não

>> print(df.groupby('Outcome')[['BMI','BloodPressure','Age','Pregnancies']].mean())

               BMI  BloodPressure        Age  Pregnancies
Outcome
Não      30.304200      68.184000  31.190000     3.298000
Sim      35.142537      70.824627  37.067164     4.865672


Quero testar se o % de gordura corporal, BMI, é estatisticamente relevante para diabetes.
Comparando o grupo com diabetes com os sem diabetes:
    
    H0 = mi1 = mi2
    Ha = mi1 <> mi2

    Alfa = 5%

Var BMI diabéticos = 52.553862218756954
Var BMI ñ diabéticos = 59.01560236

Prop < de 4:1 => considerar variâncias iguais


bmi_diab = df["BMI"][df["Outcome"]=="S"]
bmi_n_diab = df["BMI"][df["Outcome"]=="N"]
t_critical = stats.t.ppf(1 - 0.05/2, df=len(bmi_diab) + len(bmi_n_diab) - 2)
t,p = stats.ttest_ind(a=bmi_diab, b=bmi_n_diab, equal_var=True)
print(f'estatística t = {t} x t crítico {t_critical}\np valor = {p:.20f}')

estatística t = 8.47183994786525 x t crítico 1.9630657604066013
p valor = 0.00000000000000012298

estatística t > t crítico => curva diabéticos intercepta cuvrva não diabéticos muito pra direita, numa área de 0.00000000000000012298 (p valor)
Assumindo alfa = 5%, rejeitamos H0 que a média de ambos os grupos é estatisticamente igual
'''

'''
2) Calculando Z padrão:
estatística_z = (media_amostral - media_pop) / (dp_pop / (tamanho_amostra**0.5))

p-valor à esq = stats.norm.sf(estatistica_z)
compara p valor com nível de significância

'''

'''
3) testar se uma moeda é justa. Teta = prob de sair cara
H0: teta = 1/2
HA: teta <> 1/2
n=100

'''

nicotina = [26,24,23,22,28,25,27,26,28,24]
var_pop = 5.36
alfa = 0.05

# H0: mi >= 26
# HA: mi < 26 

'''
teste bicaudal a esquerda
(media - 26) / (dp/n)

#print((sum(nicotina)/10)-26/((var_pop**0.5)/len(nicotina)))
estat_z = ((sum(nicotina)/10)-26)/((var_pop**0.5)/len(nicotina)**0.5)
print(f'Z = {estat_z}')
p = stats.norm.cdf(estat_z)
print(f'p-valor = {p}')
print(f'Rej H0 se p valor < alfa {alfa}: {abs(p)<abs(alfa)}')'''

# lajotas
mi = 206
dp = 12
n = 30
x_barra = 210
alfa = 0.1
'''
H0: mi <= 206 
HA: mi > 206

z = (x_barra - mi) / (dp/n**0.5)
'''
z = ((x_barra - mi) / (dp/n**0.5))
print(f'z = {z}')
# agora, vamos testar se o z = 1.825 está na região crítica de alfa = 10% (teste unicaudal a direita)
