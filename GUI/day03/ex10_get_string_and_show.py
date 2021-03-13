import tkinter as t

def input_btn():
    input_string = e.get()
    b["text"] = input_string


r = t.Tk()
r.title("게임창 타이틀")
r.geometry("400x200")
e = t.Entry(width=20)
e.place(x=10,y=10)

b = t.Button(text="문자열 얻기", command=input_btn)
b.place(x=20,y=100)



r.mainloop()

