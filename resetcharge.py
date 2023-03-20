def do_it_again():

  print('Would you like to make another item? ')
  do_over = str(input('Please enter Yes or No: '))
  do_over = do_over.capitalize()
  if do_over == 'Yes':
    return(resetcharge == 0)
  else:
    print ('Thank you for using the DND Random Item Generator')
    return (resetcharge == 1)
