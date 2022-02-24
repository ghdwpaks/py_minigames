

STD_INPUT_HANDLE   = -10
STD_OUTPUT_HANDLE  = -11
STD_ERROR_HANDLE   = -12

FOREGROUND_BLACK     = 0x00
FOREGROUND_BLUE      = 0x01 # text color contains blue.
FOREGROUND_GREEN     = 0x02 # text color contains green.
FOREGROUND_RED       = 0x04 # text color contains red.
FOREGROUND_INTENSITY = 0x08 # text color is intensified.
BACKGROUND_BLUE      = 0x10 # background color contains blue.
BACKGROUND_GREEN     = 0x20 # background color contains green.
BACKGROUND_RED       = 0x40 # background color contains red.
BACKGROUND_INTENSITY = 0x80 # background color is intensified.

#6 yellow 노랑 
#2 green 초록
#8 gray 회색

import ctypes

std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)


def set_color(color, handle=std_out_handle):
    bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return bool

def select_green(UserInput , Word) :
    #UserInput : ['g', 'h', 'p', 'w', 'd']
    #Word : ['w', 'o', 'r', 'l', 'd']
    #res : [0, 0, 0, 0, 1]
    res = [0,0,0,0,0]
    for i in range(len(Word)) :
        if UserInput[i] == Word[i] :
            res[i] = 1
    return res

def select_yellow(UserInput, Word) :
    #UserInput : ['g', 'h', 'd', 'w', 'p']
    #Word : ['w', 'o', 'r', 'l', 'd']
    #res : [0, 0, 1, 0, 0]
    res = [0,0,0,0,0]
    for i in range(len(Word)) :
        if UserInput[i] in Word :
            res[i] = 2
    return res

def res_printer(RES) :
    global Inputs
    #print("len(RES) :",len(RES))
    #print("RES :",RES)
    #print("Inputs :",Inputs)
    Answer = 0
    for i in range(len(RES)) :
        #print("i :",i)
        if RES[i] == 0 :
            set_color(8)
            print((" "*i)+str(Inputs[i]))
        elif RES[i] == 1 :
            set_color(2)
            print((" "*i)+str(Inputs[i]))
            Answer += 1 
        elif RES[i] == 2 :
            set_color(6)
            print((" "*i)+str(Inputs[i]))
        elif RES[i] == 3 :
            set_color(2)
            print((" "*i)+str(Inputs[i]))
            Answer += 1 
    set_color(7)
    return Answer


Word = list("world")
#print("word :",word)



set_color(6)
print("Hello, world!")

set_color(2)
print("Hello, world!")

set_color(8)
print("Hello, world!")
set_color(7)

print("게임을 시작하겠습니다.")
Inputs = ""
while True :
    while True :
        Inputs = input("단어 입력 : ")
        if not len(Inputs) == 5 :
            print("다시 입력해주세요.")
            continue
        else :
            break

    Inputs = list(Inputs)
    YellowRes = select_yellow(Inputs, Word)
    GreenRes = select_green(Inputs, Word)
    RES = [0,0,0,0,0]
    for i in range(len(YellowRes)) :
        RES[i] = YellowRes[i] + GreenRes[i]
    #RES 0 : 미포함 , 1 : 정확 , 2 : 포함 , 3 : 정확
    Ans = res_printer(RES)
    if Ans >= 5 :
        break
    
set_color(7)
print("맞았습니다!")

