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
    def get_opponent(self,team):
        if team == self.team_1:
            return self.team_2
        elif team == self.team_2:
            return self.team_1
        else:
            return ""
    def inverse(self,g1,g2):
        return g1[0] == g2[2] and g1[2] == g2[0]
        
    def equals(self,game):
        return self.winner == game.winner and self.month == game.month and self.day == game.day and self.inverse(self.score,game.score) and (self.team_1 == game.team_1 or self.team_1 == game.team_2) and (self.team_2 == game.team_1 or self.team_2 == game.team_2)
        

class team:
    def __init__(self, name):
        self.name = name
        self.games = []
        self.elo_score = 1500
        
    def __str__(self):
        return self.name
        
    def add_game(self, game):
        self.games.append(game)
        
    def name(self):
        return self.name
        
    def update_score(self, elo):
        self.elo_score = elo
    
    def get_score(self):
        return self.elo_score
        
