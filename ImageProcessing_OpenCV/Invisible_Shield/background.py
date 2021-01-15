import cv2
# access webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, back = cap.read()  #read from webcam
    if ret:
        cv2.imshow("image", back)
        if cv2.waitKey(5) == ord('q'):
            #capture the image
            cv2.imwrite('background.jpg', back)
            break

cap.release()
cv2.destroyAllWindows()