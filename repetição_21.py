def main():
   
   decision = "s"

   while(decision.lower == "s"):
      a = float(input())
      b = float(input())
      
      choice = int(input())
   
      if(choice == 1):
        resultado = a + b
        print(resultado)
            
      elif(choice == 2):
        resultado = a - b
        print(resultado)
      
      elif(choice == 3):
        resultado = a * b
        print(resultado)
        
      elif(choice == 4):
        resultado = a / b
        print(resultado)
        
      elif(choice == 5):
        resultado = a**b
        print(resultado)
        
      elif(choice == 6):  
        resultado = a ** (1 / b)
        print(resultado)  
          
      else:
           print("OPERACAO INVALIDA")
           
      decision = input()     
           
      return 0


if __name__ == "__main__":
  main()
