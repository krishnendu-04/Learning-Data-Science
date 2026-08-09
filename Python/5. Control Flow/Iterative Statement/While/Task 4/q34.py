score = 0
i = 0
while(i<5):
    choice = int(input("Which question do you want to try(1-5): "))
    if choice==1:
        ans = int(input("How many states does India have? "))
        if ans==28:
            score+=1

    elif choice==2:
        ans = int(input("How many union territories does India have? "))
        if ans==8:
            score+=1

    elif choice==3:
        ans = int(input("Kerala has how many districts? "))
        if ans==14:
            score+=1

    elif choice==4:
        ans = int(input("How many balls does an over consist of in cricket? "))
        if ans==6:
            score+=1

    elif choice==5:
        ans = int(input("How many minutes is a football game normally? "))
        if ans==90:
            score+=1

    else:
        print("Invalid Choice")

    i+=1
print("Score",score)