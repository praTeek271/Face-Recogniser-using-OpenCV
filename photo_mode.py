import cv2
import os
import numpy as np
import faceRecognition as fR
import time
import os
from tqdm import tqdm
directory = os.getcwd()

test_img=cv2.imread(directory+'/TestImages/20210918_122411.jpg') 

# test_img path

faces_detected,gray_img=fR.faceDetection(test_img)
print("faces_detected:",faces_detected  )

if "trainingData.yml" not in os.listdir(directory):
    faces,faceid= fR.labels_for_training_data('./trainingImages')
    face_recognizer =fR.train_classifier(faces,faceid)
    face_recognizer.save('trainingData.yml')
    name={0:"Priyanka",1:"Kangana",2:"Robert Dowery Jr.",3:"Lauren German",4:"Tom Ellis"}

else:
    face_recognizer=cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.read('trainingData.yml')
    name={0:"Priyanka",1:"Kangana",2:"Robert Dowery Jr.",3:"Lauren German",4:"Prateek kumar singh",5:"Tom Ellis"}


for face in faces_detected:
    (x,y,w,h)=face
    roi_gray=gray_img[y:y+h,x:x+h]                                   # extracting the region
    label,confidence=face_recognizer.predict(roi_gray)
    print(f"Label : {label}\nConfidence_Score : {confidence}")    # prints the values stored
    
    fR.draw_rect(test_img,face)
    predicted_name=name[label]
    if confidence>37:
        continue
    fR.put_text(test_img,predicted_name,x,y)

#-------------------------------------------------------------------------------------------------------------------------------- 


    # for (x,y,w,h) in faces_detected:
    #     cv2.rectangle(test_img,(x,y),(x+w,y+h),(250,0,0),thickness=5)

resized_img=cv2.resize(test_img,(1000,900))
cv2.imshow("face-detected",resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows() 
