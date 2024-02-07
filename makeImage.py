from PIL import Image
import numpy as np


# corners = [(7.69921875, 126.66015625), (750.73828125, 141.1484375), (7.3515625, 1198.34375), (749.37109375, 1214.1796875)]

# allShapes = [[60.87890625, 130.15234375, 149.43359375, 114.0, 76.80078125], [978.98046875, 947.5078125, 996.33203125, 1021.39453125, 1024.87109375], 
#              [177.73046875, 271.05859375, 299.01171875, 247.390625], [592.22265625, 512.8984375, 585.53515625, 631.0234375], 
#              [465.16015625, 497.03125, 491.41796875], [324.5234375, 311.7890625, 333.83203125], 
#              [683.44921875, 688.765625, 708.9609375, 716.92578125, 705.72265625], [1004.76171875, 994.62890625, 987.5, 994.05859375, 1004.8125], 
#              [421.4296875, 448.71875, 442.66015625, 407.5390625], [739.2109375, 757.34765625, 770.06640625, 751.55859375]]

def makeMyImage(corners, allShapes):
    # Rounds elems in list "corners" from floats to integers
    for elem in range(len(corners)):
        corners[elem] = ( int(round(corners[elem][0], 0)), 
                        int(round(corners[elem][1], 0)) )


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
        #Start the linear extrapolation (2)
        for iteration in range(len(xPos) - 1):
            x1 = xPos[iteration + 1]
            x0 = xPos[iteration]
            
            y1 = yPos[iteration + 1]
            y0 = yPos[iteration]

            #Vectors from A to B
            vx = x1 - x0
            vy = y1 - y0

            step = 50
            for iter in range(step):
                x = x0 + (vx * iter / step)
                y = y0 + (vy * iter / step)

                x = int(round(x,0))
                y = int(round(y,0))

                img[y][x] = (0, 0, 0)


                #Add "Thickness"
                for a in range(-1, 1):
                    for b in range(-1, 1):
                        img[y+a][x+b] = (0, 0, 0)


                #Bruh idk how these are different but bottom one is bolder
                # img[y][x+1] = (0, 0, 0)
                # img[y][x] = (0, 0, 0)
                # img[y][x-1] = (0, 0, 0)        
                # img[y-1][x+1] = (0, 0, 0)
                # img[y-1][x] = (0, 0, 0)
                # img[y-1][x-1] = (0, 0, 0)        
                # img[y+1][x+1] = (0, 0, 0)
                # img[y+1][x] = (0, 0, 0)
                # img[y+1][x-1] = (0, 0, 0)
        return img


    # Clean and then draw holds
    # Rounds all floats to integers || Adds one extra point to end of xPos and yPos
    # Also accounts for offset
    subtractor = yMin
    for elemList in range( len(allShapes) ):
        if elemList%2 == 0:
            subtractor = xMin
        else:
            subtractor = yMin

        for elem in range( len(allShapes[elemList]) ): #This code applies the correct x OR y offset to EVERY point
            allShapes[elemList][elem] = int( round(allShapes[elemList][elem], 0) ) - subtractor
        allShapes[elemList].append(allShapes[elemList][0]) #Adds in the 'closing' point, so our shape is a polygon and not a snake


    # Goes through allShapes and adds each hold to the image
    for iter in range(0, len(allShapes), 2 ):
        img = addHold(allShapes[iter], allShapes[iter + 1], image)


    # Use PIL to create an image from the new array of pixels
    array = np.array(img, dtype=np.uint8)
    new_image = Image.fromarray(array)
    new_image.show()
    #new_image.save('test2.png')