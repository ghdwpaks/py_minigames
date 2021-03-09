from datetime import datetime
import random
import copy
import time
def get_now_time() :
    now = datetime.now()
    time_s = int(now.second)
    time_m = int(now.minute)

    return time_m * 60 + time_s

alphabet_right = ['A','B','C','D','E']
alphabet_change = ['A','B','C','D','E']
score = 0
for ii in range(0,10) :
    start_time = get_now_time()
    rand_n = random.randrange(0,len(alphabet_right))
    alphabet_change[rand_n] = None
    for i in alphabet_change :
        if i != None :
            print(i,end=" ")
    u = input("사라진 알파벳은? : ")
    end_time = get_now_time()
    if start_time > end_time - 10 :
        score += 1
        print("제때에 잘 맞추셨습니다!!")
    else :
        print("시간초과했습니다!")
    alphabet_change = copy.deepcopy(alphabet_right)
print("총 10번의 기회로 {}번을 맞추셨습니다!".format(score))




