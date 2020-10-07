import cv2
img=cv2.imread("test_image.png")
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("orignial",img)
cv2.imshow("Gray Image",img)
cv2.waitKey(0)
cv2.DestroyAllWindows()