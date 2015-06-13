##############
## Problem 22
##
## 
import csv

with open('p022_names.txt', 'rb') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
    names = csv_reader.next()

names2 = sorted(names)

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def letter_score(letter):
    if len(letter) > 1:
        raise ValueError('This function accepts letters only')
    return alphabet.index(letter)+1

def score(name):
    score = 0
    for j in range(len(name)):
        score += letter_score(name[j])
    return score

name_scores = [ score(names2[j])*(j+1) for j in range(len(names2)) ]
    
print_sol(22, sum(name_scores)) ## 871198282
