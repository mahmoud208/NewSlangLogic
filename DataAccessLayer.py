import codecs
import csv
import os
import itertools
from model import*
import sys

def LoadData(filename="Dictionary.csv"): 
        list_of_lexemes = []
        
        with codecs.open(filename)  as csvfile:
            lines = csv.reader(csvfile)
            data = list(lines)
            for row in data:
                lexeme = Lexeme(unicode((row[0]),'utf-8'),unicode((row[3]),'utf-8'),unicode((row[1]),'utf-8'),unicode((row[2]),'utf-8'),True,(0,0))
                features = []
                for x in range(len(row) - 1):
                    if x > 3 and row[x] != "":
                        the_feature = row[x].split('=')
                        feature_obj = feature(unicode(the_feature[0],'utf-8'),unicode(the_feature[1],'utf-8'))
                        features.append(feature_obj)
                        lexeme.features = features
                list_of_lexemes.append(lexeme)
        #sort dictionarry by the longest length
        list_of_lexemes.sort(key = lambda obj:(len(obj.name),obj.score1,obj.score2), reverse=True)
   
        return list_of_lexemes  

class dataAccessLayer:
    #static member
    __lexemes = LoadData()

    def __init__(self):
        pass

    #get matches lexemes from the database
    @classmethod
    def GetMatchesFromDb(cls,lex):
        matches = []
        
        for lexeme in cls.__lexemes:
           if lexeme.name == lex.name:
               matches.append(lexeme)
           if matches:
               return matches
           else:
               matches.append(lex)
               return matches