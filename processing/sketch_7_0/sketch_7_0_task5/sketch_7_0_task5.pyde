def setup():
    size(500, 500)
    smooth()
    background(255)
    strokeWeight(1)

counter=0
counter1=0
cRadius=10
cx=250
cy=250
def draw():
    stroke(0, 50)
    global counter, counter1, cRadius, switcher
    nx = sin(counter1)*cRadius + cx
    ny = cos(counter1)*cRadius + cy
        
    x1 = nx - sin(counter)*(50)
    y1 = ny - cos(counter)*(50)
    x2 = nx + sin(counter)*(50)
    y2 = ny + cos(counter)*(50)
    
    line(mouseX+x1 , y1 , x2 , y2)
    
    counter += 0.1
    if (counter > 2*PI):
        counter = 0
        
    counter1 += 0.01
    cRadius += counter1/30
    
    if (counter1 > 2*PI):
        counter1 = 0
def keyPressed():
    if (key=='s'):
        saveFrame("myProcessing.png")
