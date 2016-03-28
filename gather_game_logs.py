# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 01:29:23 2016

@author: James
"""

import urllib2
import os

url = "http://www.retrosheet.org/gamelogs/"

for x in range(1871,2016,1):
    f_name = "gl" + str(x) + ".zip"
    url_f = url + f_name
    request = urllib2.urlopen(url_f)
    
    zip_f = open(os.getcwd() + os.sep + "game_logs" + os.sep + f_name,"w")
    zip_f.write(request.read())
    zip_f.close()
