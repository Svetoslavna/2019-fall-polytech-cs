add_library("sound")
import random
bands = 512
play_state = True
spectrum = [0.0 for i in range(0, bands)]
my_bands = 128
resolution = bands/my_bands

def setup():
    global fft,  bg, sf
    size(1107, 683)
    fill(255)
    stroke(255)
    strokeWeight(2)
    bg = loadImage("back.jpg")
    sf = SoundFile(this, "test.mp3")
    sf.loop()
    fft = FFT(this, bands)
    fft.input(sf)
    
def draw():
    global fft, resolution, bg
    background(bg)
    spectrum = fft.analyze()
    filter_size = int(len(spectrum)/2)
    spectrum = spectrum[:filter_size]
    resolution = filter_size/my_bands
    
    translate(width/2, height/2)
    for i in range(0, my_bands):
        angle = i*2*PI/my_bands
        rotate(2*PI/my_bands)
        line_len = height/4 + (mean(spectrum[i*resolution:(i+1)*resolution]) * 5 * sin(angle))
        print(str(line_len) + ":ANGLE:" + str(angle))
        line(0,0,0,line_len)

def mouseClicked():
    global sf, play_state
    if play_state:
        sf.stop()
        play_state = False
    else:
        sf.play()
        play_state = True

def mean(data):
    return (sum(data)*50/len(data))
