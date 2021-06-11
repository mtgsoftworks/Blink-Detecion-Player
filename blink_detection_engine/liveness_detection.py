import cv2
import f_liveness_detection
import cv2
import numpy as np
import imutils
import time
import os
import pathlib
import sys

#!/usr/bin/env python
#-*-coding:utf-8-*-

def bounding_box(img,box,match_name=[]):
    for i in np.arange(len(box)):
        x0,y0,x1,y1 = box[i]
        img = cv2.rectangle(img,
                      (x0,y0),
                      (x1,y1),
                      (0,255,0),3);
        if not match_name:
            continue
        else:
            cv2.putText(img, match_name[i], (x0, y0-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)
    return img


# inicializar conteo de parpadeos
COUNTER,TOTAL = 0,0
input_type = "webcam"

#----------------------------- Video ------------------------------
if input_type == "webcam":
    cv2.namedWindow("Blink Detection Engine")
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    while True:
                     
        star_time = time.time()
        ret, im = cam.read()
        im = imutils.resize(im, width=750)
        # veri akışını girin
        out = f_liveness_detection.detect_liveness(im,COUNTER,TOTAL)
        boxes = out['box_face_frontal']+out['box_orientation']
        tags = out['emotion']+out['orientation']
        TOTAL= out['total_blinks']
        COUNTER= out['count_blinks_consecutives']
        res_img = bounding_box(im,boxes,tags)

        f = open(os.path.abspath(os.path.dirname(sys.argv[0])) + "\\data_settings\\eye_movement.txt","w")
        f.write(str(out['orientation']))
        f.close()
        
        f2 = open(os.path.abspath(os.path.dirname(sys.argv[0])) + "\\data_settings\\face_detection.txt","w")
        f2.write(str(out['emotion']))
        f2.close()

        f3 = open(os.path.abspath(os.path.dirname(sys.argv[0])) + "\\data_settings\\number_of_blinks.txt","w")
        f3.write(str(TOTAL))
        f3.close()        

        end_time = time.time() - star_time    
        FPS = 1/end_time
        cv2.putText(res_img,f"FPS: {round(FPS,3)}",(10,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
        cv2.putText(res_img,f"blinks: {round(TOTAL,3)}",(10,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
        cv2.imshow('Privew',res_img)
        if cv2.waitKey(1) &0xFF == ord('q'):           
            break

              
