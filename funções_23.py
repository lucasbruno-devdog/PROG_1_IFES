def gerar_nova_string(string):
    string = string.upper()
    vogais = ""
    consoantes = ""
    vogais_adicionadas = set()
    
    for char in string:
        if char in "AEIOU":
            if char not in vogais_adicionadas:
                vogais += char
                vogais_adicionadas.add(char)
        else:
            consoantes += char
    
    nova_string = vogais + consoantes
    return nova_string

while True:
    entrada = input("Digite uma string: ")
    
    if entrada == "":
        break
    
    nova_string = gerar_nova_string(entrada)
    print("Nova string:", nova_string)
