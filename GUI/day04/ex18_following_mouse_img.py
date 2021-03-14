import tkinter as t
key = 0

def key_down(e) :
    global key
    key = e.keysym


def main_proc() :
    lab["text"] = key
    r.after(100,main_proc)



r = t.Tk()
r.title("실시간 키입력")
r.bind("<KeyPress>",key_down)
lab = t.Label(font=("배달의민족 한나체 Pro",80))
lab.pack()


main_proc()

r.mainloop()




