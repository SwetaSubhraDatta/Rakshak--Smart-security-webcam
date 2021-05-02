import cv2
from Survellance_Engines.Vision_engine import Vision_Engine


class AI_Engine():

  def __init__(self):
    self.VI=Vision_Engine()
    self.Tamper=False

  def knowledge_base(self,frame):
    self.Tamper=False
    LOGGING=False #Change this if you need logs
    notification, frame = self.VI.Notify_AI_engine_KB(frame)

    """Change this if you need LOGS for KB"""
    if(LOGGING):
      print(notification)


    if(notification[2]==True):
      self.Tamper=True
    #print(notification)
    Decision = "Do Nothing"
    if notification == (True,True,True): #This doesnt happen always
      Decision="High-level Breach, Raise Alarm"
    elif notification == (True,True,False):
      Decision="Intruder Detected, Raise Alarm"
    elif notification == (True,False,False):
      Decision="Motion Detected, Not Threat"
    elif notification == (False,True,False):
      Decision="Face Detected, But No Motion,Intruder has stopped moving"
    elif notification == (False,False,True):
      Decision="Tamper Detected, Raise Alarm"
    elif notification == (True,False,True):
      Decision="Motion and Tamper Detected, Raise Alarm"
    elif notification == (False,True,True):
      Decision="System Failure"
    elif notification == (False,False,False):
      Decision="Do Nothing"
    cv2.putText(frame, Decision, (2, 65), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.putText(frame, "AI_KB_SIMULATOR", (frame.shape[0] - 250, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                (0, 220, 255), 2)
    return frame

  def __del__(self):
    del(self.VI)



