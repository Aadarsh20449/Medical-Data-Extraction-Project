import cv2
import numpy as np

def preprocess_image(img):
    #use ADAPTIVE THRESHOLDING 
    #convert colorful image to gray backgoround image
    gray = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)
    resized_image = cv2.resize(gray,None,fx=1.5,fy=1.5,interpolation=cv2.INTER_LINEAR)
    processed_image = cv2.adaptiveThreshold(
        resized_image,255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        61#trail and error value BLOCK SIZE
        ,
        11#trail and error value C value constant
    )
    return processed_image