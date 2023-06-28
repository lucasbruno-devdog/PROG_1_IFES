def f_sublinhado(s):
    sub = ""
    for i in range(len(s)):
        sub += "_"
    return sub

def f_imprime(s):
    for i in range(len(s)):
        print(s[i],end=" ")
    print()

def f_imprime2(s):
    for i in range(len(s)):
        print(s[i],end="")
    print()

def main():
    cont = 0
    jogando = True
    erradas = ""
    erros = 0
    s = input().upper()
    
    sublinhado = f_sublinhado(s)
    f_imprime(sublinhado)
    while (jogando and erros < 6):
        cont += 1
        errou = True
        nova = ""
        letra = input().upper()
        for i in range(len(s)):
            if (s[i] == letra):
                errou = False
                nova += letra
            else:
                nova += sublinhado[i]
    sublinhado = nova
    if (errou):
        erros += 1
        erradas += letra
    if (sublinhado == s):
        jogando = False
    f_imprime(nova)
    f_imprime2(erradas)
    if (erros == 6):
        print(f'Que pena, você não acertou a palavra {s}')
    else:
        print(f'Parabéns, você ganhou com {cont} jogadas')
        
    return 0
if __name__ == "__main__":
    main()