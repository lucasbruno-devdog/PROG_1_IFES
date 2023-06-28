import math

def quadrado_perfeito(num):
    operacao_1 = (num // 2) + 1
    op_var = None
    sqr = None
    for i in range(1, operacao_1 + 1):
        if num > i ** 2:
            operacao_2 = num - i ** 2
        else:
            operacao_2 = i ** 2 - num
        if i == 1 or operacao_2 < op_var:
            op_var = operacao_2
            sqr = i 
    return sqr

def quadrado(num):
    quadrado_perfeito_var = quadrado_perfeito(num)
    quadrado_var = (num + (quadrado_perfeito_var ** 2)) / (2 * quadrado_perfeito_var)
    return quadrado_var  
    
def main():
    num = int(input())
    while num >= 0:
        sqr = quadrado(num)
        print(f'N={num:.4f} RAIZ={sqr:.6f}')
        num = int(input())
    return 0

if __name__ == "__main__":
    main()
