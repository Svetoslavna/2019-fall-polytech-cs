def setup():
    size(500, 500)
    smooth()
    background(50)
    strokeWeight(5)
    stroke(250)
    noLoop()
cx = 250
cy = 250
cRadius = 200
counter = 0
mcolor = 0
def draw():
    global counter, mcolor
    while counter < 2*PI:
        x1 = cos(counter)*cRadius + cx
        y1 = sin(counter)*cRadius + cy
        mcolor += 1
        stroke(mcolor)
        line(cx, cy, y1, x1)
        counter += 2*PI/255
    if(counter < 2*PI):
        counter = 0
        mcolor = 0
        background(50)
def keyPressed():
    if(key=='s'):
        saveFrame("myProcesing.png")
