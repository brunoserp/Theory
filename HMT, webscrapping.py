'''
https://www.youtube.com/watch?v=42sTntMEn6o&list=PLg3ZPsW_sghSkRacynznQeEs-vminyTQk&index=1
texto$: busca elementos que terminam com o texto
texto^: busca elementos que comecem com o texto

HTML
Estrutura feita por tags (marcações).
Toda tag tem uma marcação de início <> e de fim, </>
Dentro da tag tem uma letra/palavra que é chamada de elemento, e é padronizada para cada funcionalidade. Por ex, <a> é para link, <p> pra parágrafo, etc
Entre a tag de abertura e fechamento tem o conteúdo

 
Todo HTML começa com a tag <html> e termina com </html>:

<html>
<head>
    <title>Meu primeiro site</title>
</head>
<body>
    <p>Isso é um parágrafo</p>
</body>
</html>

Cada tag dessa tem uma função:
Por ex, <title> dentro do <head> nomeia a página acima do site

Algumas tags:
<html>: conteúdo HTML
<head>: cabeçalho do documento
<title>: título da página html
<body>: corpo do documento (página)
<h1>: cabeçalho de nível 1 (pode ir de 1 a 6)
<p>: parágrafo
<div>: conteúdo genérico (aparece abaixo da linha da tag acima)
<a>: link
<span>: conteúdo genérico em linha (aparece ao lado da linha da tag acima)
<table>: tabela
<ul>: lista não numerada (em tópicos)
<ol>: lista numerada
<li>: elemento da lista
<img>: imagem

Exemplo do <a>:
<a href="google.com">Clique aqui pra acessar o meu site pessoal</a>
Cria um link clicável com o nome "Clique aqui pra acessar meu site pessoal", e, ao clicar, te direciona ao google.com na mesma aba (tem como abrir numa outra aba tbm, mas
assim é mais simples)

Exemplo de <img>:
<img width="200px" src="diretório onde está a imagem" alt="descrição da imagem">

Cada tag tem atributos que caracterizam aquela funcionalidade, por ex a width em <img> que ajusta o tamanho da imagem

_______________________________________________________________________________________________________
PROTOCOLO HTTP E BIBLIOTECA REQUEST (solicitar requisição de um site)

Protocolo é uma padronização do envio e recebimento de informações. Quando vc acessa o Google, vc envia um protocolo pra acessar tal informação (do tipo get),
que é respondida automaticamente e o acesso é concedido.

HTTP: hypertext transfer protocol
HTML é um tipo de hypertext

Quando vc entra no Google, vc pede permissão pra acessar aquilo (método get). O servidor vai procurar qual o ID do computador que concede acesso e solicitar o acesso.

Métodos HTTP:
-> GET: slicita u mrecurso pro servidor (uma página da web, por exemplo)
-> POST: envia uma informação pro servidor (ex login)

Códigos de status (como respostas da requisição):
1XX: informativo: resposta sem conteúdo, contendo apenas informação sobre a comunicação
2XX: sucesso: a mensagem chegou ao servidor e era válida
3XX: redirecionamento: recurso buscado está em outro servidor
4XX: erro do cliente: a requisição possui algum erro
5XX: o servidor não pode atender à requisição

Usando requisições no PYTHON:
biblioteca requests

>>> response = requests.get(url)
# esse objeto acima tem atributos, como status_code, header, content :
>>> response.status_code
>>> 200             # é o código da resposta à requisição, 200 significa que foi bem sucedido
        Outros atributos do response: https://www.w3schools.com/python/ref_requests_response.asp
O atributo content, por exemplo, mostra todo o conteúdo html do site:
content = response.content

__________________________________________________________________________________________
3) BIBLIOTECA BEAUTIFULSOUP (bs4): procurar conteúdos dentro de um site (dentro do objeto content do get acima)
O beautifulsoup é uma classe dentro do bs4

>>> from bs4 import BeautifulSoup
>>> site = BeautifulSoup(content, 'html.parser')        # transforma o conteúdo do content em html
>>> site.prettify()         # organiza melhor o html do site

Como buscar a primeira ocorrência de uma tag específica:
Por exemplo, na tabela de estatísticas da CBV, quero ver o nome das jogadoras pelo HTML. Ao clicar no nome da jogadora e ir em
inspecionar, vejo que o nome está na tag <span. Porém, há varias outras tags span, cada uma com uma funcionalidade. P/ eu buscar
apenas a span de interesse, eu uso o atributo .find, passo a tag (span) como 1º argumento e o atributo num dicionário como 2º arg:
>>> nome_jogadora = site.find('span', attrs={'class': 'Ranking_PlayerName'})    # procura a tag (1º arg.) e o atributo (2º arg. como um dicionário com o nome (geralmente class) e o valor)
O nome_jogadora tem várias outras informações além do nome da jogadora. Caso vc queira pegar apenas o nome da jogadrora, faça:
>>> nome_jogadora.text

OBS: o .find() busca apenas a 1ª ocorrência da tag/atributo 
Pense na página inicial do G1 por ex, vc quer procurar pela manchete. Primeiramente, extraia a tag da área de cada notícia (como manchete,
descrição, etc) no find(). Eu acho mais fácil procurar o nome da manchete na inspeção e usar a tag mais próxima no find.
Nesse objeto do find vai ter também outras tags filhas referentes à manchete, como título, descrição, horas corridas da criação da notícia.
E aí vc pode usar outro find nesse último objeto pra pegar só o título da manchete observando as tags e atributos pelo prettify().

Caso G1, como buscar a primeira ocorrência duma tag (da manchete):
Para buscar o título de todas as notícias do site do G1:
>>> requisicao = requests.get("https://g1.globo.com/")
>>> content = requisicao.content
>>> site = BeautifulSoup(content, 'html.parser')        # transforma o conteúdo do content em html
>>> print(site.prettify())      # aqui eu observo o html organizado do g1
>>> noticia = site.find('div', attrs={'class': '_evt'})
>>> titulo = noticia.find('p',attrs={'elementtiming': 'text-ssr'})

__________________________________________________________________________________________
4) Como buscar todas as tags/atributos da página com .findAll():
Pra vc acessar um atributo, vc precisa iterar sobre o objeto findAll() extraindo, pelo find(), a tag e a classe da linha que contém o link,
e depois vc localiza o atributo pelo nome desse novo objeto e o nome do atributo entre colchetes
Nesse caso, vou tentar buscar a manchete e o link de cada matéria do g1:

>>> requisicao = requests.get("https://g1.globo.com/")
>>> content = requisicao.content
>>> site = BeautifulSoup(content, 'html.parser')        # transforma o conteúdo do content em html
Extrair todas as classes evt, que tem a manchete das colunas:
>>> nomes = site.findAll('div',attrs={'class': '_evt'})
Iterar sobre cada classe evt
>>> for nome in nomes:
    primeiro, dentro de cada evt, vamos extrair a manchete, que fica na tag p e atributo elementtiming: text-ssr
    >>> titulo_completo = nome.find('p',attrs={'elementtiming':'text-ssr'})
    >>> titulo = titulo_completo.text

    depois, vamos extrair o link, que fica na linha da tag/atributo abaixo:
    >>> html_link = nome.find('a',attrs={'class':'feed-post-link'})
    pra acessar um atributo, vc pega a linha dele (identificada acima) e procura pelo atributo dentro do []
    >>> link = html_link["href"]

__________________________________________________________________________________________
5) BUSCA AUTOMATIZADA POR PRODUTOS (é um caso prático da aula 4)
Outro exemplo: buscar o link de todas as bolas do mercado livre    
>>> produto_a_procurar = 'bola'
>>> requisicao = requests.get(f"https://lista.mercadolivre.com.br/{produto_a_procurar}")
>>> conteudo = requisicao.content
>>> site = BeautifulSoup(conteudo,'html.parser')
Essa é a parte mais importante, tive que testar algumas vezes pra achar a classe apropriada
>>> html_resultado_todos = site.findAll('a',attrs={'class':'ui-search-item__group__element ui-search-link__title-card ui-search-link'})
>>> for html_resultado in html_resultado_todos:
>>>     link = html_resultado['href']

De um modo geral, percebo que é essencial entender a estrutura do HTML, há tags pais-filhos, há atributos agrupados nas tags

__________________________________________________________________________________________
6) SELENIUM

options = Options()
# options.add_argument('--headless')    # o navegador fica minimizado ao executar
options.add_argument('windows-size=400,800')
# abrir o navegador
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
#Esse By é uma forma de procurar os atributos: CLASS_NAME, CSS_SELECTOR, ID, TAG_NAME, etc
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests
from time import sleep
import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
'''
Como fazer uma lista com o nome das jogadoras e a fração de pontos/set:
navegador = webdriver.Chrome()
# com o navegador, acessar o site
navegador.get('https://cbv-web.dataproject.com/BestPlayerRankingComplete.aspx?ID=18&rt=1')
sleep(2)
site = BeautifulSoup(navegador.page_source,'html.parser')

