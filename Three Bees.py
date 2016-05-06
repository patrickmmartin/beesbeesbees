from Tkinter import* # note case sensitive !

class Bee:
    "this class wraps up the properties of an individual bee"
    def __init__(self, offset):
        self.offset = offset
        # TODO(PMM) there is clearly scope for more properties in future iterations

class Swarm:
    " this class manages a swarm of Bees "

    def bees(self):
        "creates a swarm of bees"
        result = []

        for bindex in range(0, 3):
            result.append(Bee((0, 100 * bindex)));
        return result

    def bee_costumes(self):
        " creates the costume list"
        result = []
        ## should be N right facing, N left facing
        image_list = ['bee1.gif', 'bee2.gif', 'bee3.gif', 'bee4.gif']

        for image in image_list:
            bee_costume = PhotoImage(file = image)
            bee_sample = bee_costume.subsample(5, 5)
            result.append(bee_sample)

        return result

    def __init__(self):
        self.custome_list = self.bee_costumes()
        self.list = self.bees()


class BeeApp:
    " this class wraps up the book keeping of the Bee app"

    def __init__(self):
        #Set up window and canvas
        self.window = Tk()

        self.canvas = Canvas(self.window, width = 700, height = 500)

        # note: the app needs to own the background
        self.background_picture = PhotoImage(file='sky.gif')
        self.canvas.create_image(350, 250, image = self.background_picture)

        self.canvas.pack()
        
        self.swarm = Swarm()

        self.shift_x = 20
        self.x = 50
        self.currentFrame = 0;


    def do_image(self, bee):
        "actually creates a sprite with the known tag"

        x_offset, y_offset = bee.offset
        mid = len(self.swarm.custome_list) / 2
        frameIndex = (self.currentFrame % (mid) ) + ( (mid) if (self.shift_x < 0) else 0)
        app.canvas.create_image(50 + self.x + x_offset, 170 + y_offset,
                                    image = self.swarm.custome_list[frameIndex],
                                    tag='current_bee')
        self.canvas.update()
        self.canvas.after(1)


    def do_animation(self):
        " cleans up last frame and redraws the bee list"
    
        self.canvas.delete('current_bee')

        for bee in self.swarm.list:
            self.do_image(bee)

        if self.x > 650:
            self.shift_x = -20

        if self.x < 20:
            self.shift_x = 20

        self.x += self.shift_x

        self.currentFrame = self.currentFrame + 1

        self.canvas.after(100, self.do_animation)

    def run(self):
        " takes control of animation and invokes the main TK loop"
        self.canvas.after(1, self.do_animation)

        self.canvas.mainloop()

# construct here
app = BeeApp()

app.run()
