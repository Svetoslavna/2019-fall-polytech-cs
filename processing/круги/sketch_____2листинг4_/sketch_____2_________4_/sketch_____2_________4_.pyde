w=500 #windowWidth
h=500 #windowHeight
s=100 #ellipseSize
def setup():
    size(500,500)
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
