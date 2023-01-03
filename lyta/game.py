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
    },
    {
          'title': 'Where is Angkor Wat ?',
          'answers': ['BTB', 'SR', 'TK', 'PP'],
          'correct': 'SR'
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
    print("answer: ",  list)
    b = input("correct: ")

    add_new = {'title' : a,
               'answer' : list,
                'correct' : b
    }
    questions.append(add_new)
    print("New question has been added")
    print("Press 1 for Continue to Add , 2 for Exit ")
    y = input("Option: ")
    if y == "1":
        add_new_question()
    elif y == "2":
        pass
    else:
        print("Invalided Input!")

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
    correct_answer = 0
    for q in questions:
        print(q['title'])
        print(q["answers"])
        answer = input("Your Answer is: ")
        if q["correct"] == answer:
            print("Your Answer is correct.")
            correct_answer += 1
        else:
            print("Your Answer is False")
        if q['correct'] == 'answer':
            correct_answer += 1
    print("Your total scores is:", correct_answer)

def access1_player_features():
    print("Press A for play B for Exit Game!")
    player_option = input('Option: ')
    if player_option  == 'A':
        play_game1()
    elif player_option  == 'B':
        pass
    else:
        print("Invalid Option")
def displaying_welcome_to_users():
    print("Welcome to Mini Quiz Game")
    print("Are you admin or player?")
def display_access_denied():
    print("Access Denied!")

if __name__ == "__main__":
    while 1:
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