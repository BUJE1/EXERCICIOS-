import json
import os

filmes = "cadastro_filmes.json"
def carregar_dados ():
    if os.path.exists(filmes):
        with open(filmes, "r", encoding="utf-8")as arq_jason:
            return json.load(arq_jason)
    else:
        return[]
                             
def obter_dados():
    nome = input("informe o nome do filme: ")
    classificacao = int(input("digite a classifcação indicativa do seu filme: "))
    descricao = input("fale a descrição do filme: ")
    categoria = input("fale a categoria do filme: ")

    data_filme = {
        "nome" : nome,
        "classificacao" : classificacao,
        "descricao" : descricao,
        "categoria" : categoria
    }
    return data_filme
def cadastar_filme(receber_filme):
    db_filmes = carregar_dados()
    db_filmes.append(receber_filme)

    with open(filmes, "w", encoding= "utf-8")as arq_json:
        json.dump(db_filmes, arq_json, indent=4, ensure_ascii= False)

def mostar_filmes(filmes):
    if filmes:
        for filme in filmes:
            print(f"""
                  Nome do Filme{filme["nome"]}
                  Classificação do Filme{filme["classificacao"]}
                  Descrição do Filme{filme["descricao"]}
                  Categoria do Filme{filme["categoria"]}
                  """)
    else:
        print("Não Existe Filme Cadastrado")

def iniciar_sistema():
    db_filmes = carregar_dados()

    while True:
        print("")
        print("="*80)
        print("opcão1 => Mostar filmes cadastrados.")
        print("opcão2 => cadastrar filmes.")
        print("opcão3 => sair do sistema.")
        print("="*80)

        opcao = input("Escolha uma Opção:")

        if opcao =="1":
            mostar_filmes(db_filmes)
        elif opcao == "2":
            print(obter_dados())
        elif opcao == "3":
            print("Sistema Finalizado!!")
            break
        else:
            print("Escolha umas das opções acima.")
            

iniciar_sistema()





