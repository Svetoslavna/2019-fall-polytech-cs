def setup():
    size(500,500)
    smooth()
    noLoop()
    noStroke()
    ellipseMode(CENTER)
def draw():
    background(255)
    border = 50
    float(border)
    nw = width - 2*border
    float(nw)
    nh = height - 2*border
    float(nh)
    number = 5
    float(number)
    nWstep = nw / number
    float(nWstep)
    nHstep = nh / number
    float(nHstep)
    for i in range(0, number, 1):
        for j in range(0, number, 1):
            x = border*2 - j*nWstep + nWstep*4
            float(x)
            y = border*2 - i*nHstep + nHstep*4
            float(y)
            size = 5 + (j+i)*10
            float(size)
            mColor = size*1.5
            float(mColor)
            fill(mColor, 0, 150)
            ellipse(y, x, size, size)
            fill(250)
            ellipse(y, x, 3, 3)
