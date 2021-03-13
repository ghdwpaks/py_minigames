import tkinter

def check() :
    if cv.get() == True :
        print("체크되어 있습니다.")
    else :
        print("체크되어 있지 않습니다.")


r = tkinter.Tk()
r.title("처음부터 체크된 상태 만들기")
r.geometry("400x200")
cv = tkinter.BooleanVar()
cv.set(True)
cb = tkinter.Checkbutton(text="체크 버튼",variable=cv,command=check)
cb.pack()
r.mainloop()




