# File name: main.py
# Authors: Leonardo Dantas & Rivanildo Silva dos Santos

from webscrapper import Webscrapper # importando o objeto que representa um artigo da Wikipédia

while True:
    try:
        print("----- Web Scrapper: Wikipédia -----")

        link = input("\nInforme o link do artigo\n--->")
        artigo = Webscrapper(link)

        print("\nLink verificado!!")

        while True:
            print("\n----- Escolha uma opção -----")
            print("1 - Listar os tópicos do índice do artigo")
            print("2 - Listas todos os nomes de arquivos de imagens presentes no artigo")
            print("3 - Listar os links para outros artigos da Wikipédia que são citados no conteúdo do artigo")
            print("0 - Encerrar Programa")
            opcao = input("Informe a opção desejada\n--->")
            # Exibe o índice do artigo informado
            if opcao == '1':
                for index in artigo.list_indice():
                    print(index)
            # Exibe o nome dos arquivos de imagem presentes no corpo do artigo
            elif opcao == '2':
                index = 1
                for img in artigo.list_images():
                    img1 = img[0].split("src")[1].split("/")[-2]
                    img2 = img[0].split("src")
                    img3 = img[0].split("src")[1]
                    img4 = img[0].split("src")[1].split("/")
                    print('{}. {}'.format(index, img[0].split("src")[1].split("/")[-2]))
                    index += 1
            # Exibe a listagem dos links para outros artigos da Wikipédia presentes no artigo
            elif opcao == '3':
                index = 1
                for link in artigo.list_links():
                    link_formatado = link[0].split('"')
                    print(str(index) + ". " + link_formatado[3] + ": "+ "https://pt.wikipedia.org" + link_formatado[1])
                    index += 1
            # Encerra a aplicação
            elif opcao == '0':
                print("Programa Encerrado!")
                break
            else:
                print("Opção inválida, favor selecionar uma opção válida!")
        break
    # Trata a excessão ValueError: invocada quando o usuário passa um link que não é válido
    except ValueError:
        print("\n\nLink Inválido, favor inserir um link de uma página pertencente ao domínio pt.wikipedia.org\n\n")
