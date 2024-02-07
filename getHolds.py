from PIL import Image
import pyautogui
from pynput.mouse import Listener
from pynput import mouse
from pynput import keyboard

allShapes = [] #The complete list of shapes allShapes = [x,y...]  where x&y = type.Lists
cornerBoundary = [] #The list for the cornerBoundaries cornerBoundary = [(x,y)...] where x&y = type.Floats
corners = 0 #Incerement for the first 4 clicks. Then send the coordinates to xPos and yPos
shapeCount = 0 #Once the sinceSave gets to 5 we print out allShapes in order to "autosave"

# Later on i have to subtract every hold with the offset of the four corners I captured earlier

xPos = [] # The current xPositions for the current hold || Cleared every right mouse click
yPos = [] # Same but for yPositions

image = Image.open("testImage.jpg")
image.show()



def on_click(x, y, button, pressed): #Print rounded coordinates (p) store float coordinates (x,y)
    global corners, shapeCount

    if pressed:

        #(1)
        if button == mouse.Button.left:
            #(1)
            #######################################################
            ##  Print out the added coordinates and the first    ##
            ##   4 clicks that were sent to the coordinates list ##
            ######################################################
            p = pyautogui.position()
            print("X || Y  =  ", p.x, p.y)


            if corners == 4:
                xPos.append(x)
                yPos.append(y)
                print("X-Pos: ", xPos)
                print("Y-Positions: ", yPos)


            if corners == 0:
                print("Top Left")
                corners += 1
                cornerBoundary.append( (x, y) )
            elif corners == 1:
                print("Top Right")
                corners += 1
                cornerBoundary.append( (x, y) )
            elif corners == 2:
                print("Bottom Left")
                corners += 1
                cornerBoundary.append( (x, y) )
            elif corners == 3:
                print("Bottom Right")
                corners += 1
                cornerBoundary.append( (x, y) )
                
            if corners < 5: #Show corners
                print("Corners: ", cornerBoundary)
                
            print("\n")
        #(End 1)


        #(2)    
        elif button == mouse.Button.right: 
            #(2)
            # This will be used to save a specific piece 
            # and move onto the next one, has to clear 
            # the variable 'Boundary' in order to 
            # be able to build a new hold
            shapeCount += 1
            if(shapeCount % 5) == 0: #Every 5 saves, can change later
                print("All Shapes AutoSave: ", allShapes)

            allShapes.append( xPos )
            allShapes.append( yPos )
            xPos.clear()
            yPos.clear()

            print("Total Shape Count: ", shapeCount)


            # print("Fuck yea right click bitch")
        #(End 2)


        #(3)
        elif button == mouse.Button.middle:
            pass
            #(3)
            # This will be the last click, to print out the full set of holds
            # The other two will have autosave stuff in order to be able to map
            # the whole image over a couple program runs instead of hours of straight work
            #this AND the other autosave function should have another file that will join the 
            # two lists into one mega list
        #(End 3)
        

    
with Listener(on_click=on_click) as listener:
    listener.join()
    

    

"""
Future Goal
around where the current mouse is project a 'zoomed in' version to get more precise
and then show that video at an offset from the current mouse position AND based on what hemisphere
we are in, just to make sure that the 'zoomed in' version doesnt intersect outside where the current viewing pane
"""


