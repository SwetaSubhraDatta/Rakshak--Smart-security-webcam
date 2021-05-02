from Survellance_Engines.ML_Engine import ML_Engine
from Survellance_Engines.AI_Engine import AI_Engine
import cv2
import numpy as np
import playsound
import threading



def start_Survelleince_Agent(ML_ENGINE=True,test_Comparison=False):
    if(test_Comparison):
        ML_ENGINE=False
    print("Make sure you are running this on a local machine and your camera is functional")
    cap=cv2.VideoCapture(0)
    skip_first_frames=0

    if(ML_ENGINE):
        ML = ML_Engine()
        """When we open the aperture of a camera there is huge amount of light that hits the sensors
        Which will trigger huge difference in first set of frames and will trigger false Motion and even false 
        Camera tampering so we skip the first 4 sets of frames """
        while(True):
            skip_first_frames = skip_first_frames + 1
            ret,frame=cap.read()

            if(skip_first_frames>4):
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
                            exit("ExitLog:Simulation Ended by User")
            else:
                pass

    elif(test_Comparison):
        AI = AI_Engine()
        ML = ML_Engine()
        while(True):
            skip_first_frames = skip_first_frames + 1
            ret, frame = cap.read()
            if(skip_first_frames>4):
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
                pass

    else:
        AI = AI_Engine()
        while(True):
            skip_first_frames = skip_first_frames + 1
            ret,frame=cap.read()
            if(skip_first_frames>4):
                frame_copy = np.copy(frame)

                frame_AI=AI.knowledge_base(frame_copy)
                cv2.imshow("frame", frame_AI)
                if (AI.Tamper):
                    thread = threading.Thread(target=play_Sound)
                    thread.start()

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    del AI
                    exit("ExitLog:Simulation Ended by User")






def play_Sound():
    playsound.playsound("Resources/alert.mp3")

