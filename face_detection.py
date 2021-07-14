from types import FrameType
import cv2
from random import randrange



#loading pre-trained data from opencv using haarcascade algorithm
trained_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


# #*********WORKING WITH AN IMAGE**************
# #example of using and image and detecting a face on it
# image = cv2.imread('family.jpg')

# #make that image black and white
# grayscaled_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

# #detect faces, MultiScale detects objects of different sizes in the input image
# face_coordinates = trained_data.detectMultiScale(grayscaled_image)

# #first two numbers tell the position of the upper left corner and width and height
# print(face_coordinates)

# #loop through all the faces
# for(x, y, w, h) in face_coordinates:
# 	#assign coordinates to xywh (x, y, w, h) = face_coordinates[0]
#     #rectangle function(nameoftheimage, (x1, y1), (x1+x2, y1+y2), (bgr rectangle), thickness)
#     cv2.rectangle(image, (x, y), (x+w, y+h), (randrange(256), randrange(256), randrange(256)), 2)



# #opening a windows with imshow, first parameter name od the windows, second image
# cv2.imshow('Face detection', image)
# #window closes only after pressing a key
# cv2.waitKey()


#*********WORKING WTIH A LIVESTREAM*************
#capture video from webcam (0)chooses the default cam
webcam = cv2.VideoCapture(0)
#iterate through all the frames forever till we kill the loop
while True:
    #read the current frame
    successful_frame_read, frame = webcam.read()

    grayscaled_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_coordinates = trained_data.detectMultiScale(grayscaled_image)
    for(x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    cv2.imshow('Face detection', frame)
    #waitKey will capture frames every (x) miliseconds
    key = cv2.waitKey(1) 

    #stop if Q is pressed
    if key == 81 or key == 113:
        break

webcam.release()

print("Code Completed")