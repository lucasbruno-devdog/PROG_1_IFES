import math

def get_num_digits(num):
    # Retorna o número de dígitos de um número
    if num == 0:
        return 1
    count = 0
    while num != 0:
        count += 1
        num //= 10
    return count

def reverse_num(num):
    # Inverte um número
    reverse = 0
    while num != 0:
        reverse = (reverse * 10) + (num % 10)
        num //= 10
    return reverse

def is_perfect_square(num):
    # Verifica se um número é um quadrado perfeito
    sqrt = math.isqrt(num)
    return sqrt * sqrt == num

def is_palindrome(num):
    # Verifica se um número é uma capicua (para números com dois dígitos ou mais)
    if get_num_digits(num) < 2:
        return False
    if num == reverse_num(num):
        return True
    return False


# Programa principal
def main():
    for num in range(1, 5001):
        if is_perfect_square(num) and is_palindrome(num):
            print(f"{num} É CAPICUA E QUADRADO PERFEITO")
        elif is_perfect_square(num):
            print(f"{num} É QUADRADO PERFEITO")
        elif is_palindrome(num):
            print(f"{num} É CAPICUA")
    return 0

if __name__ == "__main__":
    main()
