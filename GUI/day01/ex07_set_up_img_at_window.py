import tkinter
root = tkinter.Tk()
root.title("첫 번째 캔버스")
canvas = tkinter.Canvas(root,width=1000,height=500)
canvas.pack()

gazou = tkinter.PhotoImage(file="img03.png")
canvas.create_image(440,190,image=gazou)




root.mainloop()
