import face_recognition
import cv2
import numpy as np
import os
import glob

## get images
faces_encodings = []
faces_names = []
cur_direc = os.getcwd()
print(cur_direc)
path = os.path.join(cur_direc, 'data/faces/')
list_of_files = [f for f in glob.glob(path+'*.jpg')]
number_files = len(list_of_files)
print(number_files)
names = list_of_files.copy()
print(names)

##train faces
for i in range(number_files):
    globals()['image_{}'.format(i)] = face_recognition.load_image_file(list_of_files[i])
    globals()['image_encoding_{}'.format(i)] = face_recognition.face_encodings(globals()['image_{}'.format(i)])[0]
    faces_encodings.append(globals()['image_encoding_{}'.format(i)])
# Create array of known names
    names[i] = names[i].replace(cur_direc, "")  
    faces_names.append(names[i])
    
    
    