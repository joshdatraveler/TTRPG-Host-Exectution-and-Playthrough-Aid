import time
import healhurtpass as hhp
import character_class as cc

def battlelog():
  print ('\nWelcome to the Battle Log:\nHere you will be able to actively track battle stats \nand recieve a written log of events as they occur')
  time.sleep(3)
  player_count = int(input("First: How many combatants are there: "))
  fighters = []
  #using this to mirror so i can sort the above list
  print('')
  time.sleep(1)
  print('You will now enter the fighters info.')
  print('Note: the order of entry does not matter')
  

#loop that goes until the user has made a class for all of the players
  for item in range(player_count):
    #pause for dramatic affect
    time.sleep(2)
    #user inputs data for th class
    name = input("\nEnter the Combatant\'s name: ")
    name = name.capitalize()
    health = int(input('Enter the Combatant\'s current health: '))
    initiative = int(input('Enter the Combatant\'s initiative roll: '))

    #creating the variable that will be stored in the dictionary along ith the class data
    '''
    combat_order[str(name)] = cc.Fighter(name,health,initiative,'N/A')
    '''
    #using it again for the print statement
    combatant = cc.Fighter(name,health,initiative,'N/A',0)
    fighters.append(combatant)
    print('\nCombatant data\n'+ str(combatant))

  fighters = sorted(fighters, key=cc.initiative_sort, reverse = True )

  print('\nThe fight order: ' )
  for item in fighters:
    print (item.name)
  print('')


  combat = 0
  play_count = 0
  while combat == 0:
    error_buff = 0
    while error_buff == 0:
      curr_fighter = fighters[play_count]
      #print (curr_fighter.name)
      #print(curr_fighter.health)
      ##############################################
      #add stuff for death saves here
     
      ##############################################
      print (str(curr_fighter.name) + ' is up')
      choice = int(input('Are they:\n1. Attacking\n2. Applying Healing\n3. Other Spellcasting/Pass Turn\n4. Oppurtunity Attack\n5. End Combat\n\nEnter the action: '))
      #fighter makes an attack
      if choice == 1:
        print(hhp.attack(fighters))

      #healing fighters
      elif choice == 2:
        print(hhp.heal(fighters))
      
      #cast spells/pass turn
      elif choice == 3:
        print(hhp.cast(fighters))
      
      #oppurtunity attack
      elif choice == 4:
        print('')
        for item in fighters:
          print (str(fighters.index(item)+1)+ '. ' + str(item.name))
        attacker = int(input('Who\'s making the attack: '))
        assailed = int(input('Who\'s being attacked: ')) 
        assailed = assailed-1
        dmgtaken = int(input('Damage dealt: '))
        fighters[assailed].health = fighters[assailed].health - dmgtaken
        print('')
        print (fighters[dmgtaker])
      
      #combat ends
      elif choice == 5:
        error_buff = 3
        combat = 2
        print('Combat Concluded\n\nPlayer Data: \n' + str(fighters))
        continue
      else:
        print('Sorry, that wasnt an option. Please try again')
        continue

      print('Is another action being made?')


      print ('\nNext Turn:')
      if play_count == (player_count-1):
        play_count = 0
        continue
      elif play_count != (player_count-1):
        play_count += 1
        continue
      continue

    
    

    

  