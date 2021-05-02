import cv2
from Survellance_Engines.Vision_engine import Vision_Engine
import playsound



class ML_Engine():

    def __init__(self):
        self.VI=Vision_Engine()
        self.IG=0
        self.impurity=1
        self.MOTION=False
        self.contours_present=False
        self.Face=False
        self.TAMPER=False
        self.Raise_Alarm=False
        self.motion_probabilty=0
        self.sensitivity_level=0
        self.thread=object

    def First_Depth_Are_There_Contours(self,frame):
        cnt_area=None
        Countours_Present=False
        Motion_detected,contours=self.VI.Detect_Motion(frame)
        if(len(contours)==0):
            self.IG = 1
            self.impurity = 0
            self.contours_present=False
            Countours_Present=self.contours_present
            return Countours_Present,None

        else:
            self.IG=self.IG+0.15
            self.impurity=self.impurity-0.15
            self.contours_present=True
            Countours_Present=self.contours_present
            for cnt in contours:
                cnt_area=cv2.contourArea(cnt)
            return Countours_Present,cnt_area

    def Second_Depth_Is_there_Motion(self,frame,cnt_area):
        if(cnt_area>=50):
            self.MOTION=True
            self.IG=self.IG+0.15
            self.impurity=self.impurity-0.15
        elif(20<=cnt_area<50):
                self.IG=self.IG+0.05
                self.impurity=self.impurity-0.05
                self.motion_probabilty=0.5
                if(self.sensitivity_level>1):
                    self.MOTION=True
                else:
                    self.MOTION=False
        else:
            self.IG=self.IG+0.02
            self.impurity=self.impurity-0.02
            self.motion_probabilty=0.2
            if(self.sensitivity_level>2):
                self.MOTION=True
            else:
                self.MOTION=False

    def Third_Depth_Is_There_a_Tamper(self,frame):

        Tamper_Detected=self.VI.Detect_Tamper(frame)
        if(Tamper_Detected):
            self.TAMPER=True
            self.Raise_Alarm=True
            self.IG=1
            self.impurity=0
        else:
            self.TAMPER=False
            self.Raise_Alarm=False

    def Fourth_Depth_is_There_a_Face(self,frame):
            Face_Detected=self.VI.Detect_face(frame)
            if(Face_Detected):
                self.Face=True
                self.Raise_Alarm=True
                self.IG=1
                self.impurity=0
            else:
                self.Face=False
                self.Raise_Alarm=False

    def classify_with_decison_trees(self,frame,Sensitvity_level):
        self.sensitivity_level=Sensitvity_level
        self.Third_Depth_Is_There_a_Tamper(frame)
        Contours_present,area=self.First_Depth_Are_There_Contours(frame)
        if(self.contours_present):
            self.Second_Depth_Is_there_Motion(frame,cnt_area=area)


            if(self.MOTION and not self.TAMPER):
                    self.Fourth_Depth_is_There_a_Face(frame)
            # elif(self.TAMPER):
            #         self.thread=threading.Thread(target=self.play_Sound,daemon=True)
            #         self.thread.start()



        self.writeon_frame(frame)
        # if(self.TAMPER):
        #     self.thread.join()
        return frame
    def writeon_frame(self,frame):
        Notification="Safe"
        cv2.putText(frame,"IG ="+str(self.IG),(20,frame.shape[0]-30),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255, 255, 255), 2)
        cv2.putText(frame,"impurity="+str(self.impurity),(20,frame.shape[0]-60),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,255,255),2)
        cv2.putText(frame,"DECISON_TREE_SIMULATOR",(frame.shape[0]-290,20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,220,255),2)
        if(self.MOTION):
            Notification="MOTION_DETECTED"
            cv2.putText(frame, Notification, (20, 65), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            if (self.Face and not self.TAMPER):
                Notification = "FACE_DETECTED! INTRUDER ALERT"
                cv2.putText(frame, Notification, (200, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        elif(self.TAMPER):
                Notification="CAMERA_TAMPERED "
                cv2.putText(frame, Notification, (70,65 ), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

        else:
            cv2.putText(frame, Notification, (1, 65), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)


        self.IG=0
        self.impurity=1



    def play_Sound(self):
        return playsound.playsound("Resources/alert.mp3")

    def __del__(self):
        del(self.VI)