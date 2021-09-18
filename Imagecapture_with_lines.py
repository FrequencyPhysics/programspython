# importing cv2
import cv2
# path
path = r'C:\Mouse cursor\gon.png'
# Reading an image in default mode
image = cv2.imread(path)
# Window name in which image is displayed
window_name = 'Image'
# Start coordinate, here (0, 0)
# represents the top left corner of image
start_point = (0, 0)
# End coordinate, here (250, 250)
# represents the bottom right corner of image
end_point = (250, 250)
# Green color in BGR
color = (0, 255, 0)
# Line thickness of 9 px
thickness = 9
# Using cv2.line() method
# Draw a diagonal green line with thickness of 9 px
image = cv2.line(image, start_point, end_point, color, thickness)
# Displaying the image
cv2.imshow(window_name, image)

start2 = (250,-20)
end2 = (-20,250)

image = cv2.line(image, start2, end2, color, thickness)
cv2.imshow(window_name,image)

start3 = (250,115)
end3 = (-20,115)

image = cv2.line(image, start3, end3, color, thickness)
cv2.imshow(window_name,image)

start4 = (115,250)
end4 = (115,0)

image = cv2.line(image, start4, end4, color, thickness)
cv2.imshow(window_name,image)

cv2.waitKey(0)
