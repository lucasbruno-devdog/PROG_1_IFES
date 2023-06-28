def main():
   
   frase = input()
   espaços = 0
   a = 0
   e = 0
   i = 0 
   o = 0
   u = 0
   l = 0
   
   for l in range(len(frase)):
       if(frase[l] == " "):
           espaços += 1
       elif(frase[l].upper() == "A"):
           a += 1
       elif(frase[l].upper() == "E"):
           e += 1
       elif(frase[l].upper() == "I"):
           i += 1
       elif(frase[l].upper() == "O"):
           o += 1
       elif(frase[l].upper() == "U"):
           u += 1
    
   print(f'ESPAÇOS EM BRANCO= {espaços}')
   print(f'A= {a}')
   print(f'E= {e}')
   print(f'I= {i}')
   print(f'O= {o}')
   print(f'U= {u}')       
                              
   return 0


if __name__ == "__main__":
  main()
