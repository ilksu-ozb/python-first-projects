import secrets
import string
import sys

def user_choices():
    while True:
        try:
            length = int(input("Password length: "))
            if length < 8 or length > 64:
                print("Choose a number between 8 and 64")
                continue
            else:
                while True:
                    special = input("Do you want special characters? (y/n)").lower()
                    if special == "y" or special == "yes":
                        special = True
                    elif special == "n" or special == "no":
                        special = False
                    else:
                        print("Invalid input. Please answer with 'yes' or 'no'.")
                        continue
                    while True:
                        numbers = input("Do you want numbers? (y/n)").lower()
                        if numbers == "y" or numbers == "yes":
                            numbers = True
                        elif numbers == "n" or numbers == "no":
                            numbers = False
                        else:
                            print("Invalid input. Please answer with 'yes' or 'no'.")
                            continue
                        
                        return length, special, numbers
            
        except KeyboardInterrupt:
            sys.exit(f"\nProgram terminated by user.")
        
        except ValueError: 
            print("Invalid input. Please check your anwser.")


def set_rules(special, numbers):
    character_pool = string.ascii_lowercase + string.ascii_uppercase
    if special:
        character_pool += string.punctuation
    
    if numbers:
        character_pool += string.digits

    return character_pool

def main():
    length, special, numbers = user_choices()
    pool = set_rules(special, numbers)

    while True:
        try:
            password = ""
            for _ in range(length):
                character = secrets.choice(pool)
                password += character

            if special and not any(char in string.punctuation for char in password):
                continue  

            if numbers and not any(char in string.digits for char in password):
                continue
            
            print(f"{password}")
            break
            


        except KeyboardInterrupt:
            sys.exit("Program terminated by user.")








if __name__ == "__main__":
    main()
