import cv2 as cv
capture = cv.VideoCapture(0)

while True:
    isTrue, img = capture.read()
    cv.imshow("video", img)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

cv.imwrite("rayon.png", img)
capture.release
cv.destroyAllWindows()
