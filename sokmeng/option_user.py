#by admin you can ask user for some question
print("welcome to game is start.")
def option():
    print("[1]--->choose (Y) for open and")
    print("[2]--->choose  (N) for no")
    print("[3]--->not found")
option()
x = int(input("plz choose one option:"))
while x>0 and x<10:
    if x ==1:
        print("......your game is starting.")
        break
    elif x==2:
        print("......your is closed.")
        break
    else:
        print(".....sorry plz choose option again")
        break
    x+=1
#score user

def score():
     print("++++buttom blue is win")
     print("++++buttom red is lose")
score()
y =str(input("when game finished have blue or red buttom:"))
while y =="blue" or y=="red" and x!=2:
    if y=="blue":
        print("contragulation you got 100")
        break
    elif y=="red":
        print("lose you got 50")
        break
    y+=1