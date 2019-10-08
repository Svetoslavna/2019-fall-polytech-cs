w=(int(500)) #windowWidth
h=(int(500)) #windowHeight
s=(int(100)) #ellipseSize
x=(int(200)) #ellipseWidth
y=(int(300)) #ellipseHeight
def setup():
    size(w,h)
    smooth()
    background(255)
    fill(50, 80)
    stroke(100)
    strokeWeight(3)
    noLoop()
def draw():
    ellipse(w/2, h/2 - s/2, x, y)
    ellipse(w/2 - s/2, h/2, x, y)
    ellipse(w/2 + s/2, h/2, x , y)
    ellipse(w/2, h/2 + s/2, x , y)
