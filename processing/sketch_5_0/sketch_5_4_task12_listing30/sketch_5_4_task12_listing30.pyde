l1x1 = 0
int(l1x1)
l1y1 = 0
int(l1y1)
l1x2 = 500
int(l1x2)
l1y2 = 500
int(l1y2)
flug = 1
int(flug)
mr = 10
float(mr)
mg = 150
float(mg)
mb = 100
float(mb)
def setup():
    background(255)
    size(500, 500)
    smooth()

def draw():
    global mr,mg,mb,l1x1,l1y1,l1x2,l1y2,flug
    background(0) 
    strokeWeight(120)
    stroke(mr , mg , mb , 25)
    line(l1x1 , l1y1 , l1x2 , l1y2)
    for i in range(1,11,1):
        k = i*50
        int(k)
        stroke(mr , mg , mb , (255/11)*i)
        line(l1x1 + k, l1y1 , l1x2 , l1y2 - k)
        line(l1x1 , l1y1 + k, l1x2 - k, l1y2)

        if(l1x1 == l1x2 or (l1x1 + k) == l1x2 or l1x1 == (l1x2
        - k)):
            mr = random(0,150)
            mg = random(0,150)
            mb = random(0,150)

        l1x1 = l1x1 + flug
        l1y1 = l1y1 + flug
        l1x2 = l1x2 - flug
        l1y2 = l1y2 - flug
        if(l1y2 < 0 or l1y2 > 500):
            flug = flug*(-1)
