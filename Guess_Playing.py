import random

number1 = random.randint(1,100)
chance = 5
counter = 0

while chance>0:
    chance -= 1
    counter += 1
    guess = int(input("guess :"))
    
    if number1 == guess:
        print(f"You guessed on the {counter}.try.")
        print(f"Your total point is : {100-(20)*(counter-1)}")
        break
    elif number1 > guess:
        print("up")
    else:
        print("down")
    
    if chance == 0:
        print(f"your chance is done. Number was : {number1}")



 # number2 = random.uniform(0,10)
 # print(number2)

 # number3 = random.randrange(0,10,2)
 # print(number3)
 
 
 
 