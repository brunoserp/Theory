''' LÓGICA DO pd.to_datetime(valor,format):
No valor vc deve passar uma string com formato completo de dia, mes e ano, em qualquer ano, e passar a formatação desse
valor no format. Lembrando que, se dia ou mês tiverem sem 0 a esquerda, é só colocar um # seguido da indicação (d pra dia ou m pra mês)

O to_datetime vai formatar em datetime, exibindo em formato americano (caso vc queira outra exibição, deverá usar o strftime, que 
transforma em string, porém na exibição que vc especificar)

Caso vc queira transformar inteiro em datetime, deverá usar os parâmetros unit e origin (especificados abaixo)
'''




r'''
TEORIA:
    DATA NO PYTHON
biblioteca nativa DateTime 
DateTime tem 6 classes principais:
    -> date: year, month, day
    -> time: hour, minute, second, microsecond, tzinfo      (assumes that every day has 24*60*60 seconds)
    -> date-time: combination of date and time
    -> timedelta: difference between two dates, times or datetimes instances to microsecond resolution
    -> tzinfo: time zone 
    -> timezone: implements a tzinfo abstract base class as a fixed offset from the UTC
___________________________________________________________
PYTHON DATE CLASS
    syntax: class datetime.date(year,month,day)
    Cria um objeto date de formato ano - mês - dia

        import datetime
        a = datetime.date(1995,9,5)
        print("Eu nasci em", a)        
            --- Eu nasci em 1995-09-05
___________________________________________________________
DATA DE HOJE
    MÉTODO .today()
        import datetime
        b = datetime.date.today()
        print("A data de hoje é", b)
            --- A data de hoje é 2024-02-04

    .today() tem atributos year, month e day:
        c = datetime.date.today().day()
        d = datetime.date.today().month()
        e = datetime.date.today().year()
        print("Hoje é dia", c, 
        \n"do mês", d,
        \n"do ano ", e)
        
        --- Hoje é dia 4
        -- do mês 9
        -- do ano 2024

___________________________________________________________
DATE TO STRINGS: strftime()
    Transforma o objeto date em uma string, permitindo variações de formatos:
    Ex: 05/09/95, 05-09-1995, sep, 2024, 09|05

    Tem parâmetro de formato, ex:
    print(b)
        -- 2024-02-04
    c = b.strftime('%d/%m/%y')
    print(c)
        -- 04-02-2024
    
                
    Opções de formatação:
    PADRÃO:
        %d: dia do mês (de 01 a 31)
        %m: nº do mês (1 a 12)
        %y: ano curto (2 últimos dígitos)
        %Y: ano completo
    OUTROS:
        %b: nome do mês, versão curta (ex: 12 = dec)
        %B: nome completo do mês
    
    MAIS: https://www.w3schools.com/python/python_datetime.asp

    EX:
        import datetime
        b = datetime.date.today()
        print("A data de hoje é", b)
            --- A data de hoje é 2024-02-04
        
        c = b.strftime('%d|%m')
        print("Mês/Ano de hoje:",c)
            --- Data de hoje formatada: 04|02

___________________________________________________________
STRING TO DATE: strptime()
    Apenas converte str to date, não é possível mudar a formatação
    Ex: se a string tiver no formato %m-%d-%y, ele vai converter pra
    date no formato %d-%m-%y
    
    Sintaxe: datetime.datetime.strptime(date object, format)
    Retorna um objeto datetime 
    A string deve ter padrões: tudo com 2 dígitos, separado por -

    import datetime
    x='24-05-15'
    print(datetime.datetime.strptime(x,"%y-%m-%d")
        --- 2024-05-15 00:00:00
    
    Tem atributo .date(), .day, .month e .year
    print(datetime.datetime.strptime(x,"%y-%m-%d").date())
        --- 2024-05-15

    print(datetime.datetime.strptime(x,"%y-%m-%d").day)
        --- 15        

    A string não precisa estar no formato %y-%m-%d:
    import datetime
    x='30-05-15'
    print(datetime.datetime.strptime(x,"%d-%m-%y").date())
        --- 2015-05-30


O Pandas tem uma função .to_datetime que converte str pra datetime64[ns]


'''

# PRÁTICA
import pandas as pd
import os
import datetime

'''1) vc tem uma coluna com ano, outra com mês e precisa formar uma coluna de data com ambas:
https://stackoverflow.com/questions/48304927/cleanly-combine-year-and-month-columns-to-single-date-column-with-pandas'''
dic_juntar_data = {'ano': [2020,2019,2022,2021],'mês':[5,8,11,12]}
df = pd.DataFrame(dic_juntar_data)
# print(f'Dataframe inicial:\n')
# print(df)

'''a) Junção das colunas mês e ano pra formar a data (em formato americano). Após essa inclusão, a coluna data tem formato datetime64[ns]'''
df['data'] = pd.to_datetime(df['ano'].astype(str) + '/' + df['mês'].astype(str) + '/01')
# print(f'\nDataframe pós formatação de data:\n')
#print(df['data'])

'''b) ok, está no formato americano (2020-01-05), e se eu quiser mudar pra d/m/y?'''
# A função strftime formata do jeito desejado, ex: 01/05/2020. Porém, está como str
#df['data'] = df['data'].dt.strftime('%d/%m/%Y')

'''E se passasse essa função .strftime e depois convertesse pra to_datetime?'''
#df['data'] = pd.to_datetime(df['data'].dt.strftime('%d/%m/%Y'))
# O to_datetime resulta no formato americano 2020-01-05
# print(df['data'])

r'''A coluna de data está como número inteiro, devido à formatação. Como formato em data?
https://www.shiksha.com/online-courses/articles/date-and-time-in-pandas/
Primeiramente, um número inteiro a ser formatado em data significa a quantidade de dias (ou outra unidade de medida de tempo) posterior 
a uma data de referência
'''

# Como exemplo, vamos supor que 40910 seja 02/01/2012
#dic_inteiro = {'data': [40910,40902,40911,40912,1]}
#df_inteiro = pd.DataFrame(dic_inteiro)
'''o to_datetime tem 2 parâmetros pra essa conversão:
-> origin: define a data inicial
-> unit: define a unidade de medida de tempo a ser contado a partir da data inicial'''
# df_inteiro['data'] = pd.to_datetime(df_inteiro['data'],unit='D',origin='1899-12-30')
'''Essa linha acima conta os dias da coluna data (pra cada linha) a partir de 30 de dezembro de 1899
Por exemplo, o nº 1 a ser formatado viraria 1899-12-31, pois é 1 dia (unit=D) após 1899-12-30'''
# print(df_inteiro)
''' O argumento padrão para unit é unix (1970-01-01)'''

''' Um caso prático: formato de data assim: 30112017. 
1º) é importante converter a coluna de data pra str no read_csv
2º) a lógica é: caso a data esteja com dia, mes e ano, vc deve colocar a coluna dentro do to_datetime e passar o formato certo. Isso vai transformar
em datetime com exibição em formato americano'''
pasta = r"C:\Users\bserpellone\Desktop\Python"
arquivo='teste_data_sped.csv'
df=pd.read_csv(os.path.join(pasta,arquivo),delimiter=';',dtype={'C100_DT_DOC': str,'C100_DT_E_S':str})
#print(df)
#df['C100_DT_DOC_form'] = pd.to_datetime(df['C100_DT_DOC'],format='%Y/%m/%d',errors='coerce')
#print(df)
