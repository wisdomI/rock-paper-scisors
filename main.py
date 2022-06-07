import random

while True:
    choices = ["r", "p", "s"]
    cpu = random.choice(choices)
    player = None

    while player not in choices:
        player = input("r, p, or s?: ").lower()


    if player == cpu:
        print("cpu: ", cpu)
        print("player: ", player)    
        print("Tie")
        
    elif player == "r":
        if cpu == "p":
            print("cpu: ", cpu)
            print("player: ", player)    
            print("You Lose!")
        if cpu == "s":
            print("cpu: ", cpu)
            print("player: ", player)    
            print("You Win!")
        
    elif player == "p":
        if cpu == "r":
            print("cpu: ", cpu)
            print("player: ", player)    
            print("You Win!")
        if cpu == "s":
            print("cpu: ", cpu)
            print("player: ", player)    
            print("You Lose!")
        
    elif player == "s":
        if cpu == "p":
            print("cpu: ", cpu)
            print("player: ", player)    
            print("You Win!")
        if cpu == "r":
            print("cpu: ", cpu)
            print("player: ", player)    
            print("You Lose!")

    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        break
print("Bye")
