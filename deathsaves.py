def death_saves(fighters):
  if curr_fighter.health < 0:
    if curr_fighter.fail_saves == 3:
      play_count += 1
      if play_count == (player_count-1):
        play_count = 0
        continue
    print ('Make a Death saving throw')
    sucfail = input('Did it Succeed (S) or Fail (F): ')
    sucfail.capitalize()
    death_buffer = False
    while death_buffer == False:
      if sucfail == 'S' or sucfail == 'Success' or sucfail == 'Succeed':
        curr_fighter.suc_save += 1
      elif sucfail =='F' or sucfail == 'Fail' or sucfail == 'Failure':
        curr_figher.fail_save +=1
      
      if curr_fighter.fail_save ==3:
        print(str(curr_fighter.name) + ' has died')
        play_count += 1
        if play_count == (player_count-1):
          play_count = 0
          death_buffer = True
          continue