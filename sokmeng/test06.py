questions =[{
        "title": "What is minimum age to vote in Cambodia ?",
        "answers": "['15', '18', '21', '16']",
        "correct": 18
    },
    {
        "title": "What many people in Cambodia ?",
        "answers": "['15', '18', '21', '16']",
        "correct": 16
    },
    {
        "title": "What many province in Cambodia ?",
        "answers": "['15', '18', '21', '16']",
        "correct": 25
    }
]

ask_more_use = []
def more_ask_user():
    n= 0
    while n<1:
        print("--------------questions--------------")
        user_questions=input("enter your question++++>>>>>>")
        ask_more_use.append(user_questions)
        print("----------------answer----------------")
        for i in range(4):
            user_answers = input("input your answer 4 answer:...")
            ask_more_use.append(user_answers)
        print("----------------correct----------------")
        choose_answer()
        print(ask_more_use)
        n+=1
    else:
        print("u want add more questions?")
        user_answer = input("you want add more question (y/n----->")
        if user_answer.lower() == "y":
            more_ask_user()
        elif user_answer.lower()=="n":
            ask_loing()
def choose_answer():
    user_choise = input("choose one correct answer:....")
    ask_more_use.append(user_choise)
def choose_option_user():
    print("choose options:\n"
          "1-->start game now\n"
          "2-->buy hero\n"
          "3-->invite friends\n")

def welcome():
        print("Hello,  welcome to questions game by python.!!!")
def ask_loing():
        who=input("Who are you?\n"
                  "im a admin(type admin)  or  im a a user(type user)\n"
                  "who...")
        if who=="admin":
                admin()
        elif who=="user":
                user()
        elif who != "user" and who!= "admin":
                not_found()
                choose_again()
                ask_loing()

def admin():
        password_admin = int(input("password_admin...."))
        if password_admin == 123:
                choose_option_admin()
        else:
                not_found()
                choose_again()
                ask_loing()
def choose_option_admin():
    print("choose options:\n"
            "A-->add user\n"
            "E-->Edit\n"
            "C-->check product\n"
            "d-->add question")
    admin_choose_option = input("is option...").lower()
    if admin_choose_option == 'a':
            print("Added user.")
    elif admin_choose_option == 'e':
            print("edited.")
    elif admin_choose_option == 'c':
            print("Checking.")
    elif admin_choose_option == 'd':
            more_ask_user()
    elif admin_choose_option != choose_option_admin():
            not_found()
            choose_option_admin()

def  read_all_question():
    score=0
    print("Questions are ....")
    i=0
    for check in questions:
        print(check['title'])
        print(check['answers'])
        answer_questions = int(input("enter your answer :..."))
        if answer_questions == check['correct']:
           score+=1
        elif answer_questions != check['correct']:
           score+=0
        i += 1
    print("losed, total =\n" , score)
    more()


def more():
    sum = 0
    j = 0
    print(ask_more_use)
    for correct_answer in ask_more_use[5]:
        answer = input(" ")
        if answer == correct_answer:
            print("Correct!")
            sum+=1
        else:
            print(f"The answer is {correct_answer!r}, not {answer!r}")
            sum+=0
        j+=1
    print("The total",sum)
def user():
    password_user = int(input("password is...."))
    if password_user == 456:
        choose_option_user()
        user_option = int(input("option   ---"))
        if user_option == 1:
            print('game is starting...')
            read_all_question()
        elif user_option == 2:
            print("choose hero u wanna buys.")
        elif user_option == 3:
            print("added.")
        else:
            not_found()
            choose_option_user()
    else:
        ask_loing()
def not_found():
        print("sorry not found!!")

def choose_again():
        print("choose again!!!")

def end():
    print("end!!")

if __name__ == "__main__":
        welcome()
        ask_loing()