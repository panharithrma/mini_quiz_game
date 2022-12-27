print('Welcome to Mini Game')
a = input('Enter Username= ')
if a == "admin":
    ls = [
        'Question1: ',
        'Question2: ',
        'Question3: ',
    ]
    for question in ls:
        print(question)
else:
    p = input('Enter Password= ')
    if p == "123":
        print('Question1: 1+1 = (2 or 1) ')
        x = input('Your choice is : ')
        if x == "2":
            print("Your answer is True")
        else:
            print("Your answer is False")