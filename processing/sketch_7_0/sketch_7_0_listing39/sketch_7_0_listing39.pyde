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
i=0
def draw():
    global i
    while i<2*PI:
        x1 = cos(i)*cRadius + cx
        y1 = sin(i)*cRadius + cy
        line(x1, y1, x1, y1)
        line(cx, cy, cx, cy)
        i+=2*PI/12
def keyPressed():
    if(key=='s'):
        saveFrame("myProcesing.png")
