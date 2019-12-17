a = [[500] *2 for a in range(500)]

 
def setup():
    size(500,500)
    stroke(100)
    for i in range(0, len(a), 1):
        for j in range(0, len(a[i]), 1):
            a[i][j] = random(10,490)
            
            
def draw():
    smooth()
    noStroke()
    background(0)
    
    for i in range(0, len(a), 1):
        eDist = dist(mouseX, mouseY, a[i][0], a[i][1])
        eSize = map(eDist,0,200,5,100)
        eColor = map(eDist,0,200,50,255)
        fill(eColor,200)
        
        cx = noise(mouseX)*10 + a[i][0]
        cy = noise(mouseY)*10 + a[i][1]
        ellipse(cx, cy,eSize, eSize)
