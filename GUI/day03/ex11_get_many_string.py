import tkinter as t

def input_btn():
    tx.insert(t.END,"몬스터 출현!")


r = t.Tk()
r.title("게임창 타이틀")
r.geometry("400x200")

b = t.Button(text="메시지", command=input_btn)
#b.place(x=20,y=100)
b.pack()

tx = t.Text()
tx.pack()



r.mainloop()

