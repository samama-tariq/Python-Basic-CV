import cv2
import imutils
img=cv2.imread("test_image.png")
gb=cv2.GaussianBlur(img,(21,21),0)
cv2.imwrite("gb_image.jpg",gb)
