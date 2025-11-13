print("Welcome to Rock-Paper-Scissors!")
choice = ["rock", "paper", "scissors"]
index = ord(str(id(choice))[-1]) % len(choice)
print(choice[index])