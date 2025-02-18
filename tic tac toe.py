
import random
boardelements = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
winner = None
game = True
mode = int(input("1.play with a friend\n2.play with computer\n:"))
player = "x"

def clear(board_elements):
    global boardelements
    boardelements = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    #return boardelements

def board(boardelements):
    print(boardelements[0], " | ", boardelements[1], " | ", boardelements[2])
    print("--- ----- ---")
    print(boardelements[3], " | ", boardelements[4], " | ", boardelements[5])
    print("--- ----- ---")
    print(boardelements[6], " | ", boardelements[7], " | ", boardelements[8])

def playerinput(boardelements):
    inp = int(input("enter a number between 1 and 9 :"))
    if inp >= 1 and inp <= 9 and boardelements[inp-1] == " ":
        boardelements[inp-1] = player
    else:
        print("error")

def hor(boardelements):
    global winner
    if boardelements[0] == boardelements[1] == boardelements[2] and boardelements[1] != " ":
        winner = boardelements[0]
        return True
    elif boardelements[3] == boardelements[4] == boardelements[5] and boardelements[3] != " ":
        winner = boardelements[3]
        return True
    elif boardelements[6] == boardelements[7] == boardelements[8] and boardelements[8] != " ":
        winner = boardelements[6]
        return True

def ver(boardelements):
    global winner
    if boardelements[0] == boardelements[3] == boardelements[6] and boardelements[0] != " ":
        winner = boardelements[0]
        return True
    elif boardelements[1] == boardelements[4] == boardelements[7] and boardelements[1] != " ":
        winner = boardelements[1]
        return True
    elif boardelements[2] == boardelements[5] == boardelements[8] and boardelements[2] != " ":
        winner = boardelements[2]
        return True

def dia(boardelements):
    global winner
    if boardelements[0] == boardelements[4] == boardelements[8] and boardelements[0] != " ":
        winner = boardelements[0]
        return True
    elif boardelements[2] == boardelements[4] == boardelements[6] and boardelements[2] != " ":
        winner = boardelements[2]
        return True

def tie(boardelements):
    global game
    if " " not in boardelements:
        board(boardelements)
        print("--------TIE--------")
        board(boardelements)
        choice()
        clear(boardelements)

def win():
    global game
    if hor(boardelements) or ver(boardelements) or dia(boardelements):
        print(winner, " WINS! ")
        board(boardelements)
        choice()
        clear(boardelements)

def switch():
    global player
    if player == "x":
        player = "o"
    else:
        player = "x"

def comp(boardelements):
    while player == "o":
        pos = random.randint(0,8)
        if boardelements[pos] == " ":
            boardelements[pos] = "o"
            switch()

def choice():
    global game
    choice = int(input("1.Play again\n2.quit\n:"))
    if choice == 2:
        print("Thank you for playing")
        game = False
    else:
        clear(boardelements)
        game = True

while game:
    if mode == 1:
        board(boardelements)
        playerinput(boardelements)
        switch()
        win()
        tie(boardelements)
    elif mode == 2:
        board(boardelements)
        playerinput(boardelements)
        switch()
        comp(boardelements)
        win()
        tie(boardelements)
