'''import platform
print(platform.system())
print(platform.release())
print(platform.processor())'''

'''import sys
print(sys.argv)
print(sys.path)
print(sys.version)
print(sys.exit())'''

'''import math
print(math.sqrt(625))
print(math.pow(2,3))
print(math.ceil(12.4))
print(math.floor(7.99))
print(math.fabs(-99))
print(math.factorial(5))
print(math.gcd(2,24))
print(math.log(6))
print(math.sin(30))
print(math.cos(0))
print(math.tan(45))
print(math.degrees(45))
print(math.radians(30))
print(abs(-1))'''

'''import random
random.seed(5)
print(random.random())
print(random.randint(1,6))
print(random.uniform(1,5))
names=['vikash','rahul','ram','rana']
print(random.choice(names))
print(random.choices(names,k=3))
print(random.shuffle(names))
print(names)'''



import random
import sys

def dice():
    return random.randint(1,6)

def first_player_turn():
    global player1_score
    player1_status=input(f"{player1}: Want to [C]ontinue or [S]top: ").upper()
    if player1_status=='C':
        player1_turn=dice()
        player1_score+=player1_turn
        if player1_score in snakes:
            player1_score=snakes[player1_score]
            print(f"\n{player1}'s turn:\nDice: {player1_turn}\n---Snake bite---\nBoard position: {player1_score}")
        elif player1_score in ladders:
            player1_score=ladders[player1_score]
            print(f"\n{player1}'s turn:\nDice: {player1_turn}\n*****Ladder*****\nBoard position: {player1_score}")
        else:
            print(f"\n{player1}'s turn:\nDice: {player1_turn}\nBoard position: {player1_score}")
    elif player1_status=='S':
        print(f'\n{player1} quit the game.\n{player2} Won the game!!!')
        sys.exit()

def second_player_turn():
    global player2_score   
    player2_status=input(f"{player2}: Want to [C]ontinue or [S]top: ").upper()
    if player2_status=='C':
        player2_turn=dice()
        player2_score+=player2_turn
        if player2_score in snakes:
            player2_score=snakes[player2_score]
            print(f"\n{player2}'s turn:\nDice: {player2_turn}\n---Snake bite---\nBoard position: {player2_score}")
        elif player2_score in ladders:
            player2_score=ladders[player2_score]
            print(f"\n{player2}'s turn:\nDice: {player2_turn}\n*****Ladder*****\nBoard position: {player2_score}")
        else:
            print(f"\n{player2}'s turn:\nDice: {player2_turn}\nBoard position: {player2_score}")
    elif player2_status=='S':
        print(f'\n{player2} quit the game.\n{player1} Won the game!!!')
        sys.exit()



player1=input("Enter the player-1: ")
player2=input("Enter the player-2: ")

player1_score=0
player2_score=0

winning_point=100

snakes={99:23,81:17,72:64,67:14,56:32,48:12,34:3,25:19,16:9}
ladders={7:19,18:77,23:85,31:44,45:71,54:63,61:94,78:88,89:93}


while player1_score<winning_point and player2_score<winning_point:
    first_player_turn()
    second_player_turn()        
else:
    if player1_score>player2_score:
        print(f"\n\n{player1} Win the game!!!!!!")
    elif player1_score==player2_score:
        print(f"\n\nTie!!!!!!")
    else:
        print(f"\n\n{player2} Win the game!!!!!!")


    



