a=600 #width
b=600 #height
def setup():
    size(a,b)
    noLoop()
    
def draw():
    background(100)
    smooth()
    strokeWeight(50)
    stroke(200)
    translate(a/2,b/2-100)
    line(-100,0,100,0)
    translate(0,100)
    scale(1.5,1.5)
    line(-100,0,100,0)
    translate(0,100)
    scale(1.5,1.5)
    line(-100,0,100,0)
    
