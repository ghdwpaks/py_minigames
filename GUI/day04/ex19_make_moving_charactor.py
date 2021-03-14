import tkinter as t
key = ""
cx = 400
cy = 300
def main_proc() :
    global cx,cy
    if key == "Up" :
        cy = cy - 20
    if key == "Down" :
        cy = cy + 20
    if key == "Left" :
        cx = cx - 20
    if key == "Right" :
        cx = cx + 20
    c.coords("MYCHR",cx,cy)
    r.after(10,main_proc)

def key_down(e) :
    global key
    key = e.keysym

def key_up(e) :
    global key
    key = ""




r = t.Tk()
r.title("캐릭터 이동")
r.bind("<KeyPress>",key_down)
r.bind("<KeyRelease>",key_up)

c = t.Canvas(width=800,height=600,bg="lightgreen")
c.pack()

img01 = t.PhotoImage(file="hk2.png")
c.create_image(cx,cy,image=img01,tag="MYCHR")

main_proc()
r.mainloop()





