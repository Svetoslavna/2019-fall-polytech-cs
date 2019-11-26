def setup():
    size(500, 500)
    smooth()
    background(255)
    noStroke()
    noLoop()
def draw():
    for i in range(0, 10, 1):
        for k in range(5):
            fill(i*20)
            rect(i*40+50, 75+40*(2*k-1), 35, 35)
            fill(160-15*i)
            rect(i*40+50, 75+40*2*k, 35, 35)
