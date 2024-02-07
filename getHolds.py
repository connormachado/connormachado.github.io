from PIL import Image
import pyautogui
from pynput.mouse import Listener as mouseListener
from pynput.keyboard import Listener as keyboardListener
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




def on_press(key):
    try:
        print("Key Pressed || {0}".format(key))
    except AttributeError:
        print("Special Key || {0}".format(key))


def on_release(key):
    
    #Use this as the finalSave button
    if key == keyboard.Key.esc:
        # This will be the last click, to print out the full set of holds
        # The other two will have autosave stuff in order to be able to map
        # the whole image over a couple program runs instead of hours of straight work
        #this AND the other autosave function should have another file that will join the 
        # two lists into one mega list

        
        #Print allShapes to terminal
        print("allShapes || ", allShapes)
        return False



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


            if (corners == 4) or (corners == 5):
                xPos.append(x)
                yPos.append(y)
                print("X-Positions: ", xPos)
                print("Y-Positions: ", yPos)


            if corners == 0:
                print("Top Left Done")
                corners += 1
                cornerBoundary.append( (x, y) )
            elif corners == 4: #Stops corners list printing after 4
                corners += 1
            elif corners == 1:
                print("Top Right Done")
                corners += 1
                cornerBoundary.append( (x, y) )
            elif corners == 2:
                print("Bottom Left Done")
                corners += 1
                cornerBoundary.append( (x, y) )
            elif corners == 3:
                print("Bottom Right Done")
                corners += 1
                cornerBoundary.append( (x, y) )


            if corners != 5: #Show corners
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

            allShapes.append( xPos.copy() )
            allShapes.append( yPos.copy() )
            
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
        
    
# Keeps the program running AND can have multiple listeners
# This took fucking forever omfg dude good shit on this
# https://stackoverflow.com/questions/45973453/using-mouse-and-keyboard-listeners-together-in-python
with mouseListener(on_click=on_click) as listener:
    with keyboardListener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    

"""
Future Goal
around where the current mouse is project a 'zoomed in' version to get more precise
and then show that video at an offset from the current mouse position AND based on what hemisphere
we are in, just to make sure that the 'zoomed in' version doesnt intersect outside where the current viewing pane
"""


