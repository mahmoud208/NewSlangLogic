import re
import copy
from DataAccessLayer import *
 
lexemes = LoadData()
#matchedLexemes = []
#notMatchedLexemes = []
#history = []


#read input text line by line
def readfile(input="input.txt") :
   file = codecs.open("input.txt","r",encoding="utf-8-sig")
   input_list = []
   for line in file :
     input_list.append(line.replace("\r\n", "")) 
   return input_list

def GetStartPosition(pattern,sentence):
    pos = sentence.find(pattern)
    return pos

#function replace founded by special chracter
def ReplaceFoundbySpecialCharachter(lexeme,sentence,specialChar):
        sentence = sentence.replace(lexeme.name,specialChar,1)
        return sentence

#split sentence
def SplitSentence(sentence,specialChar):
     splited_sentence = sentence.split(specialChar) 
     return splited_sentence

#Merge and sort by position
def MergeAndSortByPosition(found,notfound):
    lexemes = found + notfound
    lexemes.sort(key = lambda obj:(obj.position[0]), reverse=False)
    return lexemes

#search in splited sentence to get other founded lexemes
def GetMatchesAndReplace(splited_sentence,position_tracker_sentence,specialChar,matchedLexemes,notMatchedLexemes,history):
     copySplitedSentence = copy.deepcopy(splited_sentence)

     for i in range(0,len(splited_sentence))  :
         for lex in lexemes :
             if lex.name in splited_sentence[i]:
                 #occurrence_count =splited_sentence[i].count(lex.name)
                 positionInOrginal = GetStartPosition(copySplitedSentence[i],position_tracker_sentence)
                 for m in re.finditer(lex.name, position_tracker_sentence):
                    copyLexeme = copy.deepcopy(lex)
                    copyLexeme.position = (m.start()  , m.end() - 1)
                    matchedLexemes.append(copyLexeme)
                    history.append(copyLexeme)
                    splited_sentence[i] = splited_sentence[i].replace(lex.name,specialChar,1)
                    position_tracker_sentence = position_tracker_sentence.replace(lex.name,len(lex.name) * specialChar,1)

     splitedPositionTracker = position_tracker_sentence.split('0')


     for lex in splitedPositionTracker:
         if lex:
             pos = (position_tracker_sentence.find(lex),(position_tracker_sentence.find(lex) + len(lex)) - 1)
             position_tracker_sentence = position_tracker_sentence.replace(lex,len(lex) * "0",1)
             notMatchedLexemes.append(Lexeme(-1,lex,-1,-1,True,pos))
             history.append(Lexeme(-1,lex,-1,-1,True,pos))
     return True
    

#########fire rule test cases############
#passed sequence
def FireRulesAllTrue(list):
    for lex in list :
        lex.rule_result = False
    return list

#rejected sequence
def FireRulesAllFalse(MergedList):
    for lex in MergedList :
        lex.rule_result = False
    return MergedList

def AtleastOneIsFalse(sequence):
    for i in range(len(sequence)):
        if i == 0:
            sequence[i].rule_result = False
        else:
            sequence[i].rule_result = True
    return sequence

#some passed and some failed
def FireRulesMixed(MergedList):
    for lex in MergedList[:2] :
        lex.rule_result = False
   
    for lex in MergedList[-3:]:
        lex.rule_result = False
    return MergedList
########################################
#Fire Rule 
def FireRule(MergedList):

    return MergedList


#get failed sequences
def GetFailedSequences(mergelist):
    temp = []
    sequences = []
    for i in range(0,len(mergelist)):
        if mergelist[i].rule_result == False:
            temp.append(mergelist[i])
            if temp and len(mergelist) - 1 == i:
                sequences.append(temp)
        else:
            if temp:
                sequences.append(temp)
                temp = []
        
    return sequences

#get all possible permutation
def GetAllPermutations(lists):
     PermutationLists = list(itertools.product(*lists))
     return PermutationLists 

#check if all the sequence pass
def IsSequencePassed(list):
    for lexeme in list:
        if lexeme.rule_result:
            continue
        else:
            return False
    return True

#validate some sequence
def ValidateSequence(list,sequence):
    #____________________________
    for lex in range(0,len(list)) :
        for item in range(0,len(sequence)) :
            if list[lex].name==sequence[item].name and list[lex].position==sequence[item].position:
               list[lex].rule_result = True
#____________________________________
               for i in range(0,len(list)):
                   if list[i].rule_result == False:
                      list[i].rule_result = True
                      list[i].lex_id = sequence[i].lex_id
                   else:
                        break
