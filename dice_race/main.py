
import random
import os

def show_point(player,com) :
    for i in range(0,player-1) :
        print("*",end="")
    print("P",end="")
    for i in range(player,15) :
        print("*",end="")
    print("GOAL")

    for i in range(0,com-1) :
        print("*",end="")
    print("C",end="")
    for i in range(com, 15) :
        print("*",end="")
    print("GOAL")

print("Hello world!")
player = 0
com = 0

while True :
    os.system("cls")
    print("주사위 경주를 시작합니다!")
    n = random.randrange(0,5) + 1
    player += n
    n = random.randrange(0,5) + 1
    com += n
    show_point(player,com)
    u = input("")
    if player >= 14 or com >= 14 :
        break
print("승자는 ",end="")
if player >= 15 :
    print("플레이어",end="")
elif com >= 15 :
    print("컴퓨터",end="")
print("입니다!")









