def main():
   
   palavra = input().upper()
   nova_palavra = ""
   #print(palavra[::-1])       
   
   i = len(palavra) - 1
   
   while (i >=0 ):
        nova_palavra = nova_palavra + palavra[i]
        #print(palavra[i], end="")
        i = i - 1
        
   print()
   print(nova_palavra)            
           
   return 0


if __name__ == "__main__":
  main()

