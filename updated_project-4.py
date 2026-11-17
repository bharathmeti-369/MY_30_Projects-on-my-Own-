import random
def Play_game():
    number=random.randint(1,100)
    attempts=int(input("Enter attempts(1-7):"))
    if not 1<=attempts<=7:
        print("invalid attempts")
        return
    for i in range(1,attempts+1):
        guess=int(input("Guess:"))
        if guess==number:
            print("Congratulations")
            print("Attempts used:",i)
            break
        elif guess>number:
            print("too high")
        else:
            print("too low")
    else:
        print("sorry! you lost")
        print("Correct Number:",number)
while True:
    print("1. PLAY GAME")
    print("2. EXIT")
    choice=int(input("Enter choice:"))
    if choice==1:
        Play_game()
    elif choice==2:
        print("Thank you for playing")
        break
    else:
        print("Invalid choice")
