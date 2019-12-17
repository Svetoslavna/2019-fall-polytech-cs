def setup():
    size(784, 600)
    background(100)
    smooth()
    img1 = loadImage("001.jpg")
    img2 = loadImage("002.jpg")
    global img1, img2
    
def draw():
    global img1, img2
    background(100)
    myTint002 = map(mouseX, 0, width, 0, 255)
    myTint001 = map(mouseX, 0, width, 255, 0)
    tint(255, myTint001)
    image(img1, 0, 0, 784, 600)
    tint(255, myTint002)
    image(img2, 0, 0,784, 600 )
