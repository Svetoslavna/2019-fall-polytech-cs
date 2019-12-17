xCoordinate = [xCoordinate for xCoordinate in range(30)]
def setup():
    size(500, 500)
    smooth()
    noStroke()
    myInit()
def myInit():
     println("New coordinates : ")
     for i in range(len(xCoordinate)):
        xCoordinate[i] = 250 + random(-100,100)
def draw():
    background(30)
    for i in range(0, len(xCoordinate), 1):
        fill(20)
        ellipse(xCoordinate[i], 250, 5, 5)
        fill(250, 40)
        ellipse(xCoordinate[i], 250, 10*i, 10*i)
    if(mouseX > 250):
        myInit()
    println(max(xCoordinate))
def keyPressed():
    if (key=='s'):
        saveFrame("myProcessing.png")
