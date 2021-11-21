# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 16:44:44 2021

@author: taher
"""

# The data we need to retrieve
import csv
import os

file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join('analysis','election_analysis.txt')

with open(file_to_load) as election_data:
     file_reader = csv.reader(election_data)
     
     for row in file_reader:
          print(row[0])
#The total number of votes cast


#complete list of candidates with votes


#percentage of votes for each candidate


#total number of votes for each candidate


#winner based on popular vote
election_data.close()
