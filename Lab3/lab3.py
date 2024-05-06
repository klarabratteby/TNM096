import random
import copy

class Clause():

  def __init__(self, pos=None,neg=None): 
    self.pos = set(pos) if pos else set()
    self.neg = set(neg) if neg else set()

  # Return string 
  def __str__(self):
    return f"{''.join(self.pos) + ''.join('¬'+ x for x in self.neg)}"
  
  def issubset(self, other):
        return self.pos.issubset(other.pos) and self.neg.issubset(other.neg)
  
  #Subsumption
  def subsumption(self,other):
    # Check if C1 is a subset of C2 (both pos and neg)
    if self.pos.issubset(other.pos) and self.neg.issubset(other.neg):
        # Check if every literal in C1 is also in C2
        if self.pos != other.pos or self.neg != other.neg:
          return True
    return False

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

  # Construct resolvent with the remaining literals
  C.pos = C1.pos.union(C2.pos)
  C.neg = C2.neg.union(C1.neg)

  # Tautology
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

    # Resolution loop, continue until we have no resolvants left
    while KB != KBbis:      
        S = set()
        KBbis = copy.deepcopy(KB)
        
        # Iterate over all pairs of clauses
        for C1 in KB:
            for C2 in KB:
                # We dont compare identical clauses
                if C1 == C2: 
                    continue
                # Apply resolution to generate a new clause
                C = resolution(copy.deepcopy(C1), copy.deepcopy(C2))
                
                # Add new clause to set 
                if C is not False:
                    S.add(C)

        # If no new clauses are generated, return KB     
        if len(S) == 0:
            return KB
        
        KB = incorporate(S, KB)
        
    return KB

# Iterate over each clause in S
def incorporate(S, KB):
    for C in S:
        KB = incorporate_clause(C, KB)
    return KB

def incorporate_clause(C, KB):
    for B in KB:
        # Check if B is a subset of C
        if B.pos.issubset(C.pos) and B.neg.issubset(C.neg):
            return KB # return KB as it is 
    
    for B in KB.copy():
        # Check if C is a subset of B
        if C.pos.issubset(B.pos) and C.neg.issubset(B.neg):
            KB.remove(B)
    # Add C to KB
    KB.add(C)
    
    return KB

      
if __name__ == "__main__":
  
  # Task A
  # Resolution
  # Example 1
  C1 = Clause(['a','b'],['c'])
  C2 = Clause(['b','c'])
  resolvent = resolution(C1,C2)
  print("Resolvent:", resolvent)

  # Example 2
  C1 = Clause(['a','b'], ['c'])
  C2 = Clause(['b','d'],['g'])
  resolvent = resolution(C1,C2)
  print("Resolvent:", resolvent)
  #solved = solver(S)

  # Example 3
  C1 = Clause(['c','t'], ['b'])
  C2 = Clause(['b','z'],['c'])
  resolvent = resolution(C1,C2)
  print("Resolvent:", resolvent)

  
  # Subsumption 
  # Example 1
  C1 = Clause(['c','a'])
  C2 = Clause(['a','b','c'])
  result = C1.subsumption(C2)
  print("Strict subset:", result)

  # Example 2
  C1 = Clause(['b'],['c'])
  C2 = Clause(['a','b'],['c'])
  result = C1.subsumption(C2)
  print("Strict subset:", result)

  # Example 3
  C1 = Clause(['b'],['f','c'])
  C2 = Clause(['a','b'],['c'])
  result = C1.subsumption(C2)
  print("Strict subset:", result)

  # Example 4
  C1 = Clause(['b'])
  C2 = Clause(['a','b'],['c'])
  result = C1.subsumption(C2)
  print("Strict subset:", result)

  # Example 5
  C1 = Clause(['b','a'],['c'])
  C2 = Clause(['a','b'],['c'])
  result1 = C1.subsumption(C2)
  result2 = C1.issubset(C2)
  print("Strict subset:", result2)

  
  # Drawing conclusions
  #1.
  C1 = Clause(['ice'],['sun','money'])
  C2 = Clause(['ice', 'movie'],['money'])
  C3 = Clause(['money'],['movie'])
  C4 = Clause([],['movie','ice'])
  C5 = Clause(['movie'])
  C6 = Clause(['sun','money','cry'])
  #2. 
  KB = {C1, C2, C3, C4, C5, C6}
  #3.
  solved = solver(KB)
  print("")
  print("Result is:")
  for C in solved:
    print(C)
  
  
  # Task B
  # Logic Gates puzzle
  # Initial conditions
  C1 = Clause([],['A'])
  C2 = Clause(['B'])
  C3 = Clause(['C'])
  C4 = Clause(['D'])
  C5 = Clause(['E'])
  C6 = Clause([],['F'])
  # A XOR B = G
  C7 = Clause(['A','B'],['G']) 
  C8 = Clause([],['A','B','G'])
  C9 = Clause(['B','G'],['A'])
  C10 = Clause(['A','G'],['B'])
  # C XOR D = H
  C11 = Clause(['C','D'],['H'])
  C12 = Clause([],['C','D','H'])
  C13 = Clause(['D','H'],['C'])
  C14 = Clause(['C','H'],['D'])
  # E XOR F = I
  C15 = Clause(['E','F'],['I'])
  C16 = Clause([],['E','F','I'])
  C17 = Clause(['F','I'],['E'])
  C18 = Clause(['E','I'],['F'])
  # G XOR H = J
  C19 = Clause(['G','H'],['J'])
  C20 = Clause([],['G','H','J'])
  C21 = Clause(['H','J'],['G'])
  C22 = Clause(['G','J'],['H'])
  # J XOR I = K
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
  





