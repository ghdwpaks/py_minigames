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

def check_able(dice) :
    dice.sort()
    #dice = [1,1,1,3,5]
    possible_section = [check_4_of_a_kind()]
    pass
    

def check_4_of_a_kind(dice) :
    for i in range(len(dice)) :
        base_num = dice[i]
        stack = 0
        for j in range(len(dice)) :
            if dice[j] == base_num :
                stack += 1
        if stack >= 4 :
            return 1
    return 0
            
def check_full_house(dice) :

    #dice = [1,1,1,3,5]
    
    for i in range(len(dice)) :
        base_num = dice[i]
        stack = 0
        for j in range(len(dice)) :
            if dice[j] == base_num :
                stack += 1
        if stack == 2 :
            for l in range(len(dice)) :
                base_num2 = dice[l]
                stack2 = 0
                for k in range(len(dice)) :
                    if dice[k] == base_num2 :
                        stack2 += 1
                if stack2 == 3 :
                    return 1
    return 0

def check_small_straight(dice) :
    #dice = [1,1,1,3,5]
    for i in range(len(dice)) :
        for j in range(i) :
            stack = 0
            if dice[i] == dice[i-j] :
                stack += 1
            if stack >= 4 :
                return 1
    return 0



        





def print_can_set_score(possible_section = [0,0,0,0,0]) :
    #possible_section = [1,1,1,0,1,1,0,0,1,1,1,1]
    '''
    Possible_section
    0 : 4 of a Kind     동일한 주사위 눈이 4개 이상일때, 주사위 눈 5개의 총합. 최대 30점
    1 : Full House      동일한 주사위 눈이 각각 3개, 2개일때, 주사위 눈 5개의 총합. 최대 30점
    2 : Small Straight  이어지는 주사위 눈이 4개 이상일때, 고정 15점
    3 : Large Stringt  이어지는 주사위 눈이 5개일때. 고정 30점
    4 : Yacht          동일한 주사위 눈이 5개일때. 고정 50점
    '''
    prints = ["Aces\t\t1이 나온 주사위 눈의 총합","Deuces\t\t2이 나온 주사위 눈의 총합","Threes\t\t3이 나온 주사위 눈의 총합","Fours\t\t4가 나온 주사위 눈의 총합","Fives\t\t5가 나온 주사위 눈의 총합","Sixes\t\t6이 나온 주사위 눈의 총합","Choice\t\t주사위 눈 5개의 총합. 최대 30점","4 of a Kind\t동일한 주사위 눈이 4개 이상일때, 주사위 눈 5개의 총합. 최대 30점","Full House\t동일한 주사위 눈이 각각 3개, 2개일때, 주사위 눈 5개의 총합. 최대 30점","Small Straight\t이어지는 주사위 눈이 4개 이상일때, 고정 15점","Large Stringt\t이어지는 주사위 눈이 5개일때. 고정 30점","Yacht\t\t동일한 주사위 눈이 5개일때. 고정 50점"]
    
    for i in range(len(prints)) :
        if possible_section[i] == 1 :
            print(prints[i])
    
    print()
    
round = 12
print(check_small_straight([1,2,3,4,4]))


'''
print_can_set_score()
for i in range(round) :
    dice_result = get_dice_data()
'''
    


