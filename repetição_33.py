import math
def existente(palavra, letra):
    for i in range(len(palavra)):
        if(palavra[i] == letra):
            return True
    return False    

def main():
    letra_existente = True
    palavra = input().upper()
    letra = input().upper()
    
    while(existente(palavra, letra)):
        print("LETRA EXISTENTE, DIGITE OUTRA")
        letra = input().upper()
    print("LETRA INEXISTENTE")
    palavra += letra
    print(palavra)    
 
 
    return 0

if __name__ == "__main__":
  main()
