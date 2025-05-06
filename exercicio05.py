def adicionar_aluno(nome, email, serie, nota1, nota2, nota3):
    lista_alunos = []
    aluno = {
        'nome': nome,
        'email': email,
        'serie': serie,
        "lista_notas": [nota1, nota2, nota3]
    }

    lista_alunos.append(aluno)
    return lista_alunos

print(adicionar_aluno("matheus", "matheus@g.com", "2 TB", nota1, nota2, nota3))
