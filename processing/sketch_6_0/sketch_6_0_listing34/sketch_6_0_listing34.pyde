#отрисовка линий сбоку
i = 0
int(i)
k = 1
int(k)
flug = 1
int(flug)
def setup():
    size(500, 500)
    smooth()
    strokeWeight(1)
    background(0)

def draw():
    global i, flug, k
    stroke(i, 20)
    if(flug == 1):
        line(mouseX, mouseY, 500, random(0, 500))
    else:
        line(mouseX, mouseY, 0, random(0, 500))
        
    i +=k
    if(i == 255):
        k = -1
        
    if(i == 0):
        k = 1

def keyPressed():
    global flug
    if(key =='q'):
        flug *=(-1)
        
    if(key =='s'):
        saveFrame("myProcessing.png")
