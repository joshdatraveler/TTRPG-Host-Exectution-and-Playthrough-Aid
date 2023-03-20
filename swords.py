#Sword Attributes

sword_types = ['Short Sword \nReach: 5ft','Katana \nReach: 7ft','Rapier \nReach: 5ft','Scimitar \nRange: 5ft']

sword_damage = ['1d10','2d6','3d4','2d4','1d4+4','1d6+2','1d8','2d4+1','1d20','1d4+4','1d6+3','2d4+3','2d4+3','1d6+1','2d4+3','2d4+3','1d4+7','1d6+3','1d4+7','1d6+3','1d10','2d6','3d4+1','1d10','2d6','3d4+1','1']

sword_hit = ['+6','+5','+6','+5','+6','+5','+6','+5','+8','+9','+6','+7','+5','+6','+7','+5','+6','+7','+5','+9','+1']

shadow_strike = str('\nShadow Strike: \nUser sacrifices a portion of their \nlife force for access to the sprirt plane.'+
'\n- Give up 5 HP in retrun 1d2 turns of uninterrupted invisibility')
viper_tip = str('\nViper Tip: \nThe tip of the sword has a mechanism \nthat releases a deadly venom when a target is cut with it'+
'\n- On a succesful attack the target takes 1d6 poison damage every turn for the next 5 turns')
flash_point= str('\nFlash Point: \nThis sword emits a bright disorienting flash \nwhen it connects with its target'+
'\n- When a strike lands, everyone within a 5ft radius of \nthe strike is blinded for that round of combat.')
ivory_hilt=str('\nIvory Hilt: \nYou are granted unnatural sight via the mystical eye \nembedded in the hilt of your sword.'+
'\n- You gain the ability to make a counter \nattack to any attack made on you at no cost \n(You roll with disadvantage if the attack made on you \nconnects or if the attack was made from behind)')
thirsty_boi = str('\nHungry Hungry Hilt: \nThis sword was taken over long ago by an\ninterdimensional being that feeds on the life force those \nit comes in contact with'+
'\n- This sword deals 1d10 nacrotic damage to its on a hit, \nhowever if 4 turns of combat pass and it hasn\'t connected \nwith anything, it will do 1d10+2 nacrotic damage to the \nwielder \n(Only occurs during combat and is limited to \nhand-to-hand/close quarters combat encounters)')
stored_energy = str('\nEnergy Reserves: \nThis sword stores kinetic energy that can be used to boost the weilders performance\n'+'- Succesful hits store 1d6 points of energy in the hilt of the sword. \n- This energy can be used to heal (cost an action) or can be added to the following swings hit bonus')

sword_special = [shadow_strike,viper_tip,flash_point,ivory_hilt,thirsty_boi,stored_energy]
 #'\nSpecial Attack: N/A','\nSpecial Attack: N/A',ivory_hilt,thirsty_boi,stored_energy]
#sword_special = [stored_energy]
#print (special_attack[0])

########################################################

