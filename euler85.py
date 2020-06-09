def rectCounter(x,y):
    size=(x,y)
    sizeY=0
    acc=0
    while sizeY<size[0]:
        sizeX=0
        sizeY+=1
        while sizeX<size[1]:
            sizeX+=1
            rect=0
            for y in range(size[0]):
                if y+sizeY>size[0]: break
                for x in range(size[1]):
                    if x+sizeX>size[1]: break
                    rect+=1
            acc+=rect
    return acc
    

Max=0

for x in range(1,2000):
    tmp=0
    y=1
    while True:
        tmp=rectCounter(x,y)
        if tmp>2000000: break
        y+=1
    while True:
        tmp=rectCounter(x,y)
        if tmp<2000000: break        
        y-=1
    if tmp>Max: 
        Max=tmp 
        print("-->",Max,x,y,x*y)
