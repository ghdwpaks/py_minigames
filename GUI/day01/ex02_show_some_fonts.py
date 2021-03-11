import tkinter
root = tkinter.Tk() #윈도우 요소(객체)생성용 변수

u = input("입력 : ")
root.title("title : {}".format(u))
root.geometry("800x400")
#label = tkinter.Label(root, text=u,font=("System",24))
label = tkinter.Label(root, text=u,font=("배달의민족 한나체 Pro",24))
label.place(x=200,y=100)

root.mainloop() #이 mainloop는, 모든 설정이 끝난 후에 설정시켜줘야한다.


