import random
try:
    game = "start"
    def toss():
        tosscount = 0
        coin = ["head", "tail"]
        print("--------toss--------")
        print("best out of three")
        for i in range(0, 3):
            choice = str(input("Head or Tail? :")).lower()
            a = random.choice(coin)
            print("coin :", a)
            if choice == a:
                tosscount += 1
        if tosscount == 2:
            return True
        else:
            return False
    def batting():
        out = False
        score = 0
        while out == False:
            comp =random.randint(0,6)
            player = int(input("enter no. between 0 and 6 :"))
            print("computer :", comp)
            if comp == player:
                print("OUT!")
                print("score is", score)
                out = True
                return score
            else:
                score = score + player
                out = False
    def bowling():
        out = False
        score = 0
        while out == False:
            comp = random.randint(0, 6)
            player = int(input("enter no. between 0 and 6 :"))
            print("computer :", comp)
            if comp == player:
                print("OUT!")
                print("score is", score)
                out = True
                return score
            else:
                score = score + comp
                out = False
    while game == "start":
        while toss() is True:
            print("toss won!")
            play = input("batting or bowling? :")
            if play == "batting":
                print("--------batting--------")
                batting_score = batting()
                print("--------bowling--------")
                bowling_score = bowling()
                if batting_score > bowling_score:
                    print("player wins")
                    break
                else:
                    print("computer wins")
                    break
            elif play == "bowling":
                print("--------bowling--------")
                bowling_score = bowling()
                print("--------batting--------")
                batting_score = batting()
                if batting_score > bowling_score :
                    print("player wins")
                    break
                else:
                    print("computer wins")
                    break
            else:
                print("error")
                break
        else:
            print("toss lost, computer chose to bat.")
            print("--------bowling--------")
            bowling_score = bowling()
            print("--------batting--------")
            batting_score = batting()
            if batting_score > bowling_score:
                print("player wins")
            else:
                print("computer wins")
        game = input("start or quit?")
        if game == "quit":
            print("--------Thank you for playing--------")
            break
        else:
            print("--------New game-------")
            continue
except ValueError:
    print("Value error")