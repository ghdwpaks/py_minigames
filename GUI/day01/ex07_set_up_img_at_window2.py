import tkinter
from PIL import Image
root = tkinter.Tk()
root.title("첫 번째 캔버스")
window_width = 1500
window_height = 1000
canvas = tkinter.Canvas(root,width=window_width,height=window_height)
canvas.pack()

gazou = tkinter.PhotoImage(file="img03.png")
im = Image.open("img03.png")
print(im.size)
print(type(im.size[0]))
#canvas.create_image(im.size[0]//2,im.size[1]//2,image=gazou)
canvas.create_image(window_width//2,window_height//2,image=gazou)




root.mainloop()
