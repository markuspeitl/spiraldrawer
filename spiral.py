import cv2
import numpy as np


def drawSpiral(p0,startAngle,img):
    stepsize = 0.1

    granularity = 200

    for t in range(0,10000):
        smallt = t/granularity
        #if( smallt % (2*np.pi) < 0.2 ):
        #x =  int( 10 * smallt * np.cos(smallt * 0.1) * np.cos(startAngle + smallt) + zeroP[0] )
        #y =  int( 10 * smallt * np.cos(smallt * 0.1) * np.sin(startAngle + smallt) + zeroP[1] )
        x =  int( 10 * smallt * np.abs(np.cos(smallt * 0.3)) * np.cos(startAngle + smallt) + zeroP[0] )
        y =  int( 10 * smallt * np.abs(np.cos(smallt * 0.3)) * np.sin(startAngle + smallt) + zeroP[1] )

        r = np.abs(np.sin(smallt)) * 255
        g = np.abs(np.cos(smallt)) * 255
        b = 0

        if x > 0 and y > 0 and x < img.shape[0] and y < img.shape[1]:
            img[x,y] = [b,g,r]

def drawSpiralNp(p0,startAngle,img):

    granularity = 100

    #timesteps = np.arange(0,10000)
    timesteps = np.arange(0,10000) / granularity
    r = (np.abs(np.sin(timesteps)) * 255).astype(np.uint8)
    g = (np.abs(np.cos(timesteps)) * 255).astype(np.uint8)
    b = 0
    x = ( 10 * timesteps * np.abs(np.cos(timesteps * 0.3)) * np.cos(startAngle + timesteps) + zeroP[0] ).astype(int)
    y = ( 10 * timesteps * np.abs(np.cos(timesteps * 0.3)) * np.sin(startAngle + timesteps) + zeroP[1] ).astype(int)

    np.clip(x, 0, img.shape[0]-1, out=x)
    np.clip(y, 0, img.shape[1]-1, out=y)
    #x[x >= img.shape[0]] = img.shape[0] - 1
    #y[y >= img.shape[1]] = img.shape[1] - 1
    #x[x < 0] = 0
    #y[y < 0] = 0
    #print(x)
    img[x,y,:] = np.array([255,0,0])

#doclearimg = False
#rotationPStep = 1
#refreshMsec = 300

doclearimg = True
rotationPStep = 0.01
refreshMsec = int(1000/20)

clearimg = np.zeros((800,800,3),dtype=np.uint8)
img = np.zeros((800,800,3),dtype=np.uint8)
zeroP = np.array([400,400])

currentRotation = 0

while True:

    if(doclearimg):
        img = np.copy(clearimg)

    drawSpiralNp(zeroP,currentRotation + 0,img)
    drawSpiralNp(zeroP,currentRotation + 0.5 * np.pi,img)
    drawSpiralNp(zeroP,currentRotation + 1.0 * np.pi,img)
    drawSpiralNp(zeroP,currentRotation + 1.5 * np.pi,img)

    cv2.imshow('img',img)
    k = cv2.waitKey(1)
    if(k == ord('a')):
        break

    currentRotation += rotationPStep


#cv2.waitKey()