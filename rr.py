from random import choice
print ("1 stands for paper, 2 stands for rock, 3 stand for scissors")
# Using a tuple here is actually faster than using a list
signs = 1, 2, 3
def game():
    i = int(input("pick a sign, use the numbers shown above "))
    cc = choice(signs)
    if i - cc == 0:
        print ("it's a draw")
    elif i - cc == 1:
        print("you lose")
    elif  i - cc == 2:
        print("you win")
    elif i - cc == -1:
        print("you win")
    elif i - cc == -2:
        print("you lose")
    return int(input("if you want to play again, press 1"))

while game() == 1:
    pass