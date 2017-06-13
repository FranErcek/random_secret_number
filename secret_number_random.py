import random

def main():
    secret_number = random.randint(1, 36)

    while True:
        guess = int(raw_input("Guess the secret number between 1 and 36: "))

        if guess == secret_number:
            print ("YOU WIN, it's number: %s ") %secret_number
        elif guess < secret_number:
            print "Try again! Your guess is to low "
        elif guess > secret_number:
            print "Try again! Your guess is to high"

if __name__ == "__main__":
    main()