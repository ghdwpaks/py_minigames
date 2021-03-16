import tkinter as t

key = ""
def key_down(e) :
    global key
    key = e.keysym
def key_up(e) :
    global key
    key = ""

mx = 1
my = 1
def main_proc() :
    global mx,my
    if key == "Up" and maze[my - 1][mx] == 0:
        my = my - 1
    if key == "Down" and maze[my + 1][mx] == 0:
        my = my + 1
    if key == "Left" and maze[my][mx - 1] == 0 :
        mx = mx - 1
    if key == "Right" and maze[my][mx + 1] == 0 :
        mx = mx + 1
    c.coords("MYCHR",mx*80+40,my*80+40)
    r.after(300,main_proc)
    
r = t.Tk()
r.title("미로 안 이동하기")
r.bind("<KeyPress>",key_down)
r.bind("<KeyRelease>",key_up)
c = t.Canvas(width=800,height=560,bg="skyblue")
c.pack()
maze = [
[1,1,1,1,1,1,1,1,1,1],
[1,0,0,0,0,0,1,0,0,1],
[1,0,1,1,0,0,1,0,0,1],
[1,0,0,1,0,0,0,0,0,1],
[1,0,0,1,1,1,1,1,0,1],
[1,0,0,0,0,0,0,0,0,1],
[1,1,1,1,1,1,1,1,1,1]
]

for y in range(7) :
    for x in range(10) :
        if maze[y][x] == 1:
            c.create_rectangle(x*80,y*80,x*80+79,y*80+79,fill="gray",width=0)
img01 = t.PhotoImage(file="hk3.png")
c.create_image(mx * 80 + 40, my*80+40,image=img01,tag="MYCHR")

main_proc()
r.mainloop()

