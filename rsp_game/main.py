import random
u = int(input("1.가위 2.바위 3.보 :"))
com = random.randrange(0,3)
r = u - com
if r == 0 :
    print("비겼습니다")
elif r == 1 or r == -2 :
    print("이겼습니다")
elif r == -1 or r == 2 :
    print("졌습니다")



