centerX=250
centerY=250
length=350
angle=PI/4
weight=1
counter=0
class MyLine():
    def render(self, centerX, centerY, angle):
        x1 = centerX-cos(angle)*length/2
        y1 = centerY + sin(angle)*length/2
        x2 = centerX + cos(angle)*length/2
        y2 = centerY - sin(angle)*length/2
        stroke(50, 100)
        strokeWeight(weight)
        line(x1 , y1 , x2 , y2)
        strokeWeight(5)
        stroke(50)
        line(x2 , y2 , x2 , y2)
        line(x1 , y1 , x1 , y1)
MyLine = MyLine()
def setup():
    global MyLine
    size(500, 500)
    smooth()
    background(255)
   
def draw():
    global counter
    counter += 0.05
    if counter > 2*PI:
        counter = 0
    MyLine.render(width/2 + sin(counter)*50, width/2 + cos(counter)*50, counter*2)   
