import random
class Clause():

  def __init__(self, pos=None,neg=None): 
    self.pos = set(pos) if pos else set()
    self.neg = set(neg) if neg else set()

  # Return string 
  def __str__(self):
    return f"{''.join(self.pos) + ''.join('¬'+ x for x in self.neg)}"

def resolution(C1,C2):

  C = Clause() # empty clause for resolvent

  # No common 
  if not(C1.pos).intersection(C2.neg) and not (C1.neg).intersection(C2.pos):
    return None

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
  
# Not done
'''
solver(KB):
    while True:
        S = set()
        for C1 in KB:
            for C2 in KB:
                if C1 == C2:
                  continue
                C = resolution(C1, C2)
                if C is not False:
                  S = S.union({C})
'''
      
if __name__ == "__main__":
  # example 1
  C1 = Clause(['p','q'],['r'])
  C2 = Clause(['q','r'])
  resolvent = resolution(C1,C2)
  print("Resolvent:", resolvent)
  # example 2
  C1 = Clause(['a','b'], ['c'])
  C2 = Clause(['b','d'],['g'])
  resolvent = resolution(C1,C2)
  print("Resolvent:", resolvent)
  





