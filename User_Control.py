from Survellance_Engines.ML_Engine import ML_Engine
from Survellance_Engines.AI_Engine import AI_Engine
import cv2
import numpy as np
import playsound
import threading
import time


def start_Survelleince_Agent(sensitivity_level,ML_ENGINE=True,test_Comparison=False):
    if(test_Comparison):
        ML_ENGINE=False
    ML=ML_Engine()
    AI=AI_Engine()
    thread=None
    print("Make sure you are running this on a local machine and your camera is functional")
    cap=cv2.VideoCapture(0)

    if(ML_ENGINE):
        while(True):
            ret,frame=cap.read()
            frame=cv2.resize(frame,(720,540))
            frame_copy=np.copy(frame)
            #Here you can adjust the sensitivity of the system and pass it as a parameter
            ML.classify_with_decison_trees(frame_copy,2)
            cv2.imshow("frame",frame_copy)
            if(ML.TAMPER):
                thread=threading.Thread(target=play_Sound)
                thread.start()

            if cv2.waitKey(1) & 0xFF == ord('q'):
                del ML
                del AI
                exit("ExitLog:Simulation Ended by User")

    elif(test_Comparison):
        while(True):
            ret,frame=cap.read()
            frame=cv2.resize(frame,(640,480))
            frame_copy=np.copy(frame)
            frame_second_copy=np.copy(frame)
            #Here you can adjust the sensitivity of the system and pass it as a parameter
            ML.classify_with_decison_trees(frame_copy,2)
            AI.knowledge_base(frame_second_copy)
            cv2.imshow("ML_ENGINE",frame_copy)
            cv2.imshow("AI_ENGINE",frame_second_copy)
            if(ML.TAMPER or AI.Tamper):
                thread=threading.Thread(target=play_Sound)
                thread.start()


            if cv2.waitKey(1) & 0xFF == ord('q'):
                del ML
                del AI
                exit("ExitLog:Simulation Ended by User")

    else:
        while(True):
            ret,frame=cap.read()
            frame_copy = np.copy(frame)

            frame_AI=AI.knowledge_base(frame_copy)
            cv2.imshow("frame", frame_AI)
            if (AI.Tamper):
                thread = threading.Thread(target=play_Sound)
                thread.start()

            if cv2.waitKey(1) & 0xFF == ord('q'):
                del AI
                del ML
                exit("ExitLog:Simulation Ended by User")






def play_Sound():
    playsound.playsound("Resources/alert.mp3")

