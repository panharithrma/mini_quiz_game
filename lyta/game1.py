print('Welcome to Mini Game')
a = input('Enter Username= ')
ls = [
        {'question1': 'Where is the capital of Cambodia?'},
        {'answers': ('Battambang', 'Poipet', 'Siem Reap', 'Phnom Penh')},
        {'correct': 'Phnom Penh'}
    ]
if a == "admin":
    y = input("Do you want to view or add question = ")
    if y == "view":
        for question in ls:
            print(question)
    else:
        ls.append(ls)

else:
    print('1, Where is the capital of Cambodia?')
    print('Answers : Battambang, Poipet, Siem Reap or Phnom Penh')
    x = input('Your choice is : ')
    if x == "Phnom Penh":
        print("Your answer is True")
    else:
        print("Your answer is False")