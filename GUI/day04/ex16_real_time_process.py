import tkinter as t
import time as ti
tmr = 0

def count_up() :
    global tmr
    tmr += 1
    l["text"] = tmr
    #print(type(l))
    r.after(500,count_up)


r = t.Tk()
l = t.Label(font=("Times New Roman",80))
l.pack()

r.after(500,count_up)
print(1)
r.mainloop()
print(2)



