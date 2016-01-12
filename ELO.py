# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 00:26:26 2016

@author: James
"""

import math

#Defined from http://en.wikipedia.org/wiki/Elo_rating_system#Mathematical_details
def calc_odds(player_a, player_b):
        q_a = math.pow(10, (float(player_a)/400))
        q_b = math.pow(10, (float(player_b)/400))
        exp_a = q_a/(q_a + q_b)
        exp_b = q_b/(q_a + q_b)
        return (exp_a, exp_b)

#Defined from http://forrst.com/posts/An_Elo_Rating_function_in_Python_written_for_foo-hQl
def cal_elo_rank(video_a_rank, video_b_rank, winner=0,penalize_loser=True):
        if winner is 2:
                return  (video_a_rank, video_b_rank)
        elif winner is 0:
                winner_rank, loser_rank = video_a_rank, video_b_rank
        else:
                winner_rank, loser_rank = video_b_rank, video_a_rank
        
        rank_diff = winner_rank - loser_rank
        exp = float(rank_diff * -1) / 400
        odds = 1/(1 + math.pow(10,exp))
        if winner_rank < 2100:
                k = 32
        elif winner_rank >= 2100 and winner_rank < 2400:
                k = 24
        else:
                k = 16
        new_winner_rank = round(winner_rank + (k*(1-odds)))
        if penalize_loser:
                new_rank_diff = new_winner_rank - winner_rank
                new_loser_rank = loser_rank - new_rank_diff
        else:
                new_loser_rank = loser_rank
        
        if new_loser_rank < 1:
                new_loser_rank = 1
        if winner is 0:
                return (new_winner_rank, new_loser_rank)
        return (new_loser_rank, new_winner_rank)

def getRankList(ELOs):
        ranks = []
        for key in ELOs:
                ranks.append((key, ELOs[key].get_score()))
        ranks.sort(key=lambda tup: tup[1])
        list1, list2 = zip(*ranks)
        return ranks