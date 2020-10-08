import cv2
import imutils
img=cv2.imread("test_image.png")
resize=imutils.resize(img,width=20)
cv2.imwrite("resizedImage.jpg",resize)