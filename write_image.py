import cv2
img=cv2.imread("test_image.png")
img2=cv2.imwrite("new_image.png",img)
cv2.imshow("frame",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()