import sys

class Player:
    def __init__(self, name, old, score):
        self.name = name
        self.old = int(old)
        self.score = int(score)

    def __bool__(self):
        return self.score > 0



# считывание списка из входного потока (эту строчку и список lst_in не менять)
# lst_in = list(map(str.strip, sys.stdin.readlines()))

lst_in = ['Балакирев; 34; 2048',
'Mediel; 27; 0',
'Влад; 18; 9012',
'Nina P; 33; 0']


players = [Player(*i.split(';')) for i in lst_in]
# print(players)
players_filtered = list(filter(lambda x: bool(x.score), players))
# print(players_filtered)