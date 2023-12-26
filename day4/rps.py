import random 
user_select = input("Rock / Paper / scissor\n").lower()
computer_select = random.randint(0,2)
if user_select == "rock" :
    if  computer_select == 0 :
        print("computer chose Rock so it's draw" )
    elif  computer_select == 1 :
        print("computer chose paper so computer win" )
    elif  computer_select == 2 :
        print("computer chose scissor so you win" )
elif user_select == "paper" :
    if  computer_select == 0 :
        print("computer chose Rock so you win" )
    elif  computer_select == 1 :
        print("computer chose paper so it's draw" )
    elif  computer_select == 2 :
        print("computer chose scissor so computer win" )
elif user_select == "scissor" :
    if  computer_select == 0 :
        print("computer chose Rock so computer win" )
    elif  computer_select == 1 :
        print("computer chose paper so you win " )
    elif  computer_select == 2 :
        print("computer chose scissor so it's draw" )