import numpy as np 
from PIL import Image

height = 1300
width = 800

#Prepopulate an array
ar = np.ones(( height, width, 3), dtype = np.uint8)
image = 255 * ar
my_array = np.array( image ) 
np.save('image.npy', my_array) 


posses = [[173, 266, 296, 245, 173], 
         [513, 434, 504, 554, 513], 
         
         [587, 615, 629, 606, 587], 
         [749, 729, 751, 767, 749], 
         
         [56, 132, 153, 134, 82, 56], 
         [895, 867, 908, 934, 945, 895], 
         
         [373, 326, 335, 383, 373], 
         [193, 258, 278, 265, 193]]


def addHold(xPos, yPos, img, border = False):
        # If we want to bold the borders of the hold change border to True 
        # Start the linear extrapolation (2)
        # Fills space where a line between 2 points would go with single points
        for iteration in range(len(xPos) - 1):
            x1 = xPos[iteration + 1]
            x0 = xPos[iteration]
            
            y1 = yPos[iteration + 1]
            y0 = yPos[iteration]

            #Vectors from A to B
            vx = x1 - x0
            vy = y1 - y0

            step = 100
            for iter in range(step):
                # thisColor = list(np.random.choice(range(256), size=3))
                thisColor = (0, 0, 255)
                x = x0 + (vx * iter / step)
                y = y0 + (vy * iter / step)

                x = int(round(x,0))
                y = int(round(y,0))

                img[y][x] = thisColor

                if border:
                    #Add "Thickness"
                    for a in range(-1, 1):
                        for b in range(-1, 1):
                            img[y+a][x+b] = thisColor
        return img


def lineScanner(img, xPos, yPos):
    toFill = []
    
    def checkVertex(point = tuple):
        # Returns true if given point is a vertex point
        # xPos[-1] = "looping point", ie its repeated
        for p in range( len(xPos) - 1 ):
            if point == ( yPos[p], xPos[p] ):
                return True
        return False
    
    # Get the top and bottom of the holds
    bottom = max(yPos) + 1
    top = min(yPos) - 1

    left = min(xPos) - 1
    right = max(xPos) + 1

    for row in range(top, bottom): #Iterate over the y-axis
        p1 = (-1, -1) #First intersection of a line
        for column in range(left, right): #Iterate over the x-axis
            if checkVertex( (column, row) ):
                continue
            if len(list(set(img[row][column]))) != 1: #If the pixel isn't white
                if p1[0] == -1: #If we haven't intersected a border yet
                    p1 = (row, column)
                else: #We have already intersected a border and now we're on the other side of it
                    if (p1[1] + 1 == column) or (p1[1] - 1 == column) or (p1[1] - 2 == column) or (p1[1] + 2 == column):# if there are pixel groupings of 2 or 3 in a row   
                        continue
                    toFill.append( (p1, (row, column))) #Append the two points to toFill, then later for loop across the x axis of these points and fill
                    p1 = (-1, -1)
        
        p1 = (-1, -1)
    return toFill

# Draw lines and show new image
for a in range( 0, len(posses), 2):
    loaded_arr = np.load('image.npy')

    xPos = posses[a]
    yPos = posses[a + 1]

    img = addHold(xPos, yPos, my_array)
    fillers = lineScanner(img, xPos, yPos)

    # Fill the points between the scanned lines with random colors
    for pair in fillers:
        row = pair[0][0]
        start = pair[0][1]
        stop = pair[1][1]
        for column in range( start, stop):
            img[row][column] = list(np.random.choice(range(256), size=3))
    
    # Add back the blue border
    img = addHold(xPos, yPos, img, border = True)

    np.save('image.npy', img) 

img = np.load('image.npy')
new_image = Image.fromarray(img)
new_image.show()