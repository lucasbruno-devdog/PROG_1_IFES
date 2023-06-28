def main():
   
   nome = input().upper()
   letra = nome
   i = 1
   
   for letra in nome:
       print(nome[:i])
       i += 1           
           
   return 0


if __name__ == "__main__":
  main()
