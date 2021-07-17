import User_Control
import playsound

def main():
    print("1 -Low Sensitivity can only detect Large motion")
    print("2-Medium Sensitivity can detect significant disturbance in two frames")
    print("3- Will detect every single motion")
    print("I will recommend you to choose 2 when you are out of the house and 1 when you are in the house")
    sensitivity_level = input("\nEnter sensitivity level")
    sensitivity_level=int(sensitivity_level)
    if(sensitivity_level==1 or sensitivity_level==2 or sensitivity_level==3):
        print("\nNow I have two options for you to choose")
        print("I can run on AI_Engine using KB system to detect intruder")
        print("Also I can use the more sophisticated ML_Engine \n")
        print("Choose 1-ML_ENGINE 2-AI_ENGINE 3-Test_For _Comparison")
        print("I would recommend use the ML_ENGINE its much more optimised ")

        print("But you can also check both side side for comparison by pressing 3 ")
        ENGINE=input("Press 1 or 2 or 3")
        ENGINE=int(ENGINE)
        playsound.playsound("Resources/Starting_Simulation.mp3")
        if(ENGINE==1):
            User_Control.start_Survelleince_Agent(ML_ENGINE=True)
        elif(ENGINE==2):
            User_Control.start_Survelleince_Agent(ML_ENGINE=False)
        elif(ENGINE==3):
            User_Control.start_Survelleince_Agent(ML_ENGINE=False,test_Comparison=True)

        else:
            print("Ooopsie looks like you have selected a wrong option.Try again")
            main()

    else:
        print("Ooopsie looks like you have selected a wrong option.Try again")
        main()

def print_a_face():
    print("            \U0001f600   \U0001f600  \U0001f600       ")






if __name__=="__main__":


    print("Hey Everyone I am your Home Surveillance bot and I am here to keep your home safe from intruders")
    print("I can also tell you if your roommates steals your beer\n")
    print_a_face()
    playsound.playsound("Resources/hello.mp3")
    print("Before Beginning please set your sensitivity level")
    print("Here is the chart")
    main()

