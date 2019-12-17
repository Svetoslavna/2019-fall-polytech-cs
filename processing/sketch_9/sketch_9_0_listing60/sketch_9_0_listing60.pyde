xCoordinate = [xCoordinate for xCoordinate in range(10)]
def setup():
    size(500, 500)
    smooth()
    noStroke()
    for i in range(0, len(xCoordinate), 1):
        xCoordinate[i] = 35*i + 90
def draw():
    background(50)
    for coordinate in (xCoordinate):
        fill(200)
        ellipse(coordinate, 250, 30, 30)
        fill(0)
        ellipse(coordinate, 250, 3, 3)
def keyPressed():
    if (key=='s'):
     savefrom("myProcessing.png")
    
