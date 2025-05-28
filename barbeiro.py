import json
import os 

clientes = "cadastro_barbeiro.json"

def carregar_dados():
    if os.path.exists(clientes):
        with open(clientes, "r", encoding="utf-8")as arq_json:
            return json.load(arq_json)
    else:
        return[]
    
def obter_dados():
    nome = input("Digite seu nome: ")
    serviço = input("Qual vai ser seu serviço: ")
    data = input("O dia que voce deseja o serviço: ")
    horario = int(input("Digite o horario disponivel: "))
    observacoes = input("Digite uma observação de serviço de houver: ")

    data_cliente = {
        nome : "nome",
        serviço : "serviço",
        data : "data",
        horario : "horario",
        observacoes : "observacoes"
    }
    return data_cliente
def cadastar_cliente(receber_clientes):
    db_clientes = carregar_dados()
    db_clientes.append(receber_clientes)

    with open(clientes, "w", encoding="utf-8")as arq_json:
        json.dump(db_clientes, arq_json, indent=4, ensure_ascii= False)

def mostrar_agendamentos(clientes):
    if clientes:
        for cliente in clientes:
            print(f"""
                Nome do cliente{cliente["nome"]}
                Serviço do cliente{cliente["serviço"]}
                Data do serviço{cliente["data"]}
                Horario marcado{cliente["horario"]}
                Observações de servoço{cliente["observacoes"]}
                 """ )
    else:
            print("Cliente Não encontrado")

def iniciar_sistema():
    db_clientes = carregar_dados()

    while True:
        print("")
        print("="*80)
        print("opcão1 => Mostar clientes marcados.")
        print("opcão2 => cadastrar cliente.")
        print("opcão3 => sair do sistema.")
        print("="*80)

        opcao = input("Escolha umas das opções: ")

        if opcao == "1":
            mostrar_agendamentos(db_clientes)
        elif opcao == "2":
            cadastar_cliente(obter_dados())
        elif opcao == "3":
            print("Sistema finalizado.")
            break
        else:
            print("Escolha alguma das opções acima")


iniciar_sistema()

    


