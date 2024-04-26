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
        print("adding "+str(C))
        KB = incorporate_clause(C, KB)
        print("KB is now")
        for KBel in KB:
            print(KBel)
        print("")
    
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
   # C1 = Clause([],['A'])
   # C2 = Clause(['B'])
   # C3 = Clause(['C'])
   # C4 = Clause(['D'])
   # C5 = Clause(['E'])
   # C6 = Clause([],['F'])
   # C7 = Clause(['A','G'],['B'])
   # C8 = Clause(['B','G'],['A'])
   # C9 = Clause(['C','H'],['D'])
   # C10 = Clause(['D','H'],['C'])
   # C11 = Clause(['E','I'],['F'])
   # C12 = Clause(['F','I'],['E'])
   # C13 = Clause(['G','J'],['H'])
   # C14 = Clause(['H','J'],['G'])
   # C15 = Clause(['I','K'],['J'])
   # C16 = Clause(['J','K'],['I'])
    # C1 = Clause([],['A'])
    # C2 = Clause(['B'])
    # C3 = Clause(['C'])
    # C4 = Clause(['D'])
    # C5 = Clause(['E'])
    # C6 = Clause([],['F'])
    # C7 = Clause(['G','A'],['A'])
    # C8 = Clause(['G','B'],['A'])
    # C9 = Clause(['G','A'],['B'])
    # C10 = Clause(['G','B'],['B'])
    # C11 = Clause(['H','C'],['C'])
    # C12 = Clause(['H','D'],['C'])
    # C13 = Clause(['H','C'],['D'])
    # C14 = Clause(['H','D'],['D'])
    # C15 = Clause(['I','E'],['E'])
    # C16 = Clause(['I','F'],['E'])
    # C17 = Clause(['I','E'],['F'])
    # C18 = Clause(['I','F'],['F'])
    # C19 = Clause(['J','G'],['G'])
    # C20 = Clause(['J','H'],['G'])
    # C21 = Clause(['J','G'],['H'])
    # C22 = Clause(['J','H'],['H'])
    # C23 = Clause(['K','J'],['J'])
    # C24 = Clause(['K','I'],['J'])
    # C25 = Clause(['K','J'],['I'])
    # C26 = Clause(['K','I'],['I'])
    # C27 = Clause(['A'],['G','A'])
    # C28 = Clause(['A'],['G','B'])
    # C29 = Clause(['B'],['G','A'])
    # C30 = Clause(['B'],['G','B'])
    # C31 = Clause(['C'],['H','C'])
    # C32 = Clause(['C'],['H','D'])
    # C33 = Clause(['D'],['H','C'])
    # C34 = Clause(['D'],['H','D'])
    # C35 = Clause(['E'],['I','E'])
    # C36 = Clause(['E'],['I','F'])
    # C37 = Clause(['F'],['I','E'])
    # C38 = Clause(['F'],['I','F'])
    # C39 = Clause(['G'],['J','G'])
    # C40 = Clause(['G'],['J','H'])
    # C41 = Clause(['H'],['J','G'])
    # C42 = Clause(['H'],['J','H'])
    # C43 = Clause(['J'],['K','J'])
    # C44 = Clause(['J'],['K','I'])
    # C45 = Clause(['I'],['K','J'])
    # C46 = Clause(['I'],['K','I'])
    # KB = {C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, 
    #       C11, C12, C13, C14, C15, C16, C17, C18, C19, C20,
    #       C21, C22, C23, C24, C25, C26, C27, C28, C29, C30,
    #       C31, C32, C33, C34, C35, C36, C37, C38, C39, C40,
    #       C41, C42, C43, C44, C45, C46}
    C1 = Clause([],['A'])
    C2 = Clause(['B'])
    C3 = Clause(['C'])
    C4 = Clause(['D'])
    C5 = Clause(['E'])
    C6 = Clause([],['F'])
    C7 = Clause(['G','A'],['A'])
    C8 = Clause(['G','B'],['A'])
    C9 = Clause(['G','A'],['B'])
    C10 = Clause(['G','B'],['B'])
    C11 = Clause(['H','C'],['C'])
    C12 = Clause(['H','D'],['C'])
    C13 = Clause(['H','C'],['D'])
    C14 = Clause(['H','D'],['D'])
    C15 = Clause(['I','E'],['E'])
    C16 = Clause(['I','F'],['E'])
    C17 = Clause(['I','E'],['F'])
    C18 = Clause(['I','F'],['F'])
    C19 = Clause(['J','G'],['G'])
    C20 = Clause(['J','H'],['G'])
    C21 = Clause(['J','G'],['H'])
    C22 = Clause(['J','H'],['H'])
    C23 = Clause(['K','J'],['J'])
    C24 = Clause(['K','I'],['J'])
    C25 = Clause(['K','J'],['I'])
    C26 = Clause(['K','I'],['I'])
    KB = {C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, 
          C11, C12, C13, C14, C15, C16, C17, C18, C19, C20,
          C21, C22, C23, C24, C25, C26}
  
    solved = solver(KB)
    print("")
    print("Result is:")
    for Csolved in solved:
        print(Csolved)





