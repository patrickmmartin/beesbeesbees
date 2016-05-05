from Tkinter import* # note case sensitive !
from random import*

#Set up window and canvas

window=Tk()

c=Canvas(window, width=700, height=500)

background_picture=PhotoImage(file='sky.gif')
c.create_image(350,250,image=background_picture)

c.pack()

def showxy(event):
    ex=event.x
    ey=event.y
    strxy='A Flying Bee - x=%d y=%d'% (ex,ey)
    window.title(strxy)
c.bind('<Motion>',showxy)

bee_custome_list=[]
pos=0,0
shift_x=20
x=50
y=170

def bee_costumes():

    image_list = ['bee1.gif', 'bee2.gif', 'bee3.gif', 'bee4.gif']

    for image in image_list:
        bee_costume = PhotoImage(file = image)
        bee_sample = bee_costume.subsample(5,5)
        bee_custome_list.append(bee_sample)

    return bee_custome_list

def do_animation(currentframe):
    global x
    global shift_x
    global c
    global pos
    
    def do_image(x, shift_x, offset):

        x_offset, y_offset = offset
        frameIndex=(currentframe%3)+(4 if (shift_x<0) else 0)
        c.create_image(50 + x + x_offset, 170 + y_offset, image=bee_custome_list[frameIndex], tag='current_bee')
        c.move('current_bee',shift_x,0)
        c.update()
        c.after(1)

    c.delete('current_bee')
    bee_costumes()
    do_image(x,shift_x, (0, 0))
    do_image(x,shift_x, (0, 100))
    do_image(x,shift_x, (0, 200))

    if x>650:
        shift_x=-20

    if x<20:
        shift_x=20

    x+=shift_x

    currentframe = currentframe+1

    c.after(300,do_animation,currentframe)

c.after(1,do_animation,0)

c.mainloop()

