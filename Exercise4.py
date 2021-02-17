import random

def main():
    prob = 0.80
    if random.random() < prob:
        favourite = "dogs"  # change this
    elif random.random() < 0.5:
        favourite = "cats"
    else:
        favourite = "bats"
    print("I love " + favourite) 


main()
