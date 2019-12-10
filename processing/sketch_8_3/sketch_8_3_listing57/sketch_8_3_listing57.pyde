
centerX= 250
centerY= 250
angle = 0
size0  = 0
weight = 0
counter = 0

class MyEllipse():

    cX = centerX
    cY = centerY
    cA = angle
    eS = size0
    Ew = weight

    def render(self, size0):
        fill(200, size0/20)
        x1 = centerX - cos(angle)*size0/2
        y1 = centerY + sin(angle)*size0/2

        stroke(250, 100)
        strokeWeight(weight)
        ellipse(x1, y1,size0,size0)

ellipseObj = MyEllipse()

def setup():
    size(500,500)
    smooth()
    background(10)

def draw():
    global counter
    counter += 0.01
    if (counter > 2*PI):
        counter = 0

    ellipseObj.render(sin(counter*4)*mouseX)
