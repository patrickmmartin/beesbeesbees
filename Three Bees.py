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

class Bee:
    def __init__(self, offset):
        self.offset = offset
        # TODO(PMM) there is clearly scope for more properties in future iterations

class Swarm:
    " TODO(PMM) this class manages a swarm of Bees "

    def bees(self):
        result = []

        for bindex in range(0, 3):
            result.append(Bee((0, 100 * bindex)));
        return result

    def bee_costumes(self):

        result = []
        image_list = ['bee1.gif', 'bee2.gif', 'bee3.gif', 'bee4.gif']

        for image in image_list:
            bee_costume = PhotoImage(file = image)
            bee_sample = bee_costume.subsample(5,5)
            result.append(bee_sample)

        return result

    def __init__(self):
        self.custome_list = self.bee_costumes()
        self.list = self.bees()


# not really needed at this time
#def showxy(event):
#    ex=event.x
#    ey=event.y
#    strxy='A Flying Bee - x=%d y=%d'% (ex,ey)
#    window.title(strxy)
#c.bind('<Motion>',showxy)

pos=0,0
shift_x=20
x=50


# construct here
app = BeeApp()

# construct here
swarm = Swarm()

def do_animation(currentframe):
    global x
    global shift_x
    global pos
    
    def do_image(x, shift_x, offset):

        x_offset, y_offset = offset
        # TODO(PMM) - this expression should derive from the costumes
        frameIndex = (currentframe % 2) + (2 if (shift_x < 0) else 0)
        app.canvas.create_image(50 + x + x_offset, 170 + y_offset,
                                image = swarm.custome_list[frameIndex],
                                tag='current_bee')
        app.canvas.update()
        app.canvas.after(1)

    app.canvas.delete('current_bee')

    for bee in swarm.list:
        do_image(x, shift_x, bee.offset)

    if x > 650:
        shift_x = -20

    if x < 20:
        shift_x = 20

    x += shift_x

    currentframe = currentframe + 1

    app.canvas.after(100, do_animation,currentframe)


app.canvas.after(1,do_animation,0)

app.canvas.mainloop()

