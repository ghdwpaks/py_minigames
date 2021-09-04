import random as r
import copy as c

def get_dice_data() :
    left_dice = 5
    left = 5
    choosed_dices = []
    exit = False
    for j in range(left) :
        n = []
        for i in range(left_dice) :
            n.append(r.randrange(1,7))
        print("나온 숫자 :",n)
        if left == 0 :
            choosed_dices.extend(n)
        elif j == left-1 :
            choosed_dices.extend(n)
            left_dice = 0 
        else :

            while True :
                try :
                    choose_count = 0
                    choose = input("주사위 입력(ex:10010) :")
                    choose = list(choose)
                    for k in range(left_dice) :
                        if choose[k] == "1" :
                            choosed_dices.append(n[k])
                            choose_count += 1
                    print("선택된 주사위들 :",choosed_dices)
                    if len(n) - choose_count == 0 :
                        exit = True
                    else :
                        left_dice -= choose_count
                    break
                except :
                    #print("에러남")
                    continue
            if exit :
                break
        #
        #print("탈출함")
        print("\n")
    
    print("최종적으로 선택된 주사위들 :",choosed_dices)
    return choosed_dices

def check_able(dice) :
    return  [1,1,1,1,1,1,1,check_4_of_a_kind(dice),check_full_house(dice),check_small_straight(dice),check_large_straight(dice),check_yacht(dice)]
    
    

def check_4_of_a_kind(dice) :
    #print("check_4_of_a_kind dice :",dice)
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
    suba = ""
    canpass = False
    for i in range(len(dice)) :
        base_num = dice[i]
        stack = 0
        for j in range(len(dice)) :
            if dice[j] == base_num :
                stack += 1
            if stack >= 3 :
                suba = str(dice[i])
                canpass = True
                #print("suba :",suba)
                #print("canpass :",canpass)
                break
        if canpass :
            #print("canpass 1 :",canpass)
            break
    
    if canpass :
        for i in range(len(dice)) :
            stack = 0
            base_num = dice[i]
            if str(base_num) == suba :
                continue
            #print("str(base_num) :",str(base_num))
            #print("suba :",suba)
            for j in range(len(dice)) :
                if dice[j] == base_num :

                    stack += 1
                if stack >= 2 :
                    return 1
    #print('last stack :',stack)
    return 0

def check_small_straight(dice) :
    dice = set(dice) 
    dice = list(dice)
    #print("check_small_straight dice :",dice)
    base_num = 0
    stack = 0
    
    base_num = c.deepcopy(dice[0])
    for i in range(len(dice)) :
        #print("base_num + i :",base_num + i)
        #print("dice[i] :",dice[i])
        if base_num + i == dice[i] :
            stack += 1

    #print("stack 1 :",stack)
    if stack >= 4 :
        return 1

    return 0

def check_large_straight(dice) :
    dice = c.deepcopy(dice)
    dice = set(dice) 
    dice = list(dice)
    #print("check_small_straight dice :",dice)
    base_num = 0
    stack = 0
    
    base_num = c.deepcopy(dice[0])
    for i in range(len(dice)) :
        #print("base_num + i :",base_num + i)
        #print("dice[i] :",dice[i])
        if base_num + i == dice[i] :
            stack += 1

    #print("stack 1 :",stack)
    if stack >= 5 :
        return 1

    return 0

def check_yacht(dice) :
    for i in range(len(dice)) :
        base_num = dice[i]
        stack = 0
        for j in range(len(dice)) :
            if dice[j] == base_num :
                stack += 1
        if stack >= 5 :
            return 1
    return 0


def return_all_sum(dice,num) :
    res = 0
    for i in range(len(dice)) :
        if dice[i] == num :
            res += num
    return res

def return_4_of_a_kind() :

    pass

