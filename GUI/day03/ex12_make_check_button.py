import tkinter as t



r = t.Tk()
r.title("체크 버튼 다루기")
r.geometry("400x200")


cb = t.Checkbutton(text="체크 버튼")
cb.pack()



r.mainloop()

