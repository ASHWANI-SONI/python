'''
    Write a Python Scipt that captures images
    from your webcam video stream 
    Extracts all faces from the image frame(using HaarCascade)
    Stores the Fcae information into numpy arrays

    1.Read and show video stream, capture images
    2. Detect faces and show bounding box
    3. Flatten the largest face image(grayscale) and save in a numpy array
    4. Repeat the above for multiple people to generate training data

'''

import cv2
import numpy as np

#Intit Camera
cap = cv2.VideoCapture(0)

# Face Detection
face_cascade = cv2.CascadeClassifier("/Users/ashwanisoni/Documents/Courses/Python/opencv-test/haarcascade_frontalface_alt.xml")
skip = 0
face_data = []
dataset_path = './data/'
file_name = input("Enter the name of person")

while True:

    ret, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if ret == False:
        continue

    faces = face_cascade.detectMultiScale(gray_frame, 1.3, 5)
    faces = sorted(faces, key = lambda f:f[2]*f[3])

    # print(faces)
    for face in faces[-1:]:
        (x, y, w, h) = face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)

        #Extract (Crop out the required face) : Region of Interest
        offset = 10
        face_section = frame[y-offset:y+h+offset, x-offset:x+w+offset]
        face_section = cv2.resize(face_section, (100, 100))
        
        skip += 1
        # Store every 10th face
        if skip%10==0:
            face_data.append(face_section)
            print(len(face_data))
        cv2.imshow("section",face_section)

    cv2.imshow("dekhle", frame)


    key_pressed = cv2.waitKey(1) & 0xFF
    if key_pressed == ord('q'):
        break

# Convert our face list array into a nupy array
face_data = np.asarray(face_data)
face_data = face_data.reshape((face_data.shape[0], -1))
print(face_data.shape)

np.save(dataset_path+file_name+'.npy', face_data)
print("Data Successfully saved!!")
cap.release()
cv2.destroyAllWindows()