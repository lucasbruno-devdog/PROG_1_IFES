import math
def soma(num_1, num_2, num_3):
   resultado = (num_1 + num_2 + num_3)
   
   return resultado
    
def main():
    
    num_1 = int(input())
    num_2 = int(input())
    num_3 = int(input())
    resultado = soma(num_1, num_2, num_3)
    print(resultado)
 
    return 0

if __name__ == "__main__":
  main()