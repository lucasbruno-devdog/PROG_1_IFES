def f_limpaCPF(s):
    cpf = ""
    for i in range(len(s)):
        if (s[i] != "."):
            cpf += s[i]
    return cpf

def f_dv1(s):
    soma = 0
    m = 10
    for i in range(len(s)):
        soma += int(s[i])*m
        m = m-1
    dv1 = soma % 11
    if (dv1 < 2):
        dv1 = 0
    else:
        dv1 = 11 - dv1
    return dv1

def f_dv2(s):
    soma = 0
    m = 11
    for i in range(len(s)):
        soma += int(s[i])*m
        m = m-1
    dv1 = soma % 11
    if (dv1 < 2):
        dv1 = 0
    else:
        dv1 = 11 - dv1
    return dv1

def f_verificaCPF(cpf,dv):
    dv1 = f_dv1(cpf)
    dv2 = f_dv2(cpf+str(dv1))
    if (dv == str(dv1)+str(dv2)):
        return True
    return False

def main():
    cpf = input()
    cpf1 = f_limpaCPF(cpf[:11])
    dv = cpf[12:]
    if (f_verificaCPF(cpf1,dv)):
        print("CPF VÁLIDO")
    else:
        print("CPF INVÁLIDO")
    return 0

if __name__ == "__main__":
    main()