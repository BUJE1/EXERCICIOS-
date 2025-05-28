import json
import os
veiculos = "cadastro_veiculos.json" 
def carregar_dados():
    if os.path.exists(veiculos):
        with open(veiculos, "r", encoding="utf-8") as arq_json:
            return json.load(arq_json)
    else:
        return[]
    
def obter_dados():
    modelo = input("digite o modelo do veiculo: ")
    ano = int(input("digite o ano do seu veiculo: "))
    placa = input("digite a placa do veiculo: ")
    marca = input("digite o marca do seu veiculo: ")
    cor = input("digite a cor do veiculo: ")

    data_veiculo = {
        "modelo" : modelo,
        "ano" : ano,
        "placa" : placa,
        "marca" : marca,
        "cor" : cor

    }
    return data_veiculo
def cadastra_veiculo(receber_veiculo):
    db_veiculos = carregar_dados()
    db_veiculos.append(receber_veiculo)

    with open(veiculos, "w", encoding="utf-8")as arq_json:
        json.dump(db_veiculos, arq_json, indent=4, ensure_ascii=False)

def mostar_veiculos(veiculos):
    if veiculos:
        for veiculo in veiculos:
            print(f"""
                  Modelo do veiculo {veiculo["modelo"]}
                  Ano do veiculo {veiculo["ano"]}
                  Placa do veiculo {veiculo["placa"]}
                  Marca do veiculo {veiculo["marca"]}
                  Cor do veiculo {veiculo["cor"]}
                f""")
    else:
        print("Não existe veiculo cadastrado")
def iniciar_sistema():
    db_veiculos = carregar_dados()

    while True:
        print("")
        print("="*80)
        print("opcão1 => Mostar veiculos cadastrados.")
        print("opcão2 => cadastrar veiculos.")
        print("opcão3 => sair do sistema.")
        print("="*80)

        opcao = input("Escolha uma Opção:")
        if opcao =="1":
            mostar_veiculos(db_veiculos)
        elif opcao == "2":
            cadastra_veiculo(obter_dados())
        elif opcao == "3":
            print("Sistema Finalizado!!")
            break
        else:
            print("Escolha umas das opções acima.")

iniciar_sistema()

    

    
