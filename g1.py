"""
Hides suspicious characters in a picture.
"""
from PIL import Image, ImageDraw
import math, random

output = Image.new(mode = "RGB", size = (1,1200), color=(0,255,255))


def middle(c1, c2):
    r = int((c1[0]+c2[0])/2)
    g = int((c1[1]+c2[1])/2)
    b = int((c1[2]+c2[2])/2)
    return (r,g,b)

def cleanDoubles(r):
    res = []
    for e in r:
        if not e in res:
            res.append(e)
    return res
def gradient(c1, c2, l):
    if l == 0:
        return [c1, middle(c1,c2), c2]
    else:
        res = []
        grad = gradient(c1, c2, l-1)
        res.append(grad[0])
        for i in range(0,len(grad)-1):
            res.append(middle(grad[i],grad[i+1]))
            res.append(grad[i+1])
    return res #cleanDoubles(res)


def blend(picture, y, s):
    #blending, centered on y
    c1 = picture.getpixel((0, y-1))
    c2 = picture.getpixel((0, y+1))
    g = gradient(c1, c2, s)
    l = int(len(g)/2)
    for i in range(0, 2*l):
        picture.putpixel((0,y - l + i), g[i])

for i in range(0,600):
    output.putpixel((0,i), (246,224,115))

for i in range(600,900):
    output.putpixel((0,i), (179,80,30))

for i in range(900,1200):
    output.putpixel((0,i), (50,10,10))
    
    
blend(output, 600, 8)        
blend(output, 900, 5)    
    
output.save("background.png")