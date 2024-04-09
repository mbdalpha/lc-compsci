import random


class Winner:
    def __init__(self):
        self.total = 0
        self.rock = 0
        self.paper = 0
        self.scissors = 0

    def add_win(self, rps):
        self.total =

player = Winner()
computer = Winner()
tie = Winner()


choices = ['rock', 'paper', 'scissors']


def p_choose():
    #choice = input("Please choose between rock, paper, or scissors: ")
    choice = random.choice(choices)
    #print("You have chosen", choice)
    return choice.lower()


def c_choose():
    return random.choice(choices)


def play_round():
    player_choice = p_choose()

    computer_choice = c_choose()

    if player_choice == computer_choice:
        return ['tie', player_choice]
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
    (player_choice == 'paper' and computer_choice == 'rock') or \
    (player_choice == 'scissors' and computer_choice == 'paper'):
        return ['player', player_choice]
    else:
        return ['computer', computer_choice]


def game(n):
    i = 0
    p_win = 0
    c_win = 0
    t_win = 0



    pr = 0
    pp = 0
    ps = 0
    cr = 0
    cp = 0
    cs = 0
    tr = 0
    tp = 0
    ts = 0

    while i < n:
        result = play_round()
        i += 1
        if result[0] == 'player':
            p_win += 1
            if result [1] == 'rock':
                pr += 1
            elif result[1] == 'paper':
                pp += 1
            else:
                ps += 1

        elif result[0] == 'computer':
            c_win += 1
            if result [1] == 'rock':
                cr += 1
            elif result[1] == 'paper':
                cp += 1
            else:
                cs += 1

        else:
            t_win += 1
            if result [1] == 'rock':
                tr += 1
            elif result[1] == 'paper':
                tp += 1
            else:
                ts += 1

    print("\t\t\t\tOutcome\tRock\tPaper\tScissors")
    print("Player win\t\t" + str(p_win) + "\t\t" + str(pr) + "\t\t" + str(pp) + "\t\t" + str(ps))
    print("Computer win\t" + str(c_win) + "\t\t" + str(cr) + "\t\t" + str(cp) + "\t\t" + str(cs))
    print("Tie\t\t\t\t" + str(t_win) + "\t\t" + str(tr) + "\t\t" + str(tp) + "\t\t" + str(ts))
    t = [cr, cp, cs]
    if cr == max(t):
        c_strat = "rock"
        c_num = cr
    elif cp == max(t):
        c_strat = "paper"
        c_num = cp
    else:
        c_strat = "scissors"
        c_num = cs

    print("Computer best strategy was always to use", c_strat + ", which won", c_num, "times")


game(1000)





