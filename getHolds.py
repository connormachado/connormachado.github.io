import pyautogui
import numpy as np
import time

from PIL import Image
from pynput.mouse import Listener as mouseListener
from pynput.keyboard import Listener as keyboardListener
from pynput import mouse
from pynput import keyboard

#Local Python
import makeImage


#SUPER NOTE
# make it so you draw the outline of you and then make an animation of the drawing.



allShapes = [] #The complete list of shapes allShapes = [x,y...]  where x&y = type.Lists
corners = [] #The list for the cornerBoundaries corners = [(x,y)...] where x&y = type.Floats
cornerNumber = 0 #Incerement for the first 4 clicks. Then send the coordinates to xPos and yPos
shapeCount = 0 #Once the sinceSave gets to multiple of 5 we print out allShapes in order to "autosave"

xPos = [] # The current xPositions for the current hold || Cleared every right mouse click
yPos = [] # Same but for yPositions

image = Image.open("testImage.jpg")
image.show()

#Orient window
time.sleep(5)
print("Capture corners...")
print("Top Left...")


#NOTE Might not need this
# Gets keyboard input on_press
def on_press(key):
    try:
        print("Key Pressed || {0}".format(key))
    except AttributeError:
        print("Special Key || {0}".format(key))


# Gets keyboard input on_release
# Quits program on key esc, saving all progress to terminal
def on_release(key):
    if key == keyboard.Key.esc:
        # This will be the last click, to print out the full set of holds
        
        #Print allShapes to terminal
        print("allShapes || ", allShapes)
        print("\n")
        print("corners || ", corners)
        return False
    elif key == keyboard.Key.cmd:
        print("Drawing all shapes...")
        makeImage.makeMyImage(corners, allShapes)



def on_click(x, y, button, pressed): #Print rounded coordinates (p) store float coordinates (x,y)
    global cornerNumber, shapeCount

    if pressed:
        #(a)
        if button == mouse.Button.left:
            # First four clicks go towards corner list
            # Rest of the clicks go towards mapping holds
            p = pyautogui.position()
            print("X || Y  =  ", p.x, p.y)

            if cornerNumber == 4:
                xPos.append(x)
                yPos.append(y)
                print("X-Positions: ", xPos)
                print("Y-Positions: ", yPos)

            if cornerNumber == 0:
                print("Top Right...")
                cornerNumber += 1
                corners.append( (x, y) )
            elif cornerNumber == 1:
                print("Bottom Left...")
                cornerNumber += 1
                corners.append( (x, y) )
            elif cornerNumber == 2:
                print("Bottom Right...")
                cornerNumber += 1
                corners.append( (x, y) )
            elif cornerNumber == 3:
                print("|| Corners done ||")
                cornerNumber += 1
                corners.append( (x, y) )
                print("Corners: ", corners)


            #Print list of corner (boundary) points
            if cornerNumber < 4: 
                print("Corners: ", corners)
                
            print("\n")
        #(End a)


        #(b)    
        elif button == mouse.Button.right: 
            # print("Fuck yea right click bitch") #First big progress mark, KEEP this line
            
            # This will be used to save a specific hold to the "allShapes" list
            shapeCount += 1
            if(shapeCount % 5) == 0: #Every 5 shapes, print shapes to terminal
                print("All Shapes AutoSave: ", allShapes)

            allShapes.append( xPos.copy() )
            allShapes.append( yPos.copy() )
            
            xPos.clear()
            yPos.clear()

            print("Total Shape Count: ", shapeCount)

            #makeImage.makeMyImage(corners, allShapes)
        #(End b)

        
    
# Keeps the program running AND can have multiple listeners
# This took fucking forever omfg dude good shit on this (Reference 1)
with mouseListener(on_click=on_click) as listener:
    with keyboardListener(on_press=on_press, on_release=on_release) as listener:
        listener.join()



"""
Future Goal
Around where the current mouse is project a 'zoomed in' version to get more precise
and then show that video at an offset from the current mouse position AND based on what hemisphere
we are in, just to make sure that the 'zoomed in' version doesnt intersect outside where the current viewing pane
"""