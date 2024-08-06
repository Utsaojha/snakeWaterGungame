import random
# snake water gun game or scissor paper rock game
def gamewin(comp,you):
    if comp == you:
        return None
    elif comp == "s":
        if you =="w":
            return False
        elif you == "g":
            return True
    elif comp == "w":
        if you =="g":
            return False
        elif you == "s":
            return True
    elif comp == "g":
        if you =="s":
            return False
        elif you == "w":
            return True

print("Comp  turn: Snake(s) Water(w) or Gun(g)?")
randNo= random.randint (1,3)
if randNo==1:
    comp="s"
elif randNo==2:
    comp="w"
elif randNo==3:
    comp="g"

you=input("Your turn: Snake(s) Water(w) or Gun(g)?\n")


print(f"Computer choose {comp}")
print(f"You choose {you}")

a= gamewin(comp,you)
if a == None:
    print("The game is a tie")
elif a:
    print("You win!")
else:
    print("You lose!")