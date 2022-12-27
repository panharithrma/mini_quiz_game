questions = [
        "1--> who are you?",
        "--> im a admin",
        "--> im a user"
]
print(questions[0])
for i in questions:
        i = int(input("choose one option:"))
        if i==1:
                print(questions[1])
                print("plz enter your passwork:")
                passwork = int(input("....."))
                if passwork==123:
                        print("checking user")
                        print("and more option can views")
                break

        elif i==2:
                print(questions[2])
                print("welcome to game is start.")
                def option():
                        print("[1]--->choose (Y) for open and")
                        print("[2]--->choose  (N) for no")
                        print("[3]--->not found")
                option()
                x = str(input("plz choose one option:"))
                while x=="y" and x=="n":
                        if x == "y":
                                print("......your game is starting.")
                                break
                        elif x == "n":
                                print("......your is closed.")
                                break
                        else:
                                print(".....sorry plz choose option again")
                                break
                        x += 1


                # score user

                def score():
                        print("++++buttom blue is win")
                        print("++++buttom red is lose")
                score()
                y = str(input("when game finished have blue or red buttom:"))
                while y == "blue" or y == "red" and x != 2:
                        if y == "blue":
                                print("contragulation you got 100")
                                break
                        elif y == "red":
                                print("lose you got 50")
                                break
                        y += 1
        break