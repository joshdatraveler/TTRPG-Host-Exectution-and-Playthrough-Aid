import time
import battlelogfunction as blg
import main as ma
import character_stat_gen as csg

def menu():
  print ('This is a TTRPG Task Hub:\nWith this code you will be able to run various operations \nto hopefully lighten your load as a Game Host.\n')
  time.sleep(2)
  print('Current selection of tasks include:\n1. Random Item Generator:\n From Swords to Shields to Potions, this function will\n create a randomized item for you or your players to use.\n2. Battle Log:\n This function will help you keep up with turn order,\n individual player health, and fight history.\n3. Random Basic Stats Sheet:\n Quick, your players want to fight someone\n with no stats? Gotcha covered\n\n' )
  selection = int(input('Please select a task you would like to do: '))
  print('Loading Task '+str(selection))

  if selection == 1:
    time.sleep(1)
    return(ma.randomitemgen())
  elif selection == 2:
    time.sleep(1)
    return(blg.battlelog())
  elif selction == 3:
    time.sleep(1)
    return(csg.character_stat_gen())
  else:
    return ('This is not an avaialable task')
