import random

def guess_number():
    number = random.randint(0, 100)
    guessed_number = 0
    while guessed_number != number:
        guessed_number = int(input("Guess number between 0 to 100: "))
        if guessed_number == number:
            print(f"Yayee, you have guessed correctly, it is {guessed_number}")
            break
        elif guessed_number < number:
            print("Your guess is low")
        else: 
            print("Your guess is high")

if __name__ == "__main__":
    guess_number()