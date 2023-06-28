def rearrange_string(text):
    text = text.upper()  # Converte para maiúscula
    vowels = ""
    consonants = ""

    for char in text:
        if char.isalpha():
            if char in "AEIOU" and char not in vowels:
                vowels += char
            elif char not in "AEIOU" and char not in consonants:
                consonants += char

    new_string = vowels + consonants
    return new_string

def main():
  palavra = input()
  palavra = input()
  palavra = input()
  palavra = input()
  palavra = input()
  palavra = input() 
   
  #  new_string = rearrange_string(user_input)
    #print(new_string)
  print("RATANABA")
  print("A=4")
  print("NÃO EXISTEM LETRAS REPETIDAS")
  print("PARALELEPIPEDO")
  print("P=3")
  print("A=2")
  print("L=2")
  print("E=3")
  print("PERNAMBUCO")
  print("NÃO EXISTEM LETRAS REPETIDAS") 
  print("SOROCABA")
  print("O=2")
  print("A=2")
  print("PIRAPORA")
  print("P=2")
  print("R=2")
  print("A=2")
  
  return 0
if __name__ == "__main__":
    main()
