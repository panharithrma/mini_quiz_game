def option():
    print("who are you?")
    print("[1]-->im a admin")
    print("[2]-->im a user")
option()
x= int(input("choose one option :"))
while  x!=0:
    if x==1:
        print("plz enter your passwork:")
        y=int(input("....."))
        if y==123:
            view = [

            ]



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
