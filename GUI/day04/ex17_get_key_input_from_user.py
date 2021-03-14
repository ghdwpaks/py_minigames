import tkinter as t
key1 = 0
key2 = 0
m1 = [0,0]
m2 = [0,0]
tmr = 0
def key_down(e) :
    global key1
    key1 = e.keycode
    print("KEY_DOWN : ",str(key1))
    #r.bind("<KeyPress>",key_down)

def key_up(e) :
    global key2
    key2 = e.keycode
    print("KEY_UP : ",str(key2))

def Mouse_move(e) :
    global m1
    m1[0] = e.x
    m1[1] = e.y
    print("Mouse_move : ",str(m1))

def Mouse_button(e) :
    global m2
    m2[0] = e.x
    m2[1] = e.y
    print("Mouse_button_down : ",str(m2))


def count_up() :
    global tmr
    tmr += 1
    l["text"] = tmr
    #print(type(l))
    r.after(500,count_up)


r = t.Tk()

l = t.Label(font=("Times New Roman",80))
l.pack()

r.title("키 코드 얻기")
r.bind("<KeyPress>",key_down)
r.bind("<KeyRelease>",key_up)
r.bind("<Motion>",Mouse_move)
r.bind("<Button>",Mouse_button)
r.after(500,count_up)
print(1)
r.mainloop()
print(2)





