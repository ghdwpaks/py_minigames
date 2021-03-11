import tkinter

def react_button() :
    button["text"] = "클릭하셨습니다."

root = tkinter.Tk()
root.title("첫 번째 버튼")
root.geometry("800x600")
button = tkinter.Button(root, text="버튼 문자열",font=("배달의민족 한나체 Pro",24),command=react_button)
button.place(x=200,y=100)

root.mainloop()

