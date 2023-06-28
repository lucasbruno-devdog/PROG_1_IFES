
def main():
   
   palavra_um = input()
   palavra_dois = input()
   
   if(len(palavra_um) == len(palavra_dois)):
       print("MESMO TAMANHO")
   else:
       print("TAMANHO DIFERENTE")
   if(palavra_um == palavra_dois):
       print("CONTEÚDO IGUAL")
   else:
       print("CONTEÚDO DIFERENTE")
          
           
   return 0


if __name__ == "__main__":
  main()
