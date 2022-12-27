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
            print("successed!")
            break
        else:
            print("not correct")
    else:
        print("welcom to game")