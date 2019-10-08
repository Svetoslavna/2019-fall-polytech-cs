w=(int(400)) #windowWidth
h=(int(400)) #windowHeight
s=(int(200)) #ellipseSize
def setup():
    size(w,h)
    smooth()
    background(255)
    fill(50, 80)
    stroke(100)
    strokeWeight(3)
    noLoop()
def draw():
    ellipse(w/2, h/2 - s/2, s, s)
    ellipse(w/2 - s/2, h/2, s, s)
    ellipse(w/2 + s/2, h/2, s , s)
    ellipse(w/2, h/2 + s/2, s , s)
