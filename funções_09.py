import math
def dec_to_bin(num):
    # Converte um número decimal para binário
    if(num == 0):
        return 0
    binary = ''
    while(num > 0):
        binary = str(num % 2) + binary
        num //= 2
    return int(binary)


def dec_to_hex(num):
    # Converte um número decimal para hexadecimal
    hex_chars = '0123456789ABCDEF'
    if(num == 0):
        return '0'
    hexa = ''
    while(num > 0):
        hexa = hex_chars[num % 16] + hexa
        num //= 16
    return hexa

def main():
    numeros = []
    num = int(input())

    while (num >= 0):
        numeros.append(num)
        num = int(input())

    print("\nNúmeros convertidos para binário e hexadecimal:")
    for num in numeros:
        binario = dec_to_bin(num)
        hexadecimal = dec_to_hex(num)
        print(f"DEC={num} BIN={binario} HEX={hexadecimal}") 
    return 0

if __name__ == "__main__":
    main()
