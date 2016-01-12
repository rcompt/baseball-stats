# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 14:41:13 2015

@author: James
"""

from lxml import html
import requests
from team_obj import team, game
import pickle

page_name = "http://www.baseball-reference.com/teams/"

years = [str(x) for x in range(2005,2016)]
year_range = years[0] + "_to_" + years[-1]

teams = ["ARI","ATL","BAL","BOS","CHC","CHW","CIN",
         "CLE","COL","DET","HOU","KCR","ANA","LAD",
         "FLA","MIL","MIN","NYM","NYY","OAK","PHI",
         "PIT","SDP","SFG","SEA","STL","TBD","TEX",
         "TOR","WSN"]
seasons = {}

for year in years:
    page_suffix = "/" + year + ".shtml"
    teams_dic = {}
    for t in teams:
        t_obj = team(t)
        
        page = requests.get(page_name + t_obj.name + page_suffix)
        tree = html.fromstring(page.text)
        games = tree.xpath('//span[@class="poptip"]/@tip')
        cleaned_games = [g for g in games if t_obj.name in g]
        for g in cleaned_games:
            games_info = g.split(" ")
            game_num = games_info[0][:-1]
            game_month = games_info[1]
            game_day = games_info[2][:-1]
            game_team = games_info[3]
            game_day_record = games_info[4]
            game_result = games_info[5]
            if game_result == "beat":
                game_opponent = games_info[6][:-1]
                game_score = games_info[7]
                winner = t
            else:
                game_opponent = games_info[7][:-1]
                game_score = games_info[8]
                winner = game_opponent
            g = game(t,game_team,winner,game_score,game_month,game_day)
            t_obj.add_game(g)
        teams_dic[t] = t_obj
    seasons[year] = teams_dic

file_p = open(year_range + "_seasons.p","wb")
pickle.dump(seasons,file_p)
file_p.close()
    
    

    