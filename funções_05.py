import math
def tamanho(num):
   cont = 0
   while (num > 0):
       cont+=1
       num = num // 10
   return cont

def reverso(num):
   reverso_var = 0
   potencia = tamanho(num) - 1
   while(num > 0):
       res = num % 10
       reverso_var += res * 10 ** potencia
       potencia -= 1
       num = num // 10         
   return reverso_var
    
def main():
    
    num = int(input())
    print(reverso(num))
 
    return 0

if __name__ == "__main__":
  main() 