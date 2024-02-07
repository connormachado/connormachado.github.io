from PIL import Image
import numpy as np


# xPos = [206, 299, 328, 273, 206]
# yPos = [625, 544, 615, 663, 625]

corners = [(5.71484375, 81.31640625), (751.25, 81.25), (1.828125, 1210.9765625), (751.4296875, 1222.9296875)]

allShapes = [[175.8828125, 270.1796875, 301.3125, 247.7734375], [595.4921875, 513.1796875, 585.79296875, 634.08203125],
             [316.3125, 309.5625, 350.3125, 329.140625], [456.17578125, 496.3828125, 509.42578125, 484.98046875], 
             [380.48046875, 391.8203125, 418.23046875, 426.11328125, 420.19140625, 399.125], [415.40234375, 390.2578125, 387.9375, 403.6875, 425.125, 429.0625], 
             [267.98046875, 292.84375, 290.078125], [488.36328125, 475.76171875, 504.515625]]


#Used to get the offset correct
# Rounds the floats to integers
for elem in range(len(corners)):
    corners[elem][0] = int(round(corners[elem][0], 0))
    corners[elem][1] = int(round(corners[elem][1], 0))

print(corners)

# Find min and max for each x and y points
xMin = min( corners[0][0], corners[2][0] )
xMax = min( corners[1][0], corners[3][0] )

yMin = min( corners[0][1], corners[1][1] )
yMax = min( corners[2][1], corners[3][1] )

# Width and height of the given canvas/photo
width = xMax - xMin
height = yMax - yMin


#Make empty array of all white pixels
ar = np.ones(( height, width, 3), dtype = np.uint8)
image = 255 * ar


# Takes the points clicked by the user and returns an image
# Returned image has white background and black lines that go between points
def addHold(xPos, yPos, img):
    #Start the linear extrapolation
    for iteration in range(len(xPos) - 1):
        x1 = xPos[iteration + 1]
        x0 = xPos[iteration]
        
        y1 = yPos[iteration + 1]
        y0 = yPos[iteration]

        dx = x1 - x0
        dy = y1 - y0
        m = dy / dx

        # Makes sure that the for loop can run i.e. -> start < stop
        if x1 < x0: 
            tempX = x1
            x1 = x0
            x0 = tempX

            tempY = y1
            y1 = y0
            y0 = tempY


        for x in range(x0, x1):
            y = (m * (x - x0)) + y0
            y = int(round(y, 0))
            x = int(round(x, 0))


            #Add "Thickness"
            # for a in range(-1, 1):
            #     for b in range(-1, 1):
            #         img[x+a][y+b] = (0, 0, 0)


            #Bruh idk how these are different
            img[x][y+1] = (0, 0, 0)
            img[x][y] = (0, 0, 0)
            img[x][y-1] = (0, 0, 0)        
            img[x-1][y+1] = (0, 0, 0)
            img[x-1][y] = (0, 0, 0)
            img[x-1][y-1] = (0, 0, 0)        
            img[x+1][y+1] = (0, 0, 0)
            img[x+1][y] = (0, 0, 0)
            img[x+1][y-1] = (0, 0, 0)
    return img


# Clean and then draw holds
# Rounds all floats to integers || Adds one extra point to end of xPos and yPos
for elemList in range( len(allShapes) ):
    for elem in range( len(allShapes[elemList]) ):
        allShapes[elemList][elem] = int( round(allShapes[elemList][elem], 0) )
    allShapes[elemList].append(allShapes[elemList][0])


#For testing delete later
print(allShapes)


# Goes through allShapes and adds each hold to the image
for iter in range(0, len(allShapes), 2 ):
    img = addHold(allShapes[iter], allShapes[iter + 1], image)


# Use PIL to create an image from the new array of pixels
array = np.array(img, dtype=np.uint8)
new_image = Image.fromarray(array)
#new_image.show()
new_image.save('test2.png')