#___________________________________
               else:
                   break
               #_____________________________

#remove some sequence


def remove2(list,new_list,sequence):
     for item in range(0,len(sequence)):
         #for lex in range(0,len(list)):
         #new_list = copy.deepcopy(list)
         i=0
         #x=sequence[item].lex_id==list[i].lex_id and sequence[item].position==list[i].position
         while True:
                  if sequence[item].lex_id==list[i].lex_id and sequence[item].position==list[i].position:
                     #if list[i].rule_result==False:
                        list.remove(list[i])
                        break
                  i+=1      
                 
                   
             
         
#Check if list contains some element
def contains(list, filter):
    for x in list:
        if filter(x):
            return True
    return False

    #read Input
    input = readfile()

    #To Keep the position after replacing with special char
    positionTrackerSentence = readfile()
    positionTrackerSentenceCopy = copy.deepcopy(positionTrackerSentence)
#remove and replace sequence in list by new matches
#def removeAndReplaceSequence(list,sequence,newMatches):
#    if newMatches:
#       for lex in range (0,len[newMatches]):
#           if lex.rule_result==False:
#              lex.rule_result=True
#           #if new matches at the end of list 
#           if sequence[-1]==list[-1]:
#              RemoveSequence(list,sequence)
#              list=list.extend(newMatches)
#           elif sequence[0]==list[0]:
#                RemoveSequence(list,sequence)
#                list=newMatches.extend(list)
#           #else :
#           #     for x in rang(0,len(ist)):
#           #         for y in rang(0,len(sequence)):
#           #             if list[x]==sequence[0]:
#           return list



                  





