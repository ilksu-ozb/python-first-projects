import random
import sys

def control_and_choose():
    while True:
        try:
            range_start = int(input("Start of the range: "))
            range_end = int(input("End of the range: ")) 
            
            if range_start >= range_end:
                print("Invalid range. Start of the range must be less than end of the range.")
                continue
            else:
                trial = int(input("How many trials do you want to have? "))
                numbers = list(range(range_start, range_end + 1))
                number = random.choice(numbers)

            if trial <= 0:
                print("Invalid number of trials. Please enter a positive integer.")
                continue
            return number, trial
            
        except KeyboardInterrupt:
            sys.exit("Keyboard interrupt.")
        except ValueError:
            print("Invalid input. Please enter integers only.")


def main():
    number, trial = control_and_choose()
    try:
        for _ in range(trial):
            guess = int(input("Your guess: "))
            if guess == number:
                print(f"Correct! The number was {number}.")
                return
            elif guess < number:
                print("Too Low!")
            else:
                print("Too High!")

    except ValueError:
        sys.exit("Invalid input. Please enter integers only.")
    except KeyboardInterrupt:
        sys.exit("Keyboard interrupt.")


if __name__ == "__main__":
    main()

