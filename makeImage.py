from PIL import Image
import numpy as np


# pixels = [
#    [(54, 54, 54), (232, 23, 93), (71, 71, 71), (168, 167, 167)],
#    [(204, 82, 122), (54, 54, 54), (168, 167, 167), (232, 23, 93)],
#    [(71, 71, 71), (168, 167, 167), (54, 54, 54), (204, 82, 122)],
#    [(168, 167, 167), (204, 82, 122), (232, 23, 93), (54, 54, 54)]
# ]

# pixels = []
# for y in range(2280):
#     for x in range(1284):
#         pixels.append( (255,255,255) )


img = np.ones(( 2280, 1284, 3), dtype = np.uint8)
img = 255 * img

# Convert the pixels into an array using numpy
array = np.array(img, dtype=np.uint8)

# Use PIL to create an image from the new array of pixels
new_image = Image.fromarray(array)
new_image.save('test2.png')