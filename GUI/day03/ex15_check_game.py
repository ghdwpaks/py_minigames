import tkinter as t

def click_btn() :
    pts = 0
    for i in range(len(bv)) :
        if bv[i].get() == True :
            pts = pts + 1
    tx.delete("1.0",t.END)
    tx.insert("1.0","체크된 수는 "+str(pts)+"\n",t.END)
    tx.insert("2.0","당신은 둠을 플레이하기에",t.END)
    if pts == 1 :
        tx.insert("3.0"," 적합하지 않습니다.",t.END)
    elif pts == 2 :
        tx.insert("3.0"," 조금은 적합하지 않습니다.",t.END)
    elif pts == 3 :
        tx.insert("3.0"," 적합합니다",t.END)
    elif pts == 4 :
        tx.insert("3.0"," 잘 어울립니다.",t.END)
    elif pts == 5 :
        tx.insert("3.0"," 분명히 잘 될것입니다.",t.END)
    elif pts == 6 :
        tx.insert("3.0"," 찢고, 죽인다!",t.END)




print("Hello world!")
r = t.Tk()
r.title("고양이 지수 진단 게임")
r.resizable(False, False)
screen_width = 800
screen_height = 600
c = t.Canvas(r,width=screen_width,height=screen_height)
c.pack()
img1 = t.PhotoImage(file="img03.png")
c.create_image(400,300,image=img1)
button_font_size = 32
b = t.Button(text="진단하기",font=("System",32),bg="skyblue",command=click_btn)
b.place(x=400,y=screen_height-button_font_size-40)
tx = t.Text(width=40,height=5,font=("System",16))
tx.place(x=380,y=30)

bv = [None] * 6
cb = [None] * 6
it = [
    "높은 곳이 좋다",
    "샷건을 좋아한다",
    "이곳저곳 돌아다니는것을 좋아한다",
    "인간들을 지켜야한다",
    "악마들을 싫어한다",
    "찢고 , 죽인다!",
]
for i in range(len(bv)) :
    bv[i] = t.BooleanVar()
    bv[i].set(False)
    cb[i] = t.Checkbutton(text=it[i],font=("System",12), variable=bv[i],bg="#dfe")
    cb[i].place(x=400,y=160 + 40 * i)







r.mainloop()


