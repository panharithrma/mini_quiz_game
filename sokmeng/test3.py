def loing():
    print("Hello welcome to mini game...")
    print("who are you?")

def first_any_question():
    first_question = {
        "title1" : "im a admin or im a user"
    }
    print(first_question.get("title1").lower())
def dont_have_option():
    print("dont have option!!")
def plz_check_password():
    print("plz check your password!!!")
def admin():
    enter_password_admin_and_user()
    password_admin = int(input("....."))
    if password_admin == 123:
        choose_option_admin()
        optipon_admin = input("    ---").lower()
        if optipon_admin == 'a':
            print("while onec user u are you add?")
        elif optipon_admin == 'e':
            print("edit")
        elif optipon_admin == 'c':
            print("choose product u wanna check")
        else:
            dont_have_option()
    else:
        plz_check_password()
def user():
    enter_password_admin_and_user()
    password_user = int(input("...."))
    if password_user == 456:
        choose_option_user()
        user_option = int(input("   ---"))
        if user_option == 1:
            print('game is starting...')
        elif user_option == 2:
            print("choose hero u wanna buys.")
        elif user_option == 3:
            print("added.")
        else:
            dont_have_option()
    else:
        plz_check_password()

def enter_password_admin_and_user():
    print("plz enter your password...")
def choose_option_admin():
    print("choose options:\n"
          "A-->add user\n"
          "E-->Edit\n"
          "C-->check product")

def choose_option_user():
    print("choose options:\n"
          "1-->start game now\n"
          "2-->buy hero\n"
          "3-->invite friends")
                                        #main
if __name__ == "__main__":
    loing()
    first_any_question()
    answer = input(">>>")
    if answer.lower() == "admin":
        admin()
    elif answer.lower() == "user":
        user()

