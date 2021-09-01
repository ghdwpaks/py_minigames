
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


print("[1,1,1,2,2] :",check_full_house([1,1,1,2,2]))
print("[2,2,2,3,4] :",check_full_house([2,2,2,3,4]))
print("[2,2,5,3,4] :",check_full_house([2,2,5,3,4]))
