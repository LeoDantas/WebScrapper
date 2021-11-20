# File name: wikipedia.py
# Authors: Leonardo Dantas & Rivanildo Silva dos Santos


import re # biblioteca para expressões regulares
import requests # biblioteca buscar o html de uma pag web
from bs4 import BeautifulSoup # biblioteca para extrair dados de uma página HTML

class Webscrapper:
    '''
    Classe que representa, de forma abstrata, um artigo da Wikipédia
    '''
    def __init__(self, link:str):
        
        self.link = link
        if not self.verifica_link():
            raise ValueError('O link inválido!')

    
    
    def verifica_link(self):

        expressao = re.compile(r'(pt.wikipedia.org)')
        if expressao.search(self.link) == None: # verifica se o endereço pt.wikipedia.org faz parte do link
            return False
        # verifica se o status code é 200, ja que indica sucesso ao acessar a pagina requisitada.
        elif requests.get(self.link, stream = False).status_code != 200:
            return False
        else:
            return True

    def list_indice(self):

        # buscar todas as tags html que possuem a class tocnumber e toctext, pois se tratam de indices     
        expressao = re.compile(r'(<span class="tocnumber">([0-9](.[0-9])*)</span> <span class="toctext">(.)+</span>)+')

        indice = expressao.findall(requests.get(self.link).text)
        indice_corrigido = []
        for x in indice:
            # trata o html que foi inserido e busca apenas o conteudo que esta entre >< (dentro da tag)
            indice_corrigido.append(x[0].split('>')[1].split('<')[0] + ' ' + x[0].split('>')[3].split('<')[0])
        return indice_corrigido        


    def list_images(self):

        # Buscar o html
        html = requests.get(self.link).text
        
        # Captura apenas o conteudo da div bodyContent
        bs_page = BeautifulSoup(html, 'html.parser').find(id="bodyContent")
        # Busca a imagem do inicio do site, pois esta numa class diferente
        expressao_image_title = re.compile(r'(<table (.)+ class="infobox infobox infobox_v2" (.)+>)+')
        #expressao_image_title = re.compile(r'(<div class="image">(.)+</div>)+')
        # Buscar as demais imagens com a class thumbimage
        expressao_images_body = re.compile(r'(<img (.)+ class="thumbimage" (.)+>)+')
        # Concatena as informações para usar a expressão regular.
        images = expressao_image_title.findall(str(bs_page)) + expressao_images_body.findall(str(bs_page))
        return images

            

    def list_links(self):
   
        # Buscar o html
        html = requests.get(self.link).text
        # Captura apenas o conteudo da div bodyContent
        bs_page = BeautifulSoup(html, 'html.parser').find(id="bodyContent")
        # Monta a expressao regular
        expressao = re.compile(r'(<a href="/wiki/(.)+)+')
        
        links = expressao.findall(str(bs_page))
        return links

   