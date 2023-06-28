def main():
  
  choice = input()
  
  if(choice == "m" or choice == "f"):
     print("SEXO VÁLIDO")

  while(choice != "m" and choice != "f"):
     print("SEXO INVÁLIDO, DIGITE F OU M")
     choice = input()
     
     if(choice == "m" or choice == "f"):
      print("SEXO VÁLIDO")
  
           
    #return 0


if __name__ == "__main__":
  main()