def extrair_nomes_numeros(lista_jogadoras,lista_numeros_sets):
    nomes = navegador.find_elements(By.CLASS_NAME,'Ranking_PlayerName')
    for nome in nomes:
        lista_jogadoras.append(nome.text)

    numeros = navegador.find_elements(By.CLASS_NAME,'Ranking_PlayerData')
    for numero in numeros:
        lista_numeros_sets.append(numero.text)
    
    return lista_jogadoras,lista_numeros_sets

______________________________________________________________________________________________
como copiar a tabela toda e clicar nos botões que ficam em cima:

driver = webdriver.Chrome()
# com o navegador, acessar o site
driver.get('https://cbv-web.dataproject.com/BestPlayerRankingComplete.aspx?ID=18&rt=1')
driver.implicitly_wait(0.5)

tabela = driver.find_element(by=By.CSS_SELECTOR, value="#Content_Main_DIV_RankingWrapper > div:nth-child(4)")
O # acima significa selecionar o id = Content_Main_DIV_RankingWrapper. O > significa selecionar os filhos diretos. 
O div é um seletor de tipo (seleciona apenas as tags <div>), e nth-child(4) seleciona o 4º filho do elemento pai
print(tabela.text)

list_header = driver.find_element(by=By.CSS_SELECTOR, value="div.rdpWrap.rdpNumPart")
page_2 = list_header.find_element(by=By.LINK_TEXT, value="2")
page_2.click()

