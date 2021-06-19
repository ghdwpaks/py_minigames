import random as r
n = []
left_dice = 5
left = 3
 
choosed_dices = []

for j in range(left) :
    for i in range(left_dice) :
        n.append(r.randrange(1,7))
    print("나온 숫자 :",n)
    if left == 0 :
        choosed_dices.extend(n)
    else :
        choose_count = 0
        choose = input("주사위 입력(ex:10010) :")
        choose = list(choose)
        for k in range(left_dice) :
            if choose[k] == "1" :
                choosed_dices.append(n[k])
                choose_count += 1
        print("선택된 주사위들 :",choosed_dices)
        if len(n) - choose_count == 0 :
            break
        else :
            left_dice -= choose_count
    n.clear()
print("최종적으로 선택된 주사위들 :",choosed_dices)



