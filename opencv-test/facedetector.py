import cv2

cap = cv2.VideoCapture(0) 
# VideoCapture(id) id of the camera 0 is for default

face_cascade = cv2.CascadeClassifier("/Users/ashwanisoni/Documents/Courses/Python/opencv-test/haarcascade_frontalface_alt.xml")

while True:
    ret, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if ret == False:
        continue
    
    faces = face_cascade.detectMultiScale(gray_frame, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0,0), 2)

    cv2.imshow("Video_frame", frame)

    key_pressed = cv2.waitKey(1) & 0xFF
    if key_pressed == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

'''
    scaleFactor - parameter specifying how much the image size
    is reduced at each scale.

    Bascially the scale factor is used to create your scale pyramid.
    More explaination can be found here.
    In 1.05 is a good value for this, which means you use a small step
    for resizeing, i.e. reduce size

    number_of_neighbours is no of boxes we will me checking
    5 o6 6 is a good number

'''
