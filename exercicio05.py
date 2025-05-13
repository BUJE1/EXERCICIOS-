from exercicio04 import somar
alunos= []

def obter_dados_aluno():
    nome = input("informe o nome completo completo do aluno: ")
    email = input("informe o email do aluno: ")
    serie = input("informe a serie do aluno: ")
    nota01 = int(input("informe a primeira nota do aluno: "))
    nota02 = int(input("informe a segunda do aluno: "))
    nota03 = int(input("informe a terceira nota do aluno: "))

    return adicionar_aluno(nome, email, serie, nota01, nota02, nota03)


def adicionar_aluno(nome, email, serie, nota01=0, nota02=0, nota03=0):
    notas = [nota01, nota02, nota03]
    aluno = {
        'nome': nome,
        'email': email,
        'serie': serie,
        "lista_notas": notas,
        'media': somar(notas)
    }

    alunos.append(aluno)

    return alunos


def mostrar_dados_alunos(dados_alunos):
    for aluno in dados_alunos:
        print(f"nome do aluno: {aluno["nome"]}")
        print(f"demail do aluno: {aluno["email"]}")
        print(f"serie do aluno: {aluno["serie"]}")
        print(f"notas do aluno: {aluno["lista_notas"]}")
        print(f"media do aluno: {aluno["media"]}")
    
    
    return 

def iniciar_sistema():
    while True:
        print("="*80)
        print("opcão1 => mostar lista de alunos cadastrados.")
        print("opcão2 => cadastrar alunos.")
        print("opcão3 => sair do sistema.")
        print("="*80)
        opcao = input("escolha uma das opções acima: ")
 
        if opcao == "1":
            mostrar_dados_alunos(alunos)
        elif opcao == "2":
            obter_dados_aluno()
        else:
            print("sistema finalizado")
            break
        

    
 
iniciar_sistema()       