import tkinter as t
import random as rand

def click_btn() :
    lab["text"] = rand.choice(["대박","중간","안좋음","꽝"])
    lab.update()


r = t.Tk()
r.title("제비뽑기 프로그램")
r.resizable(False,False)
c = t.Canvas(r,width=1000,height=1000)
c.pack()
img01 = t.PhotoImage(file="img03.png")
c.create_image(440,150,image = img01)


print("Hello world!")
lab = t.Label(r, text="??",font=("times New Roman",120),bg="white")
lab.place(x=380,y=60)
button = t.Button(r,text="제비뽑기",font=("times new roman",36),command=click_btn,fg="skyblue")
button.place(x=360,y=400)








r.mainloop()