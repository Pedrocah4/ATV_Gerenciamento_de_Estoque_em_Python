# Registrar duas entradas de livros (título, gênero e quantidade);
# Definir um número mínimo de exemplares permitidos por gênero, utilizando constantes;
# Calcular o total de livros em estoque em uma variável;
# Exibir a porcentagem do estoque disponível por gênero no terminal;


print("SEJA BEM VINDO!")
# Constantes
MIN_FICCAO = 4
MIN_RELIGIOSO = 5
MIN_ROMANCE = 2
MIN_DRAMA = 3

# Variáveis
total_de_livros = 0
cont_ficcao = 0
cont_religioso = 0
cont_romance = 0
cont_drama = 0


# Lista de livros
livros = [
    # Exemplo de livro: {"titulo": "Diario de um banana", "genero": "comedia", "quantidade": 10}
    {"titulo": "Senhor dos aneis", "genero": "Ficção", "quantidade": 2},
    {"titulo": "Biblia", "genero": "Religioso", "quantidade": 1},
    {"titulo": "Frankenstein", "genero": "Ficção", "quantidade": 3},
    {"titulo": "Dom Casmurro", "genero": "Romance", "quantidade": 4},
    {"titulo": "Romeu e Julieta", "genero": "Drama", "quantidade": 2},
    {"titulo": "Harry Potter", "genero": "Ficção", "quantidade": 6},
    {"titulo": "Alcorão", "genero": "Religioso", "quantidade": 3},
    {"titulo": "Hamlet", "genero": "Drama", "quantidade": 1}

]
#for i in livros:
#    print(i)
registrando = True
while (registrando):
    #verificar se algum gênero está abaixo do mínimo

    cont_ficcao, cont_religioso, cont_romance, cont_drama = 0, 0, 0, 0
    for i in livros:
        if (i["genero"] == "Ficção"):
            cont_ficcao += i["quantidade"]
        elif (i["genero"] == "Religioso"):
            cont_religioso += i["quantidade"]
        elif (i["genero"] == "Romance"):
            cont_romance += i["quantidade"]
        elif (i["genero"] == "Drama"):
            cont_drama += i["quantidade"]    
    #verificar se algum gênero está abaixo do mínimo
    if (cont_ficcao < MIN_FICCAO):
        print(f"ATENÇÃO: O estoque de livros do gênero Ficção está abaixo do mínimo ({MIN_FICCAO}). Estoque atual: {cont_ficcao}")
    if (cont_religioso < MIN_RELIGIOSO):
        print(f"ATENÇÃO: O estoque de livros do gênero Religioso está abaixo do mínimo ({MIN_RELIGIOSO}). Estoque atual: {cont_religioso}")
    if (cont_romance < MIN_ROMANCE):
        print(f"ATENÇÃO: O estoque de livros do gênero Romance está abaixo do mínimo ({MIN_ROMANCE}). Estoque atual: {cont_romance}")
    if (cont_drama < MIN_DRAMA):
        print(f"ATENÇÃO: O estoque de livros do gênero Drama está abaixo do mínimo ({MIN_DRAMA}). Estoque atual: {cont_drama}")

    

    print("=====================================================")
    resposta = int(input(" ADICIONAR LIVRO: DIGITE 1 \n VER TOTAL DE LIVROS: DIGITE 2 \n VER PORCENTAGEM DE LIVROS: DIGITE 3 \n PARAR ATENDIMENTO: DIGITE 4 \n "))
    if (resposta == 1):
        titulo = input("Digite o título do livro: ")
        for i in livros:
            if (i["titulo"].lower() == titulo.lower()):#verifica se o livro já está cadastrado ignorando maiúsculas e minúsculas.
                print("Livro já cadastrado. Atualizando quantidade...")
                quantidade = int(input("Digite a quantidade de livros a ser adicionada: "))
                i["quantidade"] += quantidade
                print(f"Quantidade atualizada. Novo total de '{i['titulo']}': {i['quantidade']}")
                break
        else:
            genero = input("Digite o gênero do livro (Ficção, Religioso, Romance, Drama): ")
            quantidade = int(input("Digite a quantidade de livros: "))
            
            novo_livro = {"titulo": titulo, "genero": genero, "quantidade": quantidade}
            livros.append(novo_livro)
            print(f"Livro '{titulo}' adicionado com sucesso!")
        
    elif (resposta == 2):
        #calcular o total de livros
        total_de_livros = 0
        for i in livros:
            total_de_livros += i["quantidade"]
        print(f"O total de livros em estoque é: {total_de_livros}")
    elif (resposta == 3):
        cont_ficcao, cont_religioso, cont_romance, cont_drama = 0, 0, 0, 0
        for i in livros:
            if (i["genero"] == "Ficção"):
                cont_ficcao += i["quantidade"]
            elif (i["genero"] == "Religioso"):
                cont_religioso += i["quantidade"]
            elif (i["genero"] == "Romance"):
                cont_romance += i["quantidade"]
            elif (i["genero"] == "Drama"):
                cont_drama += i["quantidade"]

        print(f"A porcentagem de livros de Ficção é: {(cont_ficcao/total_de_livros)*100:.2f}%")
        print(f"A porcentagem de livros de Drama é: {(cont_drama/total_de_livros)*100:.2f}%")
        print(f"A porcentagem de livros de Religião é: {(cont_religioso/total_de_livros)*100:.2f}%")
        print(f"A porcentagem de livros de Romance é: {(cont_romance/total_de_livros)*100:.2f}%")

    elif (resposta == 4):
        registrando = False
    else:
        print("OPÇÃO INVÁLIDA.")
        registrando = False
    print("=====================================================")
print("LISTA DE LIVROS EM ESTOQUE:")
for i in livros:
    print(i["titulo"])
print("ATENDIMENTO FINALIZADO.")

# Fim do programa