import random

random_number = random.randint(1, 50)
tries = 5

# create a loop for to support the amount of tries
for attempt in range(tries):
    # prompt user to guess a number 
    guess = int(input("Guess the number between 1 and 50: "))
    
    # if the guess equals the random number 
    if guess == random_number:
        print(f"yeah, {random_number} is the number")
        break # we break the loop here
    # if the guess is lower than the random number
    elif guess < random_number:
        print (f"number is too low, you have {tries -attempt -1} attempt(s) left")
    # if the guess is higher than the random number
    else:
        print (f"number is too high, you have {tries -attempt -1} attempt(s) left")  
# when you're out of tries
else:
    print("Out of tries, the number was",random_number)


