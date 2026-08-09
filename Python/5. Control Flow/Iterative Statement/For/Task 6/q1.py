for i in range(1,26):
    uniform = input("Is the student wearing proper uniform? (y/n)")
    if uniform=='n':
        print(i)
    elif uniform=='y':
        pass
    else:
        print("Invalid answer")