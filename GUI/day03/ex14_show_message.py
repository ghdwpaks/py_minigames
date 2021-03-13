import tkinter as t
import tkinter.messagebox

def click_btn() :
    tkinter.messagebox.showinfo("정보","버튼을 눌렀습니다.")

r = t.Tk()
r.title("첫번재 메시지 박스")
r.geometry("400x200")
btn = t.Button(text="테스트",command=click_btn)
btn.pack()
r.mainloop()

