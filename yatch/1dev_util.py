import copy as c
def check_small_straight(dice) :
    dice = set(dice) 
    dice = list(dice)
    print("check_small_straight dice :",dice)
    base_num = 0
    stack = 0
    
    base_num = c.deepcopy(dice[0])
    for i in range(len(dice)) :
        print("base_num + i :",base_num + i)
        print("dice[i] :",dice[i])
        if base_num + i == dice[i] :
            stack += 1

    print("stack 1 :",stack)
    if stack >= 4 :
        return 1

    return 0
print("[1,1,1,2,2] :",check_small_straight([1,1,1,2,2]))
print("[2,2,2,3,4] :",check_small_straight([2,2,2,3,4]))
print("[2,2,5,3,4] :",check_small_straight([2,2,5,3,4]))
