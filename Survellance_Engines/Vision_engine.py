"""Created by Sweta Subhra Datta Praga Bollam And Bhavya Omprakash Agarwal
April 24th,2021
"""
import cv2
import numpy as np
import os




class Vision_Engine():
        backsub = cv2.createBackgroundSubtractorMOG2(history=50, varThreshold=30, detectShadows=False)#These hyperparameters are tuned to give the best results
        facecacade=cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")

        """This method detects motion in a frame by using the concept of background subtraction and checking contourArea
         on a subtracted frame 
         @return:: bool (Motion_Detected)"""

        def Detect_Motion(self,frame):
            Motion_Detected = False
            background=self.backsub.apply(frame)
            median_blur=cv2.medianBlur(background,7)#noise reduction
            #Detect contours
            # cv2.imshow("background_sub",median_blur)
            contours,hierarchy=cv2.findContours(median_blur,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            for cnts in contours:
                if(cv2.contourArea(cnts)>50):
                    Motion_Detected=True
                 #   print("Motion Status",Motion_Detected)
                    break

            # cv2.imshow("frame",median_blur)
            # if cv2.waitKey(1) & 0xFF == ord('q'):
            #     exit("KeyboardInterrupt")
            return Motion_Detected,contours


        """This method detects camera covering or camera obstruction in every frame       
        @return bool(Tamper Detected"""
        def Detect_Tamper(self,frame):
            camera_blockage_counter=0
            Tamper_Detected= False
            histograms=np.zeros(shape=(256,1))
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            #Image histogram analyisis
            for i in range(gray.shape[0]):
                for j in range (gray.shape[1]):
                    binIndex=gray[i,j]
                    histograms[binIndex,0]=+1

            for k in range(histograms.shape[0]):
                if(histograms[k,0]==0):
                    camera_blockage_counter=camera_blockage_counter+1

            if(camera_blockage_counter>60):
                Tamper_Detected=True
                #print("Tamper Status",Tamper_Detected)
            return Tamper_Detected

        """This method detects face in  frame using the concepts of haarcascades
        @return bool(Tamper Detected"""
        def Detect_face(self,frame):
            Face_Detected=False
            face_count=0
            gray_image=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            faces=self.facecacade.detectMultiScale(gray_image,1.3,2)
            if (len(faces)!=0):
                Face_Detected=True
                for each_face in faces:
                    face_count=face_count+1


            return  Face_Detected

        "This function notifies the AI engine with the tuple of events detected"
        def Notify_AI_engine_KB(self,frame):
            Motion_Detected,_=self.Detect_Motion(frame)
            Face_Detected=self.Detect_face(frame)
            Tamper_Detected=self.Detect_Tamper(frame)
            notification=(Motion_Detected,Face_Detected,Tamper_Detected)
            return notification,frame



