def main():
  
  choice = input()
  
  if(choice == ["S" or choice == "N"]):
     print("RESPOSTA CORRETA")

  while(choice != "S" and choice != "N"):
     print("RESPOSTA INCORRETA, DIGITE S OU N")
     choice = input()
     
     if(choice == "S" or choice == "N"):
      print("RESPOSTA CORRETA")
  
           
  return 0


if __name__ == "__main__":
  main()
