import random

def roll_dice():
    # Simula o lançamento de dois dados
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1 + dice2

def play_craps():
    # Função principal que joga o jogo de Craps
    rolls = []
    while True:
        roll = int(input())
        rolls.append(roll)
        print(roll)
        
        if len(rolls) == 1:
            if roll in [7, 11]:
                print("NATURAL! VOCÊ GANHOU")
                print(f"JOGADAS = {len(rolls)}")
                return
            elif roll in [2, 3, 12]:
                print("CRAPS! VOCÊ PERDEU")
                print(f"JOGADAS = {len(rolls)}")
                return
        else:
            if roll == rolls[0]:
                print("VOCÊ GANHOU")
                print(f"JOGADAS = {len(rolls)}")
                return
            elif roll == 7:
                print("VOCÊ PERDEU")
                print(f"JOGADAS = {len(rolls)}")
                return

# Programa principal
play_craps()
