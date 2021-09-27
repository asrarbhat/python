import cv2 as cv
import numpy as np

capture = cv.VideoCapture(0)
fps = 25

out = cv.VideoWriter(
    "abc.avi", cv.VideoWriter_fourcc(*'XVID'), fps, (640, 480))

while(capture.isOpened()):
    ret, frame = capture.read()
    if ret == True:

        # write the flipped frame
        out.write(frame)

        cv.imshow('frame', frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

out.release
capture.release
cv.destroyAllWindows()
