def main():
   
   data = input()
   dia = data[:2]
   mes = int(data[3:5])
   ano = data[6:]
   
   if(mes == 1):
    nmes = "janeiro"
   elif(mes == 2):
    nmes = "fevereiro"
   elif(mes == 3):
    nmes = "março"   
   elif(mes == 4):
    nmes = "abril"
   elif(mes == 5):
    nmes = "maio"
   elif(mes == 6):
    nmes = "junho"
   elif(mes == 7):
    nmes = "julho"
   elif(mes == 8):
    nmes = "agosto"
   elif(mes == 9):
    nmes = "novembro"
   elif(mes == 10):
    nmes = "outubro"
   elif(mes == 11):
    nmes = "novembro"
   elif(mes == 12):
    nmes = "dezembro"
       
   print(f'{dia} de {nmes} de {ano}')
           
   return 0


if __name__ == "__main__":
  main()
