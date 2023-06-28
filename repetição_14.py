import math
def main():
  
  maior_consumo = 0
  menor_consumo = 100000
  media_consumo = 0
  total_r = 0
  total_c = 0
  total_i = 0
  numero_consumidor = 1
  cont = 0

  preço_kWh = float(input())
  while(numero_consumidor != 0):
    numero_consumidor = int(input())
    if(numero_consumidor == 0):
      break
    qt_kWh_consumidos_mes = float(input())
    cod_cons = input().upper()

    total_pagar = preço_kWh * qt_kWh_consumidos_mes

    if(qt_kWh_consumidos_mes > maior_consumo):
      maior_consumo = qt_kWh_consumidos_mes

    if(qt_kWh_consumidos_mes < menor_consumo):
      menor_consumo = qt_kWh_consumidos_mes

    if(cod_cons == "R"):  
      total_r += qt_kWh_consumidos_mes

    elif(cod_cons == "C"):  
      total_c += qt_kWh_consumidos_mes

    elif(cod_cons == "I"):
      total_i += qt_kWh_consumidos_mes

    cont += 1

    print(f'{numero_consumidor} {total_pagar}')

  media_consumo = (total_r + total_c + total_i) / cont

  print(maior_consumo)
  print(menor_consumo)
  print(total_r)
  print(total_c)
  print(total_i)
  print(media_consumo)




  return 0


if __name__ == "__main__":
  main()
