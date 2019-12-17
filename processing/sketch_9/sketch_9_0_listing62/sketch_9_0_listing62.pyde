xCoordinate = [xCoordinate for xCoordinate in range(10)]
def setup():
    size(500, 500)
    smooth()
    noStroke()
    for i in range(0, len(xCoordinate), 1):
        xCoordinate[i] = 35*i + 90
def draw():
    background(50)
    for i in range(0, len(xCoordinate), 1):
        fill(200, 40)
        ellipse(xCoordinate[i], 250, 15*i, 15*i)
        fill(0)
        ellipse(xCoordinate[i], 250, 3, 3)
def keyPressed():
    if (key=='s'):
     savefrom("myProcessing.png")
    
