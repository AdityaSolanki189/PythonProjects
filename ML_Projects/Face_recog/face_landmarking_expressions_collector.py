import cv2
import dlib
import os
import numpy as np
#dlib is better than harcascade, as it uses deeplearning. 
#so even when you tilt face or cover partial face, it will be able to recognise
detector = dlib.get_frontal_face_detector()

predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

cap = cv2.VideoCapture(0)

mood = input("Enter Your Expression : ") #happy, sad, wow, neutral etc.

expression = 1
frames = []
outputs = []

while True:
    
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)

    for face in faces:
        landmarks = predictor(gray, face)
        #print(landmarks.parts())
        #nose = landmarks.parts()[27]
        #print(nose.x, nose.y)

        """ lip_up = landmarks.parts()[62].y
        lip_down = landmarks.parts()[66].y

        if lip_down-lip_up > 5:
            print("Mouth is Open!")
        else:
            print("Mouth is Close!")  """

        expression = np.array([[point.x - face.left(), point.y - face.top()] for point in landmarks.parts()[17:]])

    # print(faces)

    if ret:        
        cv2.imshow("My Screen", frame)
        
    key = cv2.waitKey(1)

    if key == ord("q"):
        break

    if key == ord("c"):
        # cv2.imwrite(name + ".jpg", frame)
        frames.append(expression.flatten())
        outputs.append([mood])

X = np.array(frames)
y = np.array(outputs)

data = np.hstack([y, X])

f_name = "face_expressions.npy"

if os.path.exists(f_name):
    old = np.load(f_name)
    data = np.vstack([old, data])

np.save(f_name, data)


cap.release()
cv2.destroyAllWindows()