tabela = driver.find_element(by=By.CSS_SELECTOR, value="#Content_Main_DIV_RankingWrapper > div:nth-child(4)")
print(tabela.text)

#ctl00_Content_Main_LV_Ranking_RDP2 > div.rdpWrap.rdpNumPart

driver.quit()'''

    
#df = pd.DataFrame(lista)
#print(df.loc[10:20,0])

'''
_______________________________________________________________________________________________________

Um outro conceito super importante é o CSS, sigla de folha de estilo cascata (Cascading Style Sheets), usada pra personalizar o estilo duma pagina web
Por padrão, o HTML básico é padrão, com fonte padrão (tipo e cor), fundo branco, com parágrafos (pelo h1,...h6), etc.
O CSS não é uma linguagem de programação, nem de marcação (igual o HTML), é apenas uma linguagem de folhas de estilos.

A regra do CSS consiste emum seletor e um bloco de declaração, conforme o padrão:
>>> p {color:red;}
>>>     p = selector
>>>     {color:blue} = declaração
>>>     color: nome da propriedade
>>>     red: valor da propriedade
O seletor pontua o elemento do HTML a ser personalizado
O nome da propriedade é a forma como vc vai personalizar um elemento HTML. No caso acima, color é uma propriedade dos elementos <p>
É possível ter vários pares de nome propriedade e valor propriedade numa mesma declaração

É possível também selecionar vários tipos de elementos e aplicar um mesmo conjunto de regras a todos eles. Basta separar os elementos por vírgula:
>>> p,li,h1 {color: red;}

Seletores CSS são usado pra ENCONTRAR/SELECIONAR os elementos HTML que vc quer estilizar.
Exemplos de seletores:
    id: geralmente é único por página. P/ selecionar pelo id, use # + nome id
    classe: . + nome da classe
    atributo: ex img[src] seleciona <img src="myimage.png">
    universal: seleciona todos os elementos HTML de uma página. Símbolo: *

No Selenium vc pode usar driver.findElement(By.CSS_SELECTOR("forma"))
Lembre de que o caminho da classe não pode ter espaços, coloque ponto final no lugar
É comum ter um <div classe = " " outro_atributo = "valor"
Nesse caso, faça:
>>> div."nome.classe"["outro_atributo"="valor"]
Exemplos:
https://www.browserstack.com/guide/css-selectors-in-selenium 

servico = Service(ChromeDriverManager().install())
webdriver.Chrome(service=servico)

Extrair o título dos anúncios do airbnb:
driver = webdriver.Chrome()
url=r"https://www.airbnb.com.br/s/S%C3%A3o-Paulo-~-S%C3%A3o-Paulo--Brasil/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2024-05-01&monthly_length=3&monthly_end_date=2024-08-01&price_filter_input_type=0&channel=EXPLORE&query=S%C3%A3o%20Paulo%20-%20S%C3%A3o%20Paulo&place_id=ChIJ9cXwmIFEzpQR7-ebZCySXMo&date_picker_type=calendar&checkin=2024-06-19&checkout=2024-06-24&source=structured_search_input_header&search_type=autocomplete_click"
driver.get(url)
driver.implicitly_wait(5)
x = driver.find_elements(By.CSS_SELECTOR, "div.t1jojoys.atm_g3_1kw7nm4.atm_ks_15vqwwr.atm_sq_1l2sidv.atm_9s_cj1kg8.atm_6w_1e54zos.atm_fy_1vgr820.atm_7l_jt7fhx.atm_cs_9dzvea.atm_w4_1eetg7c.atm_ks_zryt35__1rgatj2.dir.dir-ltr[data-testid=listing-card-title]")

lista = []
for i in x:
    lista.append(str(i.text))
print(lista)



'''