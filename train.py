import face_recognition
import picamera
import numpy as np
from time import sleep
import pickle
import os

camera = picamera.PiCamera()
camera.resolution = (320, 240)
output = np.empty((240, 320, 3), dtype=np.uint8)


# Initialize some variables
face_locations = []
face_encodings = []

isFound = False

print("Looking for faces : ")

while not isFound:
    print(". . .")
    # Grab a single frame of video from the RPi camera as a numpy array
    camera.start_preview(fullscreen=False, window = (100, 20, 640, 480))
    sleep(5)
    camera.capture(output, format="rgb")
    camera.stop_preview()
    
    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(output)

    if(len(face_locations)==1):
        
        
        face_encodings = face_recognition.face_encodings(output, face_locations)

        # Loop over each face found in the frame to see if it's someone we know.
        text = input("Enter name : ")
        id = input("Enter id : ")
        os.makedirs('dataset/{}'.format(id))
        
        
        with open('dataset/{}/{}.dat'.format(id,text), 'wb') as f:
            pickle.dump(face_encodings[0], f)
            
        isFound = True
        
        
        
        
