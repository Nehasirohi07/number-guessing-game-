# generate random number 
# between 1 to 100
# user input guess number 
# if the ai number is higher then user guess print higher and if not print lower
# the user will only have 7 lives 
# loose one live in ever wrong guess 
# if the users input is correct then print YAY You Win

import random
def game():
    random_no = random.randint(1, 100)
    guess = int(input("ENTER A NUMBER: ")) 
    lives = 7
    gameover= False

    while lives > 0 and gameover != True:

        if guess > random_no:
            print("Lower")
        elif guess < random_no:
            print("Higher")
        elif guess == random_no:
            print("YAY You Win Bitch")
            break
        lives -=1
        print("remaining lives : ", lives)
        guess = int(input("ENTER A NUMBER: "))
    
    if lives == 0:
        print("game over")
        
    
      


game()
       




