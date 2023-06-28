def main():

  numero_turmas = int(input())

  ausencia_maior = 0 
  ausencia_menor = 1000
  turma_ausencia_sup = 0
  turma_maior_ausencia = ""
  turma_menor_ausencia = ""  

 
  for i in range(1, numero_turmas + 1):
    turma_id = input()
    quantidade_alunos = int(input())

    ausencia = 0

    for o in range(1, quantidade_alunos + 1): 
     matricula_aluno = input()
     frequencia_aluno = input()
     if(frequencia_aluno == "A"):
        ausencia += 1

    ausencia_percent = (ausencia/quantidade_alunos)*100

    print(f'TURMA={turma_id} AUSENCIA= {ausencia_percent:.2f} %')

    if(ausencia_percent > ausencia_maior):
        ausencia_maior = ausencia_percent
        turma_maior_ausencia = turma_id

    elif(ausencia_percent < ausencia_menor):
        ausencia_menor = ausencia_percent
        turma_menor_ausencia = turma_id

    if(ausencia_percent > 20):
        turma_ausencia_sup += 1

#-------------------------------------------------------------------#    

  print(f'TURMA COM MAIOR % DE AUSENCIA= {turma_maior_ausencia} AUSENCIA= {ausencia_maior:.2f}%')
  print(f'TURMA COM MENOR % DE AUSENCIA= {turma_menor_ausencia} AUSENCIA= {ausencia_menor:.2f}%')
  print(f'{turma_ausencia_sup} TURMAS COM % DE AUSENCIA SUPERIOR A 20%')     

  return 0


if __name__ == "__main__":
  main()
