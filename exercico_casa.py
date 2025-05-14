clientes = []

def obter_dados_clientes():
    nome = input("informe o nome completo completo do aluno: ")
    cpf = int(input("informe o seu CPF: "))
    rg = int(input("informe o seu RG: "))
    nacimento = input("informe a sua data de nascimento: ")
    endereco = input("informe o seu endreço: ")
    cidade = input("informe a sua cidade: ")
    estado = input("informe o estado: ")
    telefone = int(input("informe o seu telefone: "))
    celular = int(input("informe o seu celular: "))
    email = input("informe o seu email: ")

    return adicionar_cliente(obter_dados_clientes)

def adicionar_cliente(nome, cpf, rg, nascimento, endereço, cidade, estado, telefone, celular, email):
    cliente = {
      'nome' :  nome,
      "cpf" : cpf,
      "rg" : rg,
      "nascimento" : nascimento,
      "endereco" : endereço,
      "cidade" : cidade,
      "estado" : estado,
      "telefone" : telefone,
      "celular" : celular,
      "email"  : email
    }
    
    clientes.append
    return clientes

def mostar_dados_clientes(dados_clientes):
    for cliente in dados_clientes:
        print(f"nome do cliente: {cliente["nome"]}")
        print(f"cpf do cliente: {cliente["cpf"]}")
        print(f"rg do cliente: {cliente["rg"]}")
        print(f"nascimento do cliente: {cliente["nascimento"]}")
        print(f"endereço do cliente: {cliente["endereco"]}")
        print(f"cidade do cliente: {cliente["cidade"]}")
        print(f"estado do cliente: {cliente["estado"]}")
        print(f"telefone do cliente: {cliente["telefone"]}")
        print(f"celular do cliente: {cliente["celular"]}")
        print(f"email do cliente: {cliente["email"]}")

        return
    
def iniciar_sistema(): 
    while True:
        print("="*80)
        print("opcão1 => mostar lista de alunos cadastrados.")
        print("opcão2 => cadastrar alunos.")
        print("opcão3 => sair do sistema.")
        print("="*80)
        opcao = input("escolha uma das opções acima: ")

        if opcao == '1':
            print(mostar_dados_clientes)
        elif opcao == '2':
            print(obter_dados_clientes)
        else:
            print("finalizado")
            break

iniciar_sistema()



        




      
      
       







