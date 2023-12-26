def game ():
    step1 = input("left or right?\n").lower()

    if step1 == 'right' :
        print("game over ........ \n try again \n")
        game()

    step2 = input("swim or wait ?\n").lower()
    if step2 == "swim" :
        print("game over ........ \n try again \n")
        game()

    step3 = input("which door ? red / blue / yellow? \n").lower()
    if step3 == "yellow" :
        print("you won")
        exit()
    else :
        print("game over ........ \n try again \n")
        game()

game()