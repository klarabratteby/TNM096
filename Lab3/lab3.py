import random
import copy

class Clause():

  def __init__(self, pos=None,neg=None): 
    self.pos = set(pos) if pos else set()
    self.neg = set(neg) if neg else set()

  # Return string 
  def __str__(self):
    return f"{''.join(self.pos) + ''.join('¬'+ x for x in self.neg)}"

def resolution(C1, C2):

  C = Clause() # empty clause for resolvent

  # No common 
  if not(C1.pos).intersection(C2.neg) and not (C1.neg).intersection(C2.pos):
    return False

  if C1.pos.intersection(C2.neg):
    common_literal = random.choice(list(C1.pos.intersection(C2.neg)))
    C1.pos.remove(common_literal)
    C2.neg.remove(common_literal)
  else:
    common_literal = random.choice(list(C1.neg.intersection(C2.pos)))
    C1.neg.remove(common_literal)
    C2.pos.remove(common_literal)

  # Construct resolvent
  C.pos = C1.pos.union(C2.pos)
  C.neg = C2.neg.union(C1.neg)

  if C.pos.intersection(C.neg):
    return False

  return C

def solver(KB):
    KBbis = None

    #We clean KB
    for B in KB.copy():
        for C in KB.copy():
            if C != B and C.pos.issubset(B.pos) and C.neg.issubset(B.neg) and B in KB:
                KB.remove(B)

    while KB != KBbis:      
        S = set()
        KBbis = copy.deepcopy(KB)
        
        for C1 in KB:
            for C2 in KB:
                if C1 == C2:
                    continue
                C = resolution(copy.deepcopy(C1), copy.deepcopy(C2))
                if C is not False:
                    S = union(C, S)
                    
        if len(S) == 0:
            return KB
        
        KB = incorporate(S, KB)
        
    return KB

def incorporate(S, KB):
    for C in S:
        KB = incorporate_clause(C, KB)
    
    return KB

def incorporate_clause(C, KB):
    for B in KB:
        if B.pos.issubset(C.pos) and B.neg.issubset(C.neg):
            return KB
    
    for B in KB.copy():
        if C.pos.issubset(B.pos) and C.neg.issubset(B.neg):
            KB.remove(B)
    
    KB = union(C, KB)
    
    return KB

def union(C, S):
    for B in S:
        if C.pos == B.pos and C.neg == B.neg:
            return S

    S.add(C)
    
    return S
        

      
if __name__ == "__main__":
  # example 1
  #C1 = Clause(['p','q'],['r'])
  #C2 = Clause(['q','r'])
  #resolvent = resolution(C1,C2)
  #print("Resolvent:", resolvent)
  
  # example 2
  #C1 = Clause(['a','b'], ['c'])
  #C2 = Clause(['b','d'],['g'])
  #resolvent = resolution(C1,C2)
  #print("Resolvent:", resolvent)
  #solved = solver(S)
  
  # Drawing conclusions
  # C1 = Clause(['ice'],['sun','money'])
  # C2 = Clause(['ice', 'movie'],['money'])
  # C3 = Clause(['money'],['movie'])
  # C4 = Clause([],['movie','ice'])
  # C5 = Clause(['movie'])
  # C6 = Clause(['sun','money','cry'])
  # KB = {C1, C2, C3, C4, C5, C6}
  
    # Logic Gates puzzle
    C1 = Clause([],['A'])
    C2 = Clause(['B'])
    C3 = Clause(['C'])
    C4 = Clause(['D'])
    C5 = Clause(['E'])
    C6 = Clause([],['F'])
    C7 = Clause(['A','B'],['G'])
    C8 = Clause([],['A','B','G'])
    C9 = Clause(['B','G'],['A'])
    C10 = Clause(['A','G'],['B'])
    C11 = Clause(['C','D'],['H'])
    C12 = Clause([],['C','D','H'])
    C13 = Clause(['D','H'],['C'])
    C14 = Clause(['C','H'],['D'])
    C15 = Clause(['E','F'],['I'])
    C16 = Clause([],['E','F','I'])
    C17 = Clause(['F','I'],['E'])
    C18 = Clause(['E','I'],['F'])
    C19 = Clause(['G','H'],['J'])
    C20 = Clause([],['G','H','J'])
    C21 = Clause(['H','J'],['G'])
    C22 = Clause(['G','J'],['H'])
    C23 = Clause(['J','I'],['K'])
    C24 = Clause([],['J','I','K'])
    C25 = Clause(['I','K'],['J'])
    C26 = Clause(['J','K'],['J'])
    KB = {C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, 
          C11, C12, C13, C14, C15, C16, C17, C18, C19, C20,
          C21, C22, C23, C24, C25, C26}
  
    solved = solver(KB)
    print("")
    print("Result is:")
    for Csolved in solved:
        print(Csolved)





