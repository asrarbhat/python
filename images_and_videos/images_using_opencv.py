import cv2 as cv

img = cv.imread("download.jpeg")
print(img.shape)
cv.imshow("image", img)

cv.imwrite("hello1.jpeg", img)

cv.waitKey(2000)
