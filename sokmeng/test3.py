# password admin ==123
# password user ==456
def loing():
    print("Hello welcome to mini game...")
    print("who are you?")
def first_any_question():
    first_question = {
        "title1" : "im a admin or im a user"
    }
    print(first_question.get("title1").lower())
def enter_password_admin_and_user():
    print("plz enter your password...")
def admin():
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
    password_user = int(input("...."))
    if password_user == 456:
        choose_option_user()
        user_option = int(input("   ---"))
        if user_option == 1:
            print('game is starting...')
            read_all_question()
        elif user_option == 2:
            print("choose hero u wanna buys.")
        elif user_option == 3:
            print("added.")
        elif user_option ==4:
                user_ask()
        else:
            dont_have_option()
    else:
        plz_check_password()
def plz_check_password():
    print("plz check your password!!!")
def dont_have_option():
    print("dont have option!!")

def read_all_question():
    print("All Questions are .... ")
    question = len(questions)
    i = 0
    while i<question:
        print(questions[i])
        answer1 = int(input("........"))
        if answer1 == 18:
            got_score()
        else:
            lose_game()
        print(questions[i+1])
        answer2 = int(input("........"))
        if answer2==16:
            got_score()
        else:
            lose_game()
        if answer1 == 18 and answer2 == 16:
            print("total=40")
            break
        elif answer1!=18 and answer2==16:
            print("total=20")
            break
        elif answer1==18 and answer2!=16:
            print("total =20")
            break
        else:
            print("=0")
            print("plz play again you can do it(y/n) yes or no!!!!")
            user_answer = input(">>>>")
            if user_answer =="y":
                print("game is starting...")
                read_all_question()
                break
            else:
                pass
        i+=1

questions = [
    {
        'title': 'What is minimum age to vote in Cambodia ?',
        'answers': ['15', '18', '21', '16'],
    }
]
questions.append("Question: how many people in  cambodia?\n"
                 "10million\n"
                 "16million")
ask_from_use =[""]
def user_ask():

    n= 1
    while n<n+1:
        user_questions=input("enter your question++++>>>>>>")
        ask_from_use.append(user_questions)
        user_answer = input("input your answer 4 answer:...")
        user_choise = input("choose one correct answer:....")
        if user_choise == user_answer:
            got_score()
            sum = n*20
            print(sum)
        else:
            lose_game()
        ask_from_use.append(user_answer)
        print(ask_from_use)
        n+=1
    user_answer = input("you want add more question (y/n----->")
    if user_answer.lower() == "y":
        user_ask()
    elif user_answer.lower()=="n":
        choose_option_user()
    else:
        pass

def got_score():
    score = 20
    print("you got score :" + str(score))
def lose_game():
    print("your game is losed")
def choose_option_admin():
    print("choose options:\n"
          "A-->add user\n"
          "E-->Edit\n"
          "C-->check product")
def choose_option_user():
    print("choose options:\n"
          "1-->start game now\n"
          "2-->buy hero\n"
          "3-->invite friends\n"
          "4--> ask your question by your self")

#main
if __name__ == "__main__":
    loing()
    first_any_question()
    answer = input(">>>")
    enter_password_admin_and_user()
    if answer.lower() == "admin":
        admin()
    elif answer.lower() == "user":
        user()

