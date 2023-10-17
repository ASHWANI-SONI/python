import cv2

img = cv2.imread('logo.png')

cv2.imshow('Title idhar aataa', img)
gray = cv2.imread('logo.png', cv2.IMREAD_GRAYSCALE)

cv2.imshow('gray', gray)
#  0 -> infintie time
# 255 miliseconds
#waitKey(time)

cv2.waitKey(0) # program will stop if any key pressed
cv2.destroyAllWindows()
