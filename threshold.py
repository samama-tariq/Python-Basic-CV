import cv2
import imutils
img=cv2.imread("test_image.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,threshold=cv2.threshold(gray,220,255,cv2.THRESH_BINARY)
cv2.imwrite("ThreshImage.jpg",threshold)