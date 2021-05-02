import User_Control

def main():
    sensitivity_level = 0
    ENGINE = 0
    ML_ENGINE=False
    Test_Comparison=False
    print("1 -Low Sesnitivity can only detect Large motion")
    print("2-Medium Sensitivity can detect significant disturbance in two frames")
    print("3- Will detect every single motion")
    print("I will recommend you to choose 2 when you are out of the house and 1 when you are in the house")
    sensitivity_level = input("\nEnter sensitivity level")
    sensitivity_level=int(sensitivity_level)
    if(sensitivity_level==1 or sensitivity_level==2 or sensitivity_level==3):
        print("\nNow I have two options for you")
        print("I can run on AI_Engine using KB system to detect intruder")
        print("Also I can use the more sophisticated ML_Engine \n")
        print("Choose 1-ML_ENGINE 2-AI_ENGINE 3-Test_For _Comparison")
        print("I would recommend use the ML_ENGINE its much more optimised ")

        print("But you can also check both side side for comparsion by pressing 3 ")
        ENGINE=input("Press 1 or 2 or 3")
        ENGINE=int(ENGINE)
        if(ENGINE==1):
            ML_ENGINE=True
            User_Control.start_Survelleince_Agent(sensitivity_level,ML_ENGINE)
        elif(ENGINE==2):
            User_Control.start_Survelleince_Agent(sensitivity_level,ML_ENGINE)
        elif(ENGINE==3):
            User_Control.start_Survelleince_Agent(sensitivity_level,ML_ENGINE,test_Comparison=True)

        else:
            print("Ooopsie looks like you have selected a wrong option.Try again")
            main()

    else:
        print("Ooopsie looks like you have selected a wrong option.Try again")
        main()




if __name__=="__main__":

    print("Hey Everyone I am your Home Surveillance bot and I am here to keep your home safe from intruders")
    print("I can also tell you if your roommates steals your beer\n")
    print("Before Beginning please set your sensitivity level")
    print("Here is the chart")
    main()

