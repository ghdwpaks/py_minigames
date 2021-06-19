import random as r

def get_dice_data() :
    left_dice = 5
    left = 3
    choosed_dices = []
    for j in range(left) :
        n = []
        for i in range(left_dice) :
            n.append(r.randrange(1,7))
        print("나온 숫자 :",n)
        if left == 0 :
            choosed_dices.extend(n)
        elif len(n) == 1 and j == left-1 :
            choosed_dices.extend(n)
            left_dice = 0 
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
    
    print("최종적으로 선택된 주사위들 :",choosed_dices)
    return choose_count
def print_can_set_score(possible_section) :
    #possible_section = [1,1,1,0,1,1,0,0,1,1,1,1]
    '''
    Possible_section
    0 : Aces    1이 나온 주사위 눈의 총합
    1 : Deuces  2이 나온 주사위 눈의 총합
    2 : Threes  3이 나온 주사위 눈의 총합
    3 : Fours   4가 나온 주사위 눈의 총합
    4 : Fives   5가 나온 주사위 눈의 총합
    5 : Sixes   6이 나온 주사위 눈의 총합
    6 : Choice          주사위 눈 5개의 총합. 최대 30점
    7 : 4 of a Kind     동일한 주사위 눈이 4개 이상일때, 주사위 눈 5개의 총합. 최대 30점
    8 : Full House      동일한 주사위 눈이 각각 3개, 2개일때, 주사위 눈 5개의 총합. 최대 30점
    9 : Small Straight  이어지는 주사위 눈이 4개 이상일때, 고정 15점
    10 : Large Stringt  이어지는 주사위 눈이 5개일때. 고정 30점
    11 : Yacht          동일한 주사위 눈이 5개일때. 고정 50점
    '''
    print()
round = 12
for i in range(round) :
    dice_result = get_dice_data()
    


