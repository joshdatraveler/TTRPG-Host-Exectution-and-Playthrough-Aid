class Fighter:
  def __init__(self,name,health,initiative,suc_saves,fail_saves):
    self.name = name
    self.health = health
    self.initiative = initiative
    self.suc_saves = suc_saves
    self.fail_saves = fail_saves
  
  def __repr__(self):
    return '({},{},{},{},{})'.format(self.name,self.health,self.initiative,self.suc_saves,self.fail_saves)

  def __str__(self):
    return(str(self.name) + '\nHealth: ' 
    + str(self.health)+ '   Saves: ' + str(self.suc_saves))


def initiative_sort(char):
  return(char.initiative)

