def setup():
    global img
    background(100)
    smooth()
    size(800, 800)
    img = loadImage("01.jpg")
    

def draw():
    global img
    background(100)
    image(img , mouseX , mouseY, 200, 200)