def print_can_set_score(possible_section = [0,0,0,0,0,0,0,0,0,0,0,0]) :
    global dice_result
    global  points
    #print("현재 점수 :")
    #for i in range(len(points)) :
        #print(str(i+1)+"  "+str(points[i]))
    #print("\n\n")
    #possible_section = [1,1,1,0,1,1,0,0,1,1,1,1]
    '''
    Possible_section
    0 : Aces    1이 나온 주사위 눈의 총합
    1 : Deuces  2이 나온 주사위 눈의 총합
    2 : Threes  3이 나온 주사위 눈의 총합
    3 : Fours   4가 나온 주사위 눈의 총합
    4 : Fives   5가 나온 주사위 눈의 총합
    5 : Sixes   6이 나온 주사위 눈의 총합
    6 : Choice          주사위 눈 5개의 총합.
    7 : 4 of a Kind     동일한 주사위 눈이 4개 이상일때, 주사위 눈 5개의 총합.
    8 : Full House      동일한 주사위 눈이 각각 3개, 2개일때, 주사위 눈 5개의 총합.
    9 : Small Straight  이어지는 주사위 눈이 4개 이상일때, 고정 15점
    10 : Large Stringt  이어지는 주사위 눈이 5개일때. 고정 30점
    11 : Yacht          동일한 주사위 눈이 5개일때. 고정 50점
    '''
    prints = ["Aces\t\t1이 나온 주사위 눈의 총합","Deuces\t\t2이 나온 주사위 눈의 총합","Threes\t\t3이 나온 주사위 눈의 총합","Fours\t\t4가 나온 주사위 눈의 총합","Fives\t\t5가 나온 주사위 눈의 총합","Sixes\t\t6이 나온 주사위 눈의 총합","Choice\t\t주사위 눈 5개의 총합. 최대 30점","4 of a Kind\t동일한 주사위 눈이 4개 이상일때, 주사위 눈 5개의 총합. 최대 30점","Full House\t동일한 주사위 눈이 각각 3개, 2개일때, 주사위 눈 5개의 총합. 최대 30점","Small Straight\t이어지는 주사위 눈이 4개 이상일때, 고정 15점","Large Stringt\t이어지는 주사위 눈이 5개일때. 고정 30점","Yacht\t\t동일한 주사위 눈이 5개일때. 고정 50점"]
    
    for i in range(len(prints)) :
        if possible_section[i] == 1 :
            print(str(points[i])+"   "+str(i+1)+"  "+str(prints[i]))
        
    print("현재 나온 주사위 결과 :",dice_result)
    choose = int(input("삽입선택 :"))  
    c_1= choose -1 
    #print("c-1 : ",c_1)
    if possible_section[c_1] == 1 :
        #print(prints[c_1],"에 삽입 에정 확인됨")
        #print("c_1 == 6 :",c_1 == 6)
        if c_1 == 0 or c_1 == 1 or c_1 == 2 or c_1==3 or c_1== 4 or c_1== 5 :
            points[c_1] = return_all_sum(dice_result,choose)
        elif c_1 == 6 or c_1 == 7 or c_1 == 8:
            #print("6 또는 7 또는 8 들어옴")
            points[c_1] = sum(dice_result) 
        elif c_1 == 9 :
            points[c_1] = 15
            print(points[c_1])
        elif c_1 == 10 :
            points[c_1] = 30
            print(points[c_1])
        elif c_1 == 11 :
            points[c_1] = 50
            print(points[c_1])
    print()
    
round = 6
points = [0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(round) :
    dice_result = get_dice_data()
    #print("main dice_result :",dice_result)
    possible_section = check_able(dice_result)
    print_can_set_score(possible_section)
    print("\n\n\n\n")
    
print("게임이 끝났습니다")

prints = ["Aces\t\t1이 나온 주사위 눈의 총합","Deuces\t\t2이 나온 주사위 눈의 총합","Threes\t\t3이 나온 주사위 눈의 총합","Fours\t\t4가 나온 주사위 눈의 총합","Fives\t\t5가 나온 주사위 눈의 총합","Sixes\t\t6이 나온 주사위 눈의 총합","Choice\t\t주사위 눈 5개의 총합. 최대 30점","4 of a Kind\t동일한 주사위 눈이 4개 이상일때, 주사위 눈 5개의 총합. 최대 30점","Full House\t동일한 주사위 눈이 각각 3개, 2개일때, 주사위 눈 5개의 총합. 최대 30점","Small Straight\t이어지는 주사위 눈이 4개 이상일때, 고정 15점","Large Stringt\t이어지는 주사위 눈이 5개일때. 고정 30점","Yacht\t\t동일한 주사위 눈이 5개일때. 고정 50점"]
for i in range(len(points)) :
    print(points[i],"\t",prints[i])
print("최종 점수는",sum(points),"입니다.")

