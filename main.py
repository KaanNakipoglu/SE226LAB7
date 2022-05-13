import cv2
import cv2 as cv
import numpy as np

image = cv.imread('sad.jpeg', cv.IMREAD_COLOR)
blue,green,red = cv.split(image)
cv.imshow("blue",blue)
cv.imshow("green",green)
cv.imshow("red",red)
cv.imshow("hello",image)
blue=blue + 102
green=green + 30
red=red + 5
newİmage= cv.merge((blue,green,red))
cv.imshow("newhello",newİmage)
cv.waitKey(0)
cv.destroyAllWindows()