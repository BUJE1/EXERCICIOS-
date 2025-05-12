from exercicio04 import somar

def adicionar_aluno(nome, email, serie, nota1=0, nota2=0, nota3=0):
    lista_alunos = []
    notas = [nota1, nota2, nota3]
    aluno = {
        'nome': nome,
        'email': email,
        'serie': serie,
        "lista_notas": [nota1, nota2, nota3],
        'media': somar([nota1, nota2, nota3])
    }

    lista_alunos.append(aluno)
    media = somar(aluno["lista_notas"])
    return lista_alunos

print(adicionar_aluno("matheus", "matheus@g.com", "2 TB", 9, 8, 2))
