
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

def read_all_question():
    print("All Questions are .... ")
    for question in questions:
        print(question)

def add_new_question():
    print("Add New Question")

def access_admin_features():
    print("Press 1 for Read All Questions 2 for Add a New Question.")
    admin_option = input('Option: ')
    if admin_option == '1':
        read_all_question()
    elif admin_option == '2':
        add_new_question()
    else:
        print("Invalid Option")

def access_player_features():
    print("Press A for .... B for...")

def displaying_welcome_to_users():
    print("Welcome to Mini Quiz Game")
    print("fdafadf")
    print("fdafdafdafda")

def display_access_denied():
    print("Access Denied!")

if __name__ == "__main__":
    displaying_welcome_to_users()
    username = input('Enter Username= ')
    print(username)
    if username == 'admin':
        admin_password = input('Admin Password: ')
        if admin_password == '123':
            access_admin_features()
        else:
            display_access_denied()
    elif username == 'player':
        player_password = input('Player Password: ')
        if player_password == 'abc':
            access_player_features()
        else:
            display_access_denied()
    else:
        display_access_denied()
