def setup():
    size(500, 500)
    smooth()
    background(255)
    strokeWeight(1)

counter=0
counter1=0
cRadius=100
cx=250
cy=250
def draw():
    stroke(0, 30)
    global counter, counter1, cRadius, cy, cx
    nx = sin(counter1)*cRadius + cx
    ny = cos(counter1)*cRadius + cy
        
    x1 = nx - sin(counter)*(100)
    y1 = ny - cos(counter)*(100)
    x2 = nx + sin(counter)*(100)
    y2 = ny + cos(counter)*(100)
    
    bezier(x1, y1, x1-x2, y1-y2, x2 -x1, y2 -y1, x2 , y2)
    bezier(x1, y1, x1+x2 , y1+y2 , x2+x1, y2+y1, x2 , y2)
    fill(255)
    
    counter += 0.1
    if (counter > 2*PI):
        counter = 0
        
    counter1 += mouseX/(float (width*2))
    
    if (counter1 > 2*PI):
        counter1 = 0
def keyPressed():
    if (key=='s'):
        saveFrame("myProcessing.png")
