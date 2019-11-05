def setup():
    size(600,600)
    noLoop()
    
def set_color(i):
    fill(i)
    rect(0,50, 150, 50)
    rect(50,0, 50, 150)
    
def draw(): 
    background(20)
    smooth()
    noStroke()
    
    pushMatrix()
    translate(100, 0)
    rotate(PI/4)
    set_color(180)
    popMatrix()
    
    pushMatrix()
    translate(220, 110)
    rotate(PI/6)
    scale(2)
    set_color(220)
    popMatrix()
    
    pushMatrix()
    translate(520, 350)
    rotate(PI/3)
    scale(1.4)
    set_color(80)
    popMatrix()
