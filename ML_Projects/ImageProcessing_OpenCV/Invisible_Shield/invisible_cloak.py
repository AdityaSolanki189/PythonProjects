import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
back= cv.imread('./background.jpg')

while cap.isOpened():
    #take each frame
    ret, frame = cap.read()

    if ret:
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        #cv.imshow("hsv",hsv)

        #get hsv value of red
        #lower: hue-10,100,100; higher: hue+10,255,255
        red = np.uint8([[[0,0,255]]]) #bgr red
        hsv_red = cv.cvtColor(red, cv.COLOR_BGR2HSV)
        #print(hsv_red)

        #threshold the hsv value to get only red colors
        l_red = np.array([0, 100, 100])
        u_red = np.array([10,255,255])

        #only the red color is now highlighted in the webcam
        mask = cv.inRange(hsv, l_red, u_red)
        #cv.imshow("mask",mask)

        #now we mask red with our background image
        #bitwise and replaces all red with background image
        part1 = cv.bitwise_and(back, back, mask=mask)
        #cv.imshow("part1", part1)
        
        #unmask
        mask = cv.bitwise_not(mask)

        #all things not red
        part2 = cv.bitwise_and(frame, frame, mask=mask)
        #cv.imshow("mask", part2)
        
        cv.imshow("mask", part1+part2)


        if cv.waitKey(5) == ord('q'):
            break

cap.release()
cv.destroyAllWindows()
