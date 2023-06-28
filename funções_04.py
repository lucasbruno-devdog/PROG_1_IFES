import math
def tamanho(num):
   cont = 0
   while (num > 0):
       cont+=1
       num = num // 10
   return cont
    
def main():
    
    num = int(input())
    print(tamanho(num))
 
    return 0

if __name__ == "__main__":
  main()