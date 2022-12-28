

def add_new_question():
    print("Processing Add New Question!")

def view_all_questions():
    print("Processing View All Questions!")

def access_admin_features():
    print("Press 1 for .... 2 for...")

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
