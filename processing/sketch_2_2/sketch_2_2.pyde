barWidth = 20


def setup():
    size(barWidth * 32, 360)
    colorMode(HSB, width, height, 100)
    noStroke()


def draw():
    whichBar = mouseX / barWidth
    barX = whichBar * barWidth
    fill(barX, mouseY, 66)
    rect(barX, 0, barWidth, height)
