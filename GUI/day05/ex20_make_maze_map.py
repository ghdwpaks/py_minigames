import tkinter as t
maze = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,1,0,0,1],
    [1,0,1,1,0,0,1,0,0,1],
    [1,0,0,1,0,0,0,0,0,1],
    [1,0,0,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]
]

r = t.Tk()
r.title("미로 표시")
c = t.Canvas(width=800,height=560,bg="skyblue")
c.pack()
for y in range(7) :
    for x in range(10) :
        if maze[y][x] == 1 :
            c.create_rectangle(x*80,y*80,x*80+80,y * 80 + 80,fill="gray")
r.mainloop()            






