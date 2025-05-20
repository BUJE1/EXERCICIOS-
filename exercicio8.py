import json
import os

funcionarios = "funcionarios.json" 
def carregar_dados():
    if os.path.exists(funcionarios):
        with open(funcionarios, "r", encoding="utf-8") as arq_json:
          return json.load(arq_json) 
    else :
       return[]
    
funcionarios = carregar_dados()
for funcionario in funcionarios:
   if funcionario["salario"] >= 5500:
    print(f"nome do funcionario: {funcionario["nome"]}, salario do funcionario: {funcionario["salario"]}")
   else:
      print("funcionarios não encontrado")



