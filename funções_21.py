def remove_vogais(texto):
    vogais = "AEIOU"
    novo_texto = ""

    for letra in texto:
        letra = letra.upper()
        if letra not in vogais:
            novo_texto += letra

    return novo_texto

def main():
    while True:
        palavra = input()
        if palavra == "":
            break

        nova_palavra = remove_vogais(palavra)
        print(nova_palavra)
            
    return 0

if __name__ == "__main__":
    main()
