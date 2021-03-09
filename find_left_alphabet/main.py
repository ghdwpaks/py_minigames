import random

print("Hello world!")

alphabet = ['A','B','C','D','E']

left = alphabet[random.randrange(0,len(alphabet))]

print("알파벳 ",end="")
for i in range(0,len(alphabet)) : print(alphabet[i],end=" ")
print(" 들 중에 하나가 사라졌습니다. 맞춰보세요!")
while True :
    u = input("입력 : ")
    if u == left :
        print("맞았습니다!")
        break
    else :
        print("아닙니다.")
        continue
    





