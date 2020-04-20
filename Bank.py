#RFID
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
#facerecognition
import face_recognition
import picamera
import numpy as np
import pickle

camera = picamera.PiCamera()
camera.resolution = (320, 240)
output = np.empty((240, 320, 3), dtype=np.uint8)

reader = SimpleMFRC522()

try:
        print("Place your access card : ")
        id, text = reader.read()
        #print(id)
        #print(text)
        print("Customer Verified : ",text)
        print("Loading authorized bank employee's face image(s)")
        harshal_image = face_recognition.load_image_file("harshal.jpg")
        
        with open('dataset/7/harshal.dat', 'rb') as f:
            harshal_face_encoding = pickle.load(f)    
        
        
        face_locations = []
        face_encodings = []

        isFound = False

        print("Looking for faces : ")

        while not isFound:
            print(". . .")
            # Grab a single frame of video from the RPi camera as a numpy array
            camera.capture(output, format="rgb")

            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(output)

            if(len(face_locations)>0):
                face_encodings = face_recognition.face_encodings(output, face_locations)

                # Loop over each face found in the frame to see if it's someone we know.
                for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                    match = face_recognition.compare_faces([harshal_face_encoding], face_encoding)
            
                    if match[0]:
                        name = "Harshal Mandlekar"
                        print("Identified as : {}!".format(name))
                        print("Access Granted")
                        isFound = True
                    else:
                        print("Not matched")

        

except Exception as e:
    print(e)
        
        
finally:
        GPIO.cleanup()