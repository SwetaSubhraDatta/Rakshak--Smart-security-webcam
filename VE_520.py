"""Created by Sweta Subhra Datta
April 24th,2021
"""
import cv2
import numpy as np



class Vision_Engine():
        backsub = cv2.createBackgroundSubtractorMOG2(history=50, varThreshold=30, detectShadows=False)#These hyperparameters are tuned to give the best results
        facecacade=cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")

        """This method detects motion in a frame by using the concept of background subtraction and checking contourArea
         on a subtracted frame 
         @return:: bool (Motion_Detected)"""

        def Detect_Motion(self,frame):
            Motion_Detected = False
            frame_copy=np.copy(frame)
            background=self.backsub.apply(frame_copy)
            median_blur=cv2.medianBlur(background,7)
            contours,hierarchy=cv2.findContours(median_blur,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            for cnts in contours:
                if(cv2.contourArea(cnts)>50):
                    Motion_Detected=True
                 #   print("Motion Status",Motion_Detected)
                    break

            # cv2.imshow("frame",median_blur)
            # if cv2.waitKey(1) & 0xFF == ord('q'):
            #     exit("KeyboardInterrupt")
            return Motion_Detected


        """This method detects camera covering or camera obstruction in every frame
        
        @return bool(Tamper Detected"""
        def Detect_Tamper(self,frame):
            camera_blockage_counter=0
            Tamper_Detected= False
            histograms=np.zeros(shape=(256,1))
            frame_copy = np.copy(frame)
            gray=cv2.cvtColor(frame_copy,cv2.COLOR_BGR2GRAY)

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



        def Detect_face(self,frame):
            Face_Detected=False
            face_count=0
            frame_copy = np.copy(frame)
            gray_image=cv2.cvtColor(frame_copy,cv2.COLOR_BGR2GRAY)
            faces=self.facecacade.detectMultiScale(gray_image,1.3,5)
            if (len(faces)!=0):
                Face_Detected=True
                for each_face in faces:
                    face_count=face_count+1

            return  Face_Detected


        def Notify_AI_engine_KB(self,frame):
            Motion_Detected=self.Detect_Motion(frame)
            Face_Detected=self.Detect_face(frame)
            Tamper_Detected=self.Detect_Tamper(frame)
            notification=(Motion_Detected,Face_Detected,Tamper_Detected)
            return notification,frame


def capture_Video():
    VE=Vision_Engine()
    print("Make sure you are running this on a local machine and your camera is functional")
    cap=cv2.VideoCapture(0)
    while(True):
        ret,frame=cap.read()
        ######@PRAGNA AND @BHAVYA###
        #####Notification for the AI engine can be get from here
        ##You need to
        ## Step 1:Make a class of AI_engine
        ##Step 2: Make methods that takes notifcations as paramter
        ##Step 3: make Decsions

        notifcation,frame=VE.Notify_AI_engine_KB(frame)
        print(notifcation)
        cv2.imshow("Frame",frame)
        cv2.waitKey(1)


if __name__=="__main__":
    capture_Video()
