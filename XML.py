import os
import xml.etree.ElementTree as ET
import pandas as pd

# biblioteca xml.etree.ElementTree examina arquivos de extensão xml, e por convenção é apelidado de ET

'''
    SOBRE ARQUIVO XML:
        XML tem formato hierárquico e é tratado como uma árvore.
        
        XML tem sessões, chamadas elements, definidas por uma tag de início de fim.
        Uma tag é uma marcação de construtor que se inicia com < e termina com >. O conteúdo entre cada < > é chamado de conteudo do elemento.
        Elementos podem ter elemenos filhos.
        O elemento mais alto é chamado root, e contém todos os demais elementos.

        Atributos são pares de nomes-valores que existem nas tags. Uma tag pode contar ATÉ um atributo (nome-valor)


        O ET tem as classes 
            - ElementTree, que representa o XML todo como uma árvore 
            - Element, que representa nós da árvore (elementos do XML)


        https://mjamilmoughal.medium.com/working-with-xml-using-python-933e39598581
        https://docs.python.org/3/library/xml.etree.elementtree.html

'''
pasta_xml = r"C:\Users\bserpellone\Documents\Projetos\Nutrien\Arquivos_da_Nutrien_(DTi)\compilado_xmls\35221203860998000435550100000288601581634500-nfe.xml"
#pasta_xml = r"C:\Users\bserpellone\Desktop\Python\Teoria\países.xml"

# transforma o XML num objeto ElementTree
tree = ET.parse(pasta_xml)
# extrai a raiz do objeto ElementTree
root = tree.getroot()
for filhos in root.iter():
    if filhos.tag.endswith('vProd'):
        print(filhos.tag, filhos.text)



