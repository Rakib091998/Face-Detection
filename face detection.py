#!/usr/bin/env python
# coding: utf-8

# In[26]:


import cv2 
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
face_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")

img = cv2.imread("a.jpg")

gray_img =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 

faces = face_cascade.detectMultiScale(gray_img, scaleFactor = 1.05, minNeighbors=5) 
print(type(faces)) 
print(faces)


for x,y,w,h in faces:
    img=cv2.rectangle(img, (x,y), (x+w,y+h),(0,255,0),3)

cv2.imshow("Gray", img)

cv2.waitKey(0)
cv2.destroyAllwindows()


# In[ ]:




