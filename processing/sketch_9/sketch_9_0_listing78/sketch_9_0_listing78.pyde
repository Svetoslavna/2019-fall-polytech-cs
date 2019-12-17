def setup():
    background(100)
    smooth()
    noStroke()
    img0 = loadImage("001.jpg")
    img1 = loadImage("001black.jpg")
    size(600, 800)
def draw():
    global img0, img1
    if( frameCount == 1):
        image(img1, 0, 0, 600, 800)
        pointSize = map(mouseX, 0, width, 0, 100)
        pointAlpha = map(mouseY, 0, height, 0, 255)
        x=random(img0.width)
        x = int
        y=random(img0.height)
        loc = x + y*img0.width
        img0.loadPixels()
        r = red(img0.pixels[loc])
        g = green(img0.pixels[loc])
        b = blue(img0.pixels[loc])
        fill(r,g,b,pointAlpha)
        ellipse(x,y,pointSize,pointSize)
        tint(255, 2)
        image(img1, 0, 0, 600, 800)
def keyPressed():
    saveFrame("myProcessing" + frameCount +".jpg")
