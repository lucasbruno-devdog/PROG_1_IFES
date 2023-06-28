import math
def main():
  
  idade = 1
  cont = 0
  total_idade = 0
  media_idade = 0


  while(idade != 0):
    idade = int(input()) 
    if(idade == 0):
      break

    cont += 1  
    total_idade += idade

  media_idade = total_idade/cont 

  print(f'{media_idade:.1f}') 

  return 0


if __name__ == "__main__":
  main()
