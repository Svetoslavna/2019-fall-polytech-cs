#линии отрисовываются сверху
i = 0
int(i)
k = 1
int(k)
flug = 1
int(flug)


def setup():
    size(500, 500)
    smooth()
    background(0)
    strokeWeight(1)


def upDate():
    global i,k
    i += k
    if(i == 255):
        k=-1

    if(i == 0):
        k=1

def draw():
    global i,flug
    stroke(i, 20)
    if(flug == 1):
        line(mouseX , mouseY , random(0,500), 0)
    else:
        line(mouseX , mouseY , random(0,500), random(0,500))

    upDate()


def keyPressed():
    global flug
    if (key== "q"):
        flug *=(-1)

    if (key== "s"):
        saveFrame("myProcessing .png")
