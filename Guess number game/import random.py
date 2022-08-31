import random
num=random.randint(0,100)
attempts=0
while True:
    attempts+=1
    guessNum=int(input("Guess The Number: \n"))
    if guessNum<num:
        print("Your guess was too less")
    elif guessNum>num:
        print("Your guess was too high")
    else:
        print(f"You guessed the right number in {attempts} attempts")
        break
    
print("Thank you for playing")