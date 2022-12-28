questions = {
    "title" : "who are you?",
    "answer":["write (a) im a admin", "write (u) im a user"],
    "answeradmin":"im a admin",
    "answeruser":"im a user",
    "password": [1 ,2, 4, 5, 6],
    "correct": 1,
    "titleadmin": "what do u want to do?  \n  "
              "--write(a) for add user\n  "
              "--write(e) for edit!"

}
if "title" in questions:
    print(questions["title"])
    if "answer" in questions:
        print(questions["answer"])
        anw = str(input("....:"))
        if anw.lower() == "a": #choose admin
            print(questions["answeradmin"])
            print("plz enter your password:")
            pas = int(input("--->"))
            if pas ==1:     #enter password
                print(questions["titleadmin"])
            else:
                print("plz check your password!!!")
        elif anw.lower() == "u":
            print(questions["answeruser"])

        else:
            print("your title not found!!")
