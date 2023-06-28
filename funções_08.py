import math

def menor_num(num_1, num_2, num_3):
    if(num_1 <= num_2 and num_1 <= num_3):
        return num_1
    elif(num_2 <= num_3):
        return num_2
    else:
        return num_3

def mdc(num_1, num_2, num_3):
    aeon = 1
    max = menor_num(num_1, num_2, num_3)
    while(aeon <= max):
        if(num_1 % aeon == 0 and num_2 % aeon == 0 and num_3 % aeon == 0):
            mdc_var = aeon
        aeon += 1    
    return mdc_var   
    
def main():
   for i in range(4):    
    num_1 = int(input())
    num_2 = int(input())
    num_3 = int(input())
    print(f'MDC({num_1}, {num_2}, {num_3})={mdc(num_1, num_2, num_3)}')
    
   return 0

if __name__ == "__main__":
    main()