def Process(sentence):
    matchedLexemes = []
    notMatchedLexemes = []
   # newconcatinatedLex=[]
    history = []
    positionTrackerSentence = copy.deepcopy(sentence)
    positionTrackerSentenceCopy = copy.deepcopy(positionTrackerSentence)

    for lexeme in lexemes:
            if lexeme.name in sentence:
                for m in re.finditer(lexeme.name, sentence):
                    copyLexeme = copy.deepcopy(lexeme)
                    copyLexeme.position = (m.start(), m.end() - 1)
                    matchedLexemes.append(copyLexeme)
                    history.append(copyLexeme)
                    sentence = ReplaceFoundbySpecialCharachter(lexeme,sentence,"0")
                    positionTrackerSentence = ReplaceFoundbySpecialCharachter(lexeme,positionTrackerSentence,len(lexeme.name) * "0")
                splitedList = SplitSentence(sentence,"0")
                isFinished = GetMatchesAndReplace(splitedList,positionTrackerSentence,"0",matchedLexemes,notMatchedLexemes,history)
                if isFinished:
                    break
    
    output = MergeAndSortByPosition(matchedLexemes,notMatchedLexemes)
    
    #apply Fire Rule
    FireRulesMixed(output)
    
    #Get All Failed Sequences
    allFailedSequences = GetFailedSequences(output)

    #get maches for every sequence
    for sequence in allFailedSequences:
        sequenceMatches = []
        for lex in sequence:
            matches = dataAccessLayer.GetMatchesFromDb(lex)
            sequenceMatches.append(matches)
        permutations = GetAllPermutations(sequenceMatches)
        for permutation in permutations:
            ruleResult =FireRulesAllFalse(permutation)
            if IsSequencePassed(ruleResult):
                ValidateSequence(output,permutation)
                sequenceMatches = []
                break

        #if sequence fails add it to the history and apply concatination
        #scenario
        if not IsSequencePassed(sequence):
            for lexeme in sequence:
                if not contains(history, lambda x: x.lex_id == lexeme.lex_id):
                    history.append(lexeme)

        #Apply concatination scenario if permutation failed
            concatinatedLex = "".join([lex.name for lex in sequence])
            new_list = copy.deepcopy(output)
            remove2(output,new_list,sequence)
            
            for lexeme in lexemes:
                #if lex not found in history
                if lexeme.name in concatinatedLex :#and not contains(history, lambda lex: lex.lex_id == lexeme.lex_id):
                    #______________________________________
                              
                    ValidateSequence(output,sequence)
                    #_____________________________________
                    #lexeme.rule_result = True
                    Position = (sequence[0].position[0],sequence[-1].position[1])
                    for m in re.finditer(lexeme.name, concatinatedLex):
                        copyLexeme = copy.deepcopy(lexeme)
                        copyLexeme.position = (m.start() + Position[0]  , m.end() - 1 + Position[0])
                        #______________________________________
                        ValidateSequence(output,sequence)
                        #__________________________________
                        copyLexeme.rule_result = True
                        if not contains(history, lambda lex: lex.lex_id == lexeme.lex_id and lex.position==copyLexeme.position):
                            if copyLexeme.rule_result==False:
                                copyLexeme.rule_result=True
                            output.append(copyLexeme)
                            #____________________________________
                            #newconcatinatedLex.append(lexeme)  
                            #___________________________________
                            concatinatedLex = concatinatedLex.replace(lexeme.name,len(lexeme.name) * "0",1)

                    splited_sentence = concatinatedLex.split("0")

                    for i in range(0,len(splited_sentence)):
                        if not splited_sentence[i]:
                            continue
                        for lex in lexemes :
                            if lex.name in splited_sentence[i]:#and not contains(history, lambda lexeme: lexeme.lex_id == lex.lex_id):
                               
                                for m in re.finditer(lex.name, concatinatedLex):
                                    copyLexeme = copy.deepcopy(lex)
                                    copyLexeme.position = (m.start() + Position[0]  , m.end() - 1 + Position[0])
                                    
                                    if not contains(history, lambda lex: lex.lex_id == copyLexeme.lex_id and lex.position==copyLexeme.position):
                                        if copyLexeme.rule_result==False:
                                            copyLexeme.rule_result=True
                                            #______________________________________
                                            ValidateSequence(output,sequence)

                                        #newconcatinatedLex.append(lex)
                                           
                                            #_________________________________
                                        #lex.rule_result=True
                                         #copyLexeme = copy.deepcopy(lex)
                                        #copyLexeme.rule_result = True
                                            output.append(copyLexeme)
                    
                                        #-----------------------------------------------
                                        #concatinatedLex=concatinatedLex.replace(lex.name,"0")
                                        #
                                        #for x in output :
                                        #    if x.rule_result==False:
                                        #        lex.rule_result=True
                                    concatinatedLex = concatinatedLex.replace(lex.name,len(lex.name) * "0",1)
                    for i in splited_sentence:
                        Position = (sequence[0].position[0],sequence[-1].position[1])
                        output.append(Lexeme(-1,i,-1,-1,True,Position))   
                    concatinatedLexTracker = concatinatedLex.split('0')                    
                    for lex in concatinatedLexTracker:
                        if lex:
                            pos = (concatinatedLex.find(lex) + Position[0],(concatinatedLex.find(lex) + len(lex)) - 1 + Position[0])
                            concatinatedLex = concatinatedLex.replace(lex,len(lex) * "0",1)
                            if not contains(history, lambda lexeme: lexeme.position == pos):
                                #_______________________________________________________
                                #newconcatinatedLex.append(Lexeme(-1,lex,-1,-1,True,pos))
                                #________________________________________________________
                                output.append(Lexeme(-1,lex,-1,-1,True,pos))
                                #-----------------------------------------------
                            #else:
                            #    output.append(Lexeme(-1,lex,-1,-1,True,pos))
                                #---------------------------------------------
                    #if concatinatedLex != "".join([lex.name for lex in sequence]):
                        #remove the previous sequence
                        #RemoveSequence(output,sequence)
                #to continue the loop to appy the operation on concatinated lists
                    
                    
                continue
            continue
    output.sort(key = lambda obj:(obj.position[0]), reverse=False)       
    return output

#analyse the input.txt file
def Run():
    sentences = readfile()
    with open("Output.txt", "w") as csvFile:
            isLastLineDashed = False
            for j in range(len(sentences)):
                if j== len(sentences)-1:
                    isLastLineDashed=True
                output = Process(sentences[j])
                line = sentences[j]
                line+="\n"
                notfound = ""
                isLastLineContinued = False
                
                for i in range(len(output)):
                    if i== len(output)-1:
                        isLastLineContinued=True

                    if output[i].lex_id < 0:
                        notfound = "NOTFOUND"
                    line+=notfound + " at position" + str(output[i].position) + "\n"
                    line +=str(output[i].lex_id) + "," + output[i].name + "," + str(output[i].score1) + "," + str(output[i].score2)
                    for feature in output[i].features:
                        line+="," + feature.name + "=" + feature.value
                    line+="\n"
                    if not isLastLineContinued:
                        line+="____________________________________________________________\n"
                    notfound = ""
                if not isLastLineDashed:    
                    line+="------------------------------------------------------------------\n"
                csvFile.write(line.encode('Utf-8',"ignore"))

