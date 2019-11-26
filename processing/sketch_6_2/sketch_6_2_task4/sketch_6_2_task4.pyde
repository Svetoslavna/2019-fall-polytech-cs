def setup():
    size(500,500)
    smooth()
    background(150)
    strokeWeight(1)
flug=1
int(flug)
def draw():
    stroke(flug,20)
    fill(10,20)
    myY2 = mouseY + random(-10,10)*10
    myX2 = mouseX + random(-10,10)*10
    ellipse(mouseX , mouseY ,  random(width)-myX2,  random(height)-myY2)
def keyPressed():
    global flug
    if(key=='w'):
        flug = 255
    if(key=='b'):
        flug = 0
    if(key=='s'):
        saveFrame("myProcessing.png")
