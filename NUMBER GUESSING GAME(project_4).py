import random
print("***********WELCOME TO A RANDOM NUMBER SELECTING GAME**************")
def Guess_number_game():
    print("1. PLAY GAME")
    print("2. EXIT")
while True:
    Guess_number_game()
    choice=int(input("Enter your choice:"))
    if choice==1:
        Number=random.randint(1,100)
        print("_______________WELCOME________________")
        total_attempts=int(input("Enter how many attempts do you take to guess a number:"))
        if total_attempts<=7 and total_attempts>0:
            guess_number=int(input("Enter the number you have guessed="))
            for i in range(1,total_attempts+1):
                if guess_number==Number:
                    print("Congratulations! you Guessed!")
                    count=i
                    print("total_attempts_took_to_guess:",count)
                    break

                elif guess_number>Number:
                    print("TOO high! try again")
                else:
                    print("Too low! try again")
                if i<total_attempts:
                    guess_number=int(input("Enter the number you have guessed="))
            else:
                print(" SORRY! YOU LOST THE GAME AND The number is:",Number)  
           
        else:
            print("YOU HAVE ONLY A 7 MAXIMUM ATTEMPTS")
    else:
        break





        