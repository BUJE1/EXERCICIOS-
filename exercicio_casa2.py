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

    cliente = {
        "nome": nome,
        "cpf": cpf,
        "rg": rg,
        "nascimento": nacimento,
        "endereco" : endereco,
        "cidade": cidade,
        "estado": estado,
        "telefone" : telefone,
        "celular" : celular,
        "email" : email

     }
    return cliente

def cadastar_cliente(dados_cliente):
    clientes.append(dados_cliente)

    return clientes

def mostrar_dados_clientes(dados_cliente):
 for cliente in dados_cliente:
    print(f"""
        nome do cliente: {cliente["nome"]}
        cpf do cliente: {cliente["cpf"]}
        rg do cliente: {cliente["rg"]}
        nascimento do cliente: {cliente["nascimento"]}
        endereço do cliente: {cliente["endereco"]}
        cidade do cliente: {cliente["cidade"]}
        estado do cliente: {cliente["estado"]}
        telefone do cliente: {cliente["telefone"]}
        celular do cliente: {cliente["celular"]}
        email do cliente: {cliente["email"]}

          
         """ )
    
def iniciar_sistema():
   while True:
        print("")
        print("="*80)
        print("opcão1 => mostar lista de alunos cadastrados.")
        print("opcão2 => cadastrar alunos.")
        print("opcão3 => sair do sistema.")
        print("="*80)

        opcao = input("escolha uma das opções acima: ")

        if opcao == "1":
           mostrar_dados_clientes(clientes)
        elif opcao == "2":
           cadastar_cliente(obter_dados_clientes())
        elif opcao == "3":
           print("sistema finalizado!")
           break
        else:
           print("opcão invalida")

   

iniciar_sistema()