import random
import sys

choices = ["Rock", "Paper", "Scissors"]

def main(): 
    name = input("What is your name? ").capitalize()
    rounds = int(input ("How many rounds should the game be? "))

    user_scor = 0
    comp_scor = 0

    for i in range (rounds):
        print (f"ROUND: ", i+1)

        c = computers_choice()
        u = users_choice()

        print (f"Computer: {c}")

        result = winner_is(u, c, name)
        
        if result == "user":
            user_scor += 1
        elif result == "computer":
            comp_scor += 1
        else:
            continue
    
    if user_scor > comp_scor:
        print (f"{name} WINS!")
    elif comp_scor > user_scor:
        print ("Computer WINS!")
    else:
        print("TIE!")


def users_choice():
    try:
        while True:
            u = input("3,2,1..GO: ").capitalize()
            if u in choices:
                break
        return u
                 
    except KeyboardInterrupt:
        sys.exit("Game has ended")

def computers_choice():
    c = random.choice(choices)
    return c


def winner_is(users_choice, computers_choice, name):
    if computers_choice == users_choice:
        print ("Tie!")
    elif (users_choice ==  "Rock" and computers_choice == "Scissors") or \
        (users_choice ==  "Paper" and computers_choice == "Rock") or \
        (users_choice ==  "Scissors" and computers_choice == "Paper"):
        print (f"1 point to {name}!")
        return "user"
    else:
        print ("1 point to Computer!")
        return "computer"

if __name__ == "__main__":
    main()


    
    