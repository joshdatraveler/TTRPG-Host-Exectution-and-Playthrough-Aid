import item_classes as ic
import swords as sw
import great_weapons as gw
import assorted_items as ai
import polearms as st
import shields as sh
import Ranged as ra
import resetcharge as rc
import mainmenu as me
import battlelogfunction as blf
import character_stat_gen as csg
import random
import sys
import time


def main():
  print (me.menu())


def randomitemgen():
  resetcharge = 0
  print ('Welcome to the random item generator. Listed below \nare the types of items that you can generate: \n1. Swords (75GP) \n2. Great Weapons (85GP)\n3. Shields (80GP) \n4. Polearms (70GP) \n5. Ranged Weapons (70GP)\n6. Assorted Items(30GP)')
  while resetcharge == 0:
    with open('Output.txt', 'w') as f:
      print(pick_item(), file=f)

    time.sleep(2)
    print('Would you like to make another item? ')
    do_over = str(input('Please enter Yes or No: '))
    do_over = do_over.capitalize()
    if do_over == 'Yes':
      resetcharge = 0
    else:
      resetcharge = 1
      return ('Thank you for using the DND Random Item Generator')
    



def pick_item():
  selection = int(input('\nWhich type of item would you like to create: '))

  if selection == 1:
    type = random.choice(sw.sword_types)
    damage = random.choice(sw.sword_damage)
    hit = random.choice(sw.sword_hit)
    special = random.choice(sw.sword_special)
    weapon = ic.Sword(type,damage,hit,special)
    print('Your item is ready in the output text!')
    return (weapon)
    #print(rc.do_it_again())
    
  elif selection == 2:
    type = random.choice(gw.gw_types)
    hit = random.choice(gw.gw_hit)
    damage = random.choice(gw.gw_dmg)
    special = random.choice(gw.gw_special)
    weapon = ic.Great_Weapons(type,damage,hit,special)
    print('Your item is ready in the output text!')
    return (weapon)
    #print(rc.do_it_again())
  elif selection == 3:
    shield_ac_buff = random.choice(sh.sh_ac_buff)
    str_req = random.choice(sh.sh_str_req)
    special = random.choice(sh.sh_spec_ab)
    shield = ic.Shields(shield_ac_buff,str_req,special)
    print('Your item is ready in the output text!')
    return(shield)
      #print(rc.do_it_again())
  elif selection == 4:
    print('Sorry, we don\'t have that right now ')
      #print(rc.do_it_again())
  elif selection ==5:
    print('Sorry, we don\'t have that right now ')
      #print(rc.do_it_again())
  elif selection == 6:
    item_type = random.choice(ai.item_desc)
    abnor = random.choice(ai.abnormalities)
    item = ic.Assorted_Items(item_type,abnor)
    print('Your item is ready in the output text!')
    return(item)
  else:
    print('Yeah we straight dont got that shit yo, \nidk what to tell you')
    
    
   # resetcharge = 0
    #print('Would you like to make another item? ')
   # do_over = str(input('Please enter Yes or No: '))
   # do_over = do_over.capitalize()
    #if do_over == 'Yes':
    #  resetcharge = 0
   # else:
   #   resetcharge = 1

  

if __name__ == '__main__':
  main()



#print (pick_item())
#print (rf.shadow_strike)

#slasher = ic.Sword('Short sword','1d10 Fire dmg','+7','N/A')
#print (slasher)DA