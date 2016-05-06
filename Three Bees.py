from Tkinter import* # note case sensitive !

class BeeApp:
    " this class wraps up the book keeping of the Bee app"

    def __init__(self):
        #Set up window and canvas
        self.window = Tk()

        self.canvas = Canvas(self.window, width=700, height=500)

        # note: the app needs to own the background
        self.background_picture = PhotoImage(file='sky.gif')
        self.canvas.create_image(350,250,image = self.background_picture)

        self.canvas.pack()

# construct here
app = BeeApp()

class Bee:
    " TODO(PMM) this class represents a bee sprite "

class Swarm:
    " TODO(PMM) this class manages a swarm of Bees "

# not really needed at this time
#def showxy(event):
#    ex=event.x
#    ey=event.y
#    strxy='A Flying Bee - x=%d y=%d'% (ex,ey)
#    window.title(strxy)
#c.bind('<Motion>',showxy)

bee_custome_list=[]
bee_list=[]
pos=0,0
shift_x=20
x=50
y=170

def bees():
    for bindex in range(0, 3):
        bee_list.append((0, 100 * bindex));

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
        app.canvas.create_image(50 + x + x_offset, 170 + y_offset, image=bee_custome_list[frameIndex], tag='current_bee')
        app.canvas.move('current_bee',shift_x,0)
        app.canvas.update()
        app.canvas.after(1)

    app.canvas.delete('current_bee')

    for bee in bee_list:
        do_image(x, shift_x, bee)

    if x>650:
        shift_x=-20

    if x<20:
        shift_x=20

    x+=shift_x

    currentframe = currentframe+1

    app.canvas.after(300,do_animation,currentframe)

bee_costumes()
bees()

app.canvas.after(1,do_animation,0)

app.canvas.mainloop()

