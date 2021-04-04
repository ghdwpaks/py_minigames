print("Hello world!")
import csv
import os
table = []
with open('status_table.csv','r') as f :
    reader = csv.DictReader(f)
    for row in reader :
        table.append(row)
print(table)
print("Hello world!")
p = True #pass 이탈 여부
o = "" #object 
i = 1

def print_ops_graph(n) :
    n = int(n)
    print("\t[",end="")
    '''
    if n <= 5 :
        print("#",end="")
    elif n <= 10 :
        print("#"*2,end="")
    elif n <= 15 :
        print("#"*3,end="")
    elif n <=  20:
        print("#"*4,end="")
    elif n <=  25:
        print("#"*5,end="")
    elif n <=  30:
        print("#"*6,end="")
    elif n <=  35:
        print("#"*7,end="")
    elif n <=  40:
        print("#"*8,end="")
    elif n <=  45:
        print("#"*9,end="")
    elif n <=  50:
        print("#"*10,end="")
    elif n <=  55:
        print("#"*11,end="")
    elif n <=  60:
        print("#"*12,end="")
    elif n <=  65:
        print("#"*13,end="")
    elif n <=  70:
        print("#"*14,end="")
    elif n <=  75:
        print("#"*15,end="")
    elif n <=  80:
        print("#"*16,end="")
    elif n <=  85:
        print("#"*17,end="")
    elif n <=  90:
        print("#"*18,end="")
    elif n <=  95:
        print("#"*19,end="")
    elif n <=  100:
        print("#"*20,end="")
    '''
    print("#"*(n // 5),end="")
    print("]")

def print_ops(n) :
    os.system("cls")
    i = 1 #여기 i 에다가 n 넣어야 하지 않음?
    '''
    print("n = ",n)
    print("type(n) = ",type(n))
    print("table[1][0] : ",table[0])
    '''
    print("바이크 이름 : {}".format(table[0][str(n)]))
    print("스피드:\t\t{}".format(table[1][str(n)]),end='')
    print_ops_graph(table[1][str(n)])
    print("브레이크 :\t{}".format(table[2][str(n)]),end='')
    print_ops_graph(table[2][str(n)])
    print("가속 :\t\t{}".format(table[3][str(n)]),end='')
    print_ops_graph(table[3][str(n)])
    print("핸들링 :\t{}".format(table[4][str(n)]),end='')
    print_ops_graph(table[4][str(n)])
    print("최고속도 :\t{}".format(table[5][str(n)]),end='')
    print_ops_graph(table[5][str(n)])
    print("가격 :\t\t{}".format(table[6][str(n)]),end='')
    print("\n")
    #t = str(i + 1)
    #print("t =",t)
    #print("type(t) = ",type(t))
    #print("table[0][i+1] : ",table[0][str(t)])
    #print("len(table[0]) = ",len(table[0]))
    print()




while p :
    
    print("폭발무기와 중화기 또는 mk2무기들은 데이터를 다루지 않습니다.")
    print("1.아쿠마(Akuma)")
    print("2.쇼타로(Shotaro)")
    print("3.바티801(Bati801)")
    print("4.하쿠초우(Hakuchou)")
    print("5.하쿠초우 드래그(HakuchouDrag)")
    print()
    print("0.EXIT 종료")
    u = input("종류선택 : ")
    if '1' in u or 'HG' in u or "pis" in u or '아쿠마' in u :
        print()
        #print_ops('hg')
        print_ops(1)
    elif '2' in u or 'SMG' in u or "쇼타로" in u or 'smg' in u:
        print()
        #print_ops('smg')
        print_ops(2)
    elif '3' in u or 'ar' in u or "rifle" in u or '바티' in u or "바티801" in u or "바티" in u or '801' in u:
        print()
        #print_ops('ar')
        print_ops(3)
    elif '4' in u or 'SG' in u or "하쿠초우" in u or 'HakuchouDrag' in u :
        print()
        #print_ops('sg')
        print_ops(4)
    elif '5' in u or 'dmr' in u or '드래그' in u  or '801' in u:
        print()
        #print_ops('dmr')
        print_ops(5)
    elif "exit" == u or "종료" == u or '0' == u or "EXIT" in u:
        p = False
    else :
        continue