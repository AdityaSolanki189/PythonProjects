import cv2
import dlib

detector = dlib.get_frontal_face_detector()

cap = cv2.VideoCapture(0)


while True:
    
    ret, frame = cap.read()

    faces = detector(frame)

    print(faces)

    if ret:        
        cv2.imshow("My Screen", frame)
        
    key = cv2.waitKey(30)

    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()