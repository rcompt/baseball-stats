# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 00:28:07 2016

@author: James
"""

import ELO
import pickle
import matplotlib.pyplot as plt
from scipy import stats

years = [str(x) for x in range(2005,2016)]
year_range = years[0] + "_to_" + years[-1]
#season = "2014"

def compare_dates(date1, date2):
    months = {
        "Jan":1,
        "Feb":2,
        "Mar":3,
        "Apr":4,
        "May":5,
        "Jun":6,
        "Jul":7,
        "Aug":8,
        "Sep":9,
        "Oct":10,
        "Nov":11,
        "Dec":12
    }
    month1 = months.get(date1.split(",")[0])
    month2 = months.get(date2.split(",")[0])
    if month1 < month2:
        return -1
    elif month1 > month2:
        return 1
    else:
        day1 = int(date1.split(",")[1])
        day2 = int(date2.split(",")[1])
        if day1 < day2:
            return 1
        else:
            return -1

def check_teams(game):
    if game.team_1 == "TBR":
        game.team_1 = "TBD"
    elif game.team_2 == "TBR":
        game.team_2 = "TBD"
    if game.winner == "TBR":
        game.winner = "TBD"
    if game.team_1 == "LAA":
        game.team_1 = "ANA"
    elif game.team_2 == "LAA":
        game.team_2 = "ANA"
    if game.winner == "LAA":
        game.winner = "ANA"
    if game.team_1 == "MIA":
        game.team_1 = "FLA"
    elif game.team_2 == "MIA":
        game.team_2 = "FLA"
    if game.winner == "MIA":
        game.winner = "FLA"
    return game

#Gather data
file_p = open(year_range + "_seasons.p","rb")
seasons = pickle.load(file_p)
file_p.close()
ari_score = []
ari_wins = []
ari_loses = []
correct = 0
first_half_correct = 0
half_season_correct = 0
total = 0
first_half_total = 0
total_half_season = 0
for season in seasons:
    dates = {}
    teams = {}
    wins = 0
    loses = 0
    for team in seasons[season]:
        teams[team] = seasons[season][team]
        team = seasons[season][team]
        for game in team.games:
            date = game.month + "," + game.day
            if date not in dates:
                dates[date] = []
            flag = False
            for game_date in dates[date]:
                if game_date.winner == game.winner and game_date.month == game.month and game_date.day == game.day and game_date.team_1 == game.team_2 and game_date.team_2 == game.team_1:
                    flag = True
                    break
            if not flag:
                dates[date].append(game)
            
    for date in dates:
        for game in dates[date]:
            game = check_teams(game)
            if game.winner == "ARI":
                wins += 1
            elif game.get_opponent(game.winner) == "ARI":
                loses += 1
            winner_odds, loser_odds = ELO.calc_odds(teams[game.winner].get_score(),teams[game.get_opponent(game.winner)].get_score())
            if winner_odds > loser_odds:
                correct += 1
                if compare_dates(date,"Jul,10") > 0:
                    half_season_correct += 1
                else:
                    first_half_correct += 1
            total += 1
            if compare_dates(date,"Jul,10") > 0:
                total_half_season += 1
            else:
                first_half_total += 1

                
            winner_new_score, loser_new_score = ELO.cal_elo_rank(teams[game.winner].get_score(),teams[game.get_opponent(game.winner)].get_score())
            teams[game.winner].update_score(winner_new_score)
            teams[game.get_opponent(game.winner)].update_score(loser_new_score)
    
    ranked_list = ELO.getRankList(teams)
    ari_score.append(teams["ARI"].get_score())
    ari_wins.append(wins)
    ari_loses.append(loses)
    
data = zip(ari_score,ari_wins)
data.sort(key=lambda tup: tup[0])
ari_score, ari_wins = zip(*data)
plt.plot(ari_score,ari_wins)
plt.show()
slope, intercept, r_value, p_value, std_err = stats.linregress(ari_score,ari_wins)
print("ELO accuracy in predictions")
print(float(correct)/total)
print("ELO accuracy in 1st half predictions")
print(float(first_half_correct)/first_half_total)
print("ELO accuracy in 2nd half predictions")
print(float(half_season_correct)/total_half_season)
plt.plot(ari_score,[slope*x + intercept for x in ari_score])