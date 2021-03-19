
import tkinter as t
import tkinter.messagebox

key = ""
def key_down(e) :
    global key
    key = e.keysym
def key_up(e) :
    global key
    key = ""

mx = 1
my = 1
clear = 0
def main_proc() :
    global mx,my,clear
    if key == "Shift_L" and clear > 1:
        c.delete("PAINT")
        mx = 1
        my = 1
        clear = 0
        for y in range(7) :
            for x in range(10) :
                if maze[y][x] == 2:
                    maze[y][x] = 0
    if key == "Up" and maze[my - 1][mx] == 0 :
        my = my - 1
    if key == "Down" and maze[my + 1][mx] == 0:
        my = my + 1
    if key == "Left" and maze[my][mx - 1] == 0 :
        mx = mx - 1
    if key == "Right" and maze[my][mx + 1] == 0 :
        mx = mx + 1
    if maze[my][mx] == 0:
        maze[my][mx] = 2
        clear = clear + 1
        c.create_rectangle(mx*80,my*80,mx*80+79,my*80+79,fill="pink",width=0,tag="PAINT")
    c.delete("MYCHR")
    c.create_image(mx*80+40,my*80+40,image=img01,tag="MYCHR")
    if clear == 30 :
        c.update()
        t.messagebox.showinfo("축하합니다!","모든 바닥을 칠했습니다!")
    else :
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

