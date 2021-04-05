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
    print("#"*(n // 5),end="")
    print("]")

def print_ops(n) :
    os.system("cls")
    i = 1
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
    print()




while p :
    print("1.아쿠마(Akuma)")
    print("2.쇼타로(Shotaro)")
    print("3.바티801(Bati801)")
    print("4.하쿠초우(Hakuchou)")
    print("5.하쿠초우 드래그(HakuchouDrag)")
    print("6.파지오(Faggio)")
    print("7.렉트로(Lectro)")
    print("8.가고일(Gargoyle)")
    print("9.BF400")
    print("10.쓰러스트(Thrust)")
    print()
    print("0.EXIT 종료")
    u = input("종류선택 : ")
    if "exit" == u or "종료" == u or '0' == u or "EXIT" in u:
        p = False
    elif int(u) < 11 and int(u) > 0 :
        print_ops(int(u))
    else :
        continue