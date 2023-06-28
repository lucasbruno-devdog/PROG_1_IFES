import math
def tipo(num_1):
   if(num_1 > 0):
      resultado = print("P")
   elif(num_1 < 0):
      resultado = print("N")
   elif(num_1 == 0):
      resultado = print("Z")        
   
   return resultado
    
def main():
    
    num_1 = float(input())
    resultado = tipo(num_1)
 
    return 0

if __name__ == "__main__":
  main()
