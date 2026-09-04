import random
def main():
    p=fun()
    if p==0:
        print("You failed Sorry")
    elif p==1:
        print("You guessed in first try")
    else:
        print(f"You guessed in {p} trys ")
def fun():
    dif=get_data()
    ans=random.randint(1,100)
    i=1
    if dif==1:
        chance=10
    elif dif==2:
        chance=5
    else:
        chance=3
    while i<=chance:
        guess=int(input(("Guess : ")))
        if guess==ans:
            break
        else:
            i+=1
            continue
    if i>chance:
        return 0
    else:
        return i


    
def get_data():
    dif=0
    while True:
        print("please choose  the difficulty  of the game")
        print("1. Easy (10 chances)")
        print("2. Medium (5 chances)")
        print("3 .Hard (3 chances)")
        dif=int(input("Enter your choice : as "))
        if dif<=0 or dif>3:
            print("Enter a valid choice (1,2,3)")
            continue
        else:
            break
    return dif
print("Welcome to our game")
print("In this game you have to try to guess the number from 1 to 100 ")
main()
