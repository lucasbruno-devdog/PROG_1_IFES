def f_removerEspaços(palavra):
   nova = ""
   for i in range(len(palavra)):
      if(palavra[i] != " "):
         nova = nova + palavra[i]
   return nova         

def main():
   
   palavra = input()
   palavra2 = f_removerEspaços(palavra)
   
   if(palavra2 == palavra2[::-1]):
    print("É PALÍNDROMO")
   else:
    print("NÃO É PALÍNDROMO")
    
   #neo_palavra = palavra[::-1].replace(" ", "")
   #nova_palavra = palavra.replace(" ", "")    
          
   #if(neo_palavra == nova_palavra):
    #print("É PALÍNDROMO")
   #else:
    #print("NÃO É PALÍNDROMO")               
           
   return 0 

if __name__ == "__main__":
  main()

