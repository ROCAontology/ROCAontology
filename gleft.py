from PIL import Image, ImageDraw
import math, random

def color(i):
    return {0:(100, 70, 0), #vert très très foncé
            1:(224, 224, 224), #gris clair 
            2:(112, 115, 29), #vert foncé
            3:(153, 0, 0 ), #brun
            4:(255, 128, 10), #orange
            5:(246, 224, 115) #tan
            }[i]

def drawTriangle(x,y, color, mode, image):
    #x,y index
    e = 12
    draw = ImageDraw.Draw(image)
    ed = [(e*(x),e*(y)), (e*(x+1),e*(y)), (e*(x+1),e*(y-1)), (e*(x),e*(y-1))]
    if mode==0:
        draw.polygon([ed[0],ed[1],ed[3]], fill = color)
    if mode==1:
        draw.polygon([ed[0],ed[2],ed[3]], fill = color)
    if mode==2:
        draw.polygon([ed[1],ed[2],ed[3]], fill = color)
    if mode==3:
        draw.polygon([ed[0],ed[1],ed[2]], fill = color)
    if mode==4:
        draw.polygon(ed, fill=color)

output = Image.new(mode = "RGBA", size = (600,1200), color=(200,200,200,0))
#get image data from csv
with open("leftdata.csv", "r") as f:
    data = f.readlines()

for i in range(len(data)):
    line = data[i]
    try:
        cells = line[:-1].split(";")
        for j in range(len(cells)):
            c = cells[j]
            try:
                d = c.split(",")
                colorcode = int(d[0])
                mode = int(d[1])
                drawTriangle(j,i,color(colorcode),mode,output)
            except:
                error = 0
    except:
        print("Error: could not extract cells")

output.save("left.png")


output = Image.new(mode = "RGBA", size = (600,2000), color=(200,200,200,0))
#get image data from csv
with open("leftdata.csv", "r") as f:
    data = f.readlines()

for i in range(len(data)):
    line = data[i]
    try:
        cells = line[:-1].split(";")
        for j in range(len(cells)):
            c = cells[j]
            try:
                d = c.split(",")
                colorcode = int(d[0])
                mode = int(d[1])
                drawTriangle(j,i,color(colorcode),mode,output)
            except:
                error = 0
    except:
        print("Error: could not extract cells")

output.save("left.png")
