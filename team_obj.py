# -*- coding: utf-8 -*-
"""
Created on Sat Nov 07 16:51:26 2015

@author: James
"""

class game:
    def __init__(self, team1, team2, winner, score, month, day):
        self.team_1 = team1
        self.team_2 = team2
        self.winner = winner
        self.score = score
        self.month = month
        self.day = day
    def winner(self):
        return self.winner
    def score(self):
        return self.score

class team:
    name = ""
    def __init__(self, name):
        self.name = name
        self.games = []
        
    def __str__(self):
        return self.name
        
    def add_game(self, game):
        self.games.append(game)
        
    def name(self):
        return self.name
        
