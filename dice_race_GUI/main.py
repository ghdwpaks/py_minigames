import tkinter as t
import random as rd

def clicked_button() :
    #print("버튼을 눌렀습니다!")
    tx.delete("1.0",t.END)
    tx.insert("1.0","버튼을 눌렀습니다",t.END)


print("Hello world")
r = t.Tk()
r.title("랜덤 주사위 게임")
r.resizable(False,False)    #게임 창 크기 고정
screen_width = 800
screen_height = 600
c = t.Canvas(r,width=screen_width,height=screen_height)
c.pack()

bg_img01 = t.PhotoImage(file="img03.png")
c.create_image(400,300,image=bg_img01)
button_font_size = 32
button1 = t.Button(text="주사위 돌리기",font=("배달의민족 한나체 Pro",button_font_size),bg="skyblue",command=clicked_button)
button1.place(x=screen_height // 2,y=screen_height-button_font_size-50)
text_screen_height = 5
text_screen_width = 40
tx = t.Text(width=10,height=0,font=("배달의민족 한나체 Pro",16),bg="pink")
tx.place(x=text_screen_width,y=screen_height//10)





r.mainloop()







