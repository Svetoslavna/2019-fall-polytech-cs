def setup():
    size(500, 500)
    smooth()
    strokeWeight(1)
    background(0)
i = 0
int(i)
k = 1
int(k)
def draw():
    global i, k
    stroke(i, 20)
    line(mouseX, mouseY, random(0, 500), 500)
    i += k
    if(i==255):
        k=-1
    if(i == 0):
        k = 1
def keyPressed():
    if(key=='s'):
        saveFrame("myProcessing.png")
