import math
def main():
  gols_feitos = 0   
  media_gols = 0
  time_mais_gols = 0
  time_goleador = ""
  menor_gols_partida = 100
  quantidade_partida = 0
  time_vencedor = "" 
      
  nometime_um = input()
  nometime_dois = input()
  
  while (nometime_um != ""):
  
    golstime_um = int(input())
    if(golstime_um < 0):
      print("INVÁLIDO")
        
    golstime_dois = int(input()) 
    if(golstime_um < 0):
      print("INVÁLIDO")
      
    
      
    if(golstime_um > golstime_dois):
      time_vencedor = nometime_um
      print(f'{nometime_um} x {nometime_dois}')
      print(f'Vencedor: {time_vencedor}')
    elif(golstime_dois > golstime_um):
      time_vencedor = nometime_dois
      print(f'{nometime_um} x {nometime_dois}')
      print(f'Vencedor: {time_vencedor}')
    elif(golstime_um == golstime_dois):
      print(f'{nometime_um} x {nometime_dois}')
      print("Empate")
      
   
      
    if(menor_gols_partida > golstime_um):
      menor_gols_partida = golstime_um
    elif(menor_gols_partida > golstime_dois):
      menor_gols_partida = golstime_dois
     
    if(golstime_um > time_mais_gols and golstime_um > golstime_dois):
      time_mais_gols = golstime_um
      time_goleador = nometime_um
    elif(golstime_dois > time_mais_gols and golstime_dois > golstime_um):
      time_mais_gols = golstime_dois
      time_goleador = nometime_dois    
   
     
    quantidade_partida += 1
    gols_feitos += golstime_um + golstime_dois
    
    nometime_um = input()
    nometime_dois = input()
    
            
  media_gols = gols_feitos/quantidade_partida
  
  print(f'Média de Gols: {media_gols:.2f} por jogo')
  print(f'Time que fez mais gols em um jogo: {time_goleador}')
  print(f'Menor número de gols em uma partida: {menor_gols_partida}')  
  
    
 
 
  return 0

if __name__ == "__main__":
  main()
