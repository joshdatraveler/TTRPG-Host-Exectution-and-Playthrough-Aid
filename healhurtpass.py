def attack(fighters):
  singoraoe = int(input('What kind of attack is this: \n1. Individual Attack \n2. Area of Effect Attack: ')) 
  if singoraoe == 1:
    print('\nIf damage was dealt, who recieved it: ')
    for item in fighters:
      print  (str(fighters.index(item)+1)+ '. ' + str(item.name))
    dmgtaker = int(input('Enter here: '))
    dmgtaker = dmgtaker-1
    dmgtaken = int(input('Damage dealt: '))
    fighters[dmgtaker].health = fighters[dmgtaker].health - dmgtaken
    print('')
    return (fighters[dmgtaker])

def heal(fighters):
  pass
  
def cast(fighters):
  pass