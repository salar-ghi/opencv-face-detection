import cv2

img = cv2.imread('assets/logo.png', 1)
img = cv2.resize(img, (0,0) , fx= 0.5, fy= 0.5)
img = cv2.rotate(img, rotateCode=cv2.ROTATE_90_COUNTERCLOCKWISE)


# -1, cv2.IMREAD_COLOR : Loads a color image. any transparency of image
# 0, cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
# 1, cv2.IMREAD_UNCHANGED : Loads image as such including alpha chqannel 
cv2.imshow('Image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()