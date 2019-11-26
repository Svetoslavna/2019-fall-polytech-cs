counter = 0
counter1 = 0
cx = 500/2
cy = 500/2
cRadius = 20
def setup():
    size(500, 500)
    smooth()
    background(0)
    strokeWeight(1)
def oneLineDraw(ncx, ncy):
    global counter, counter1, cx, cy, cRadius
    x1 = ncx - sin(counter1)*100
    y1 = ncy - cos(counter1)*100
    x2 = ncx + sin(counter1)*100
    y2 = ncy + cos(counter1)*100
    line(x1, y1, x2, y2)
def draw():
    global counter1, counter, cx, cy, cRadius
    stroke(200, 25)
    nx = sin(counter1)*cRadius + cx
    ny = cos(counter1)*cRadius + cy
    x1 = nx - sin(counter)*15
    y1 = ny - cos(counter)*15
    x2 = nx + sin(counter)*15
    y2 = ny + cos(counter)*15
    oneLineDraw(x2, y2)
    oneLineDraw(x1, y1)
    counter += 0.1
    if(counter > 2*PI):
        counter = 0
    counter1 += 0.01
    cRadius += counter/20
    if(counter1 > 2*PI):
        counter1 = 0
