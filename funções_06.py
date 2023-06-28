import math
def fatorial(num):
   fatorial_var = 1
   while( num > 0):
       fatorial_var = fatorial_var * num
       num -= 1          
   return fatorial_var
    
def main():
    num = int(input())
    while( num >= 0):
        print(fatorial(num))
        num = int(input())
    return 0
if __name__ == "__main__":
  main() 