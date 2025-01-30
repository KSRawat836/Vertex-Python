import random
print("Tossing the coin")
a = random.randint(0,1)
b = (input("Enter heads or tails:"))
while True:
    if b == "heads" and a == 1:
        print("You win")
        break
    elif b == "tails" and a == 0:
        print("You win")
        break
    elif b!= "heads" and b!="tails":
        print("Invalid option")
        break
    else:
        print("You lose")
        break
