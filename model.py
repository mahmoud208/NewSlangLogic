class feature:

    def __init__(self,name, value):
        self.name=name
        self.value = value
        
class Lexeme:
   
    def __init__(self,lex_id,name, score1,score2,rule_result,position):
      self.lex_id=lex_id
      self.name = name
      self.score2 = score2
      self.score1= score1
      self.rule_result= rule_result
      self.features=[]
      self.position = position

class NOtFoundLexeme:
     def __init__(self,lex_id,name,start_position,end_position,no_found):
      self.lex_id=lex_id
      self.name = name
      self.start_position = start_position
      self.end_position= end_position
      self.no_found= no_found
     
