pontuações = {}   
quantidade_jogador = 0
pontuação_maior = 0
total_pontos = 0
jogador_maior = ""

nick_jogador = input()  
while (nick_jogador != ""):
    
    pontos_jogador = 0
    
    for i in range(1, 11):
        acerto_erro = input()
        if acerto_erro == "A1":
            pontos_jogador += 5
        elif acerto_erro == "A2":
            pontos_jogador += 7   
        elif acerto_erro == "A3":
            pontos_jogador += 10
        elif acerto_erro == "E1":
            if(pontos_jogador > 0):
                pontos_jogador -= 2
        elif acerto_erro == "E2":
            if(pontos_jogador > 0):
                pontos_jogador -= 5
        elif acerto_erro == "E3":
            pontos_jogador = 0
            
        if(pontos_jogador < 0):
            pontos_jogador = 0
            
    #pontuações[nick_jogador] = pontos_jogador  
          
    print(f'{nick_jogador} {pontos_jogador} pontos')
    
    total_pontos = total_pontos + pontos_jogador
    quantidade_jogador += 1  
   
   
    if(pontos_jogador > pontuação_maior):
     jogador_maior = nick_jogador
     pontuação_maior = pontos_jogador
     
    nick_jogador = input() 
   
media_pontos = total_pontos/quantidade_jogador

#for nick_jogador, pontos_jogador in pontuações.items():
    #print( f'{nick_jogador} {pontos_jogador} pontos')   
      
print(f'Média de pontos = {media_pontos:.2f} por jogo')
print(f'Vencedor {jogador_maior} com {pontuação_maior} pontos')   
           
