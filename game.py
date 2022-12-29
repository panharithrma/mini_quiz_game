
questions = [
    {
        'title': 'What is minimum age to vote in Cambodia ?',
        'answers': ['15', '18', '21', '35'],
        'correct': '18'
    },
    {
        'title': 'How many provinces and Cities in Cambodia ?',
        'answers': ['15', '24', '25', '35'],
        'correct': '25'
    }
]
question1_player = [
    {
        'title': 'What is minimum age to vote in Cambodia ?',
        'answers': ['15', '18', '21', '35'],
    }
]
question2_player = [
    {
        'title': 'How many provinces and Cities in Cambodia ?',
        'answers': ['15', '24', '25', '35'],
    }
]
question3_player= [
        {
            'title': 'Where is Angkor Wat ?',
            'answers': ['BTB', 'SR', 'TK', 'PP'],
        }
    ]

def read_all_question():
    print("All Questions are .... ")
    for question in questions:
        print(question)

def add_new_question():
    a = input("title: ")
    n=4
    list=[]
    for i in range (n):
        element = input("Enter answer to choose= ")
        list.append(element)
    print("answer: ", list)
    b = input("correct: ")

def access_admin_features():
    print("Press 1 for Read All Questions 2 for Add a New Question.")
    admin_option = input('Option: ')
    if admin_option == '1':
        read_all_question()
    elif admin_option == '2':
        add_new_question()

    else:
        print("Invalid Option")

def play_game1():
    print("Question is:  ")
    for question in question1_player:
        print(question)
    answer = input("Your Answer is: ")
    if answer == "18":
        print("Your Answer is correct.")
    else:
        print("Your Answer is False")
    access2_player_features()

def play_game2():
    print("Question is:  ")
    for question in question2_player:
        print(question)
    answer = input("Your Answer is: ")
    if answer == "25":
        print("Your Answer is correct.")
    else:
        print("Your Answer is False")
    access3_player_features()

def play_game3():
    print("Question is:  ")
    for question in question3_player:
        print(question)
    answer = input("Your Answer is: ")
    if answer == "SR":
        print("Your Answer is correct.")
    else:
        print("Your Answer is False")

def access1_player_features():
    print("Press A for play B for Exit Game!")
    player_option = input('Option: ')
    if player_option  == 'A':
        play_game1()
    elif player_option  == 'B':
        pass
    else:
        print("Invalid Option")

def access2_player_features():
    print("Press C for continue B for Exit Game!")
    player_option = input('Option: ')
    if player_option  == 'C':
        play_game2()
    elif player_option  == 'B':
        pass
    else:
        print("Invalid Option")

def access3_player_features():
    print("Press C for continue B for Exit Game!")
    player_option = input('Option: ')
    if player_option == 'C':
        play_game3()
    elif player_option == 'B':
        pass
    else:
        print("Invalid Option")

def displaying_welcome_to_users():
    print("Welcome to Mini Quiz Game")
    print("Are you admin or player?")

def display_access_denied():
    print("Access Denied!")




if __name__ == "__main__":
    displaying_welcome_to_users()
    username = input('Enter Username= ')
    if username == 'admin':
        admin_password = input('Admin Password= ')
        if admin_password == '123':
            access_admin_features()
        else:
            display_access_denied()
    elif username == 'player':
        player_password = input('Player Password: ')
        if player_password == 'abc':
            access1_player_features()
        else:
            display_access_denied()

    else:
        display_access_denied()