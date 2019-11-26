i = 0
int(i)
k = 1
int(k)
flug = 1
int(flug)

def setup():
    size(500, 500)
    smooth()
    background(0)
    strokeWeight(1)
def upDate():
    global i,k
    i+=k
    if(i==255):
        k=-1
    if(i==0):
        k=0
def draw():
    global i
    stroke(i, 20)
    myRandom = random(-20,20)
    myY1 = mouseY - myRandom
    myY2 = mouseY + myRandom
    line(0, myY1, 500, myY2)
    upDate()
    
