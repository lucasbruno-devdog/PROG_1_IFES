def main():
  
  choice = int(input())
  
  if(choice in [1, 2, 3, 4, 5, 6]):
     print("OPÇÃO VÁLIDA")
     

  while(choice < 1 or choice > 6):
     print("OPÇÃO INVÁLIDA. DIGITE UM VALOR DE 1 A 6")
     choice = int(input())
     
     if(choice in [1, 2, 3, 4, 5, 6]):
      print("OPÇÃO VÁLIDA")
       
           
  return 0


if __name__ == "__main__":
  main()
