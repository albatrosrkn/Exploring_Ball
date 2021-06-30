
from drawingpanel import *
import time
def main():
    p = DrawingPanel(400, 400, background="light gray")
    ball= p.canvas.create_oval(5, 5, 60, 60, fill="red", width=0)
    x=1
    y=4

    while True:
        p.canvas.move(ball,x,y)
        pos=p.canvas.coords(ball)
        if pos[3]>=400 or pos[1]<=0:
            y=-y
        if pos[2]>=400 or pos[0]<=0:
            x=-x
        p.update()
        time.sleep(0.020)


main()
    

