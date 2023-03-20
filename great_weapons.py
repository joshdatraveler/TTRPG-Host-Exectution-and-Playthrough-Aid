gw_types = ['Great Axe\nReach: 5ft','Great Club\nReach: 6ft','Great Sword\nReach: 5ft','Great Hammer\nReach: 6ft']

gw_hit = ['+5','+6','+5','+6','+5','+6','+5','+6','+7','+4','+5','+6','+8','+7','+7','+4','+1','+8','+1']

gw_dmg = ['2d6+2','1d8+5','2d6+2','1d8+5','2d6+2','1d8+5','1d10+4','1d10+4','1d8+7','2d6','3d4+6','3d4+6','1d20','1','4d4+4','4d4+4','4d4+4','1d8+9','2d8+2']

concussive_force = str('\nConcussive Force: \nThis weapon uses experimental hydraulic technology to create explosive force from within the segmented body of the weapon'+
'\n- +4 Bludgeoning damage is dealt to a target \n- target is knocked back 1d20+10 ft \n- target is stunned for one round of combat \n- This effect has a recharge of 3 rounds  ')

repulsar_tech = str('\nLight Handed: \n A strange combination of moving metal and electricity makes the weapon exceptionally light, without sacrificing \ndamage output'+
'\n- +3 lightning damage \n- this weapon can be weilded with one handed at no cost\n- succesful strikes have a 50/50 chance of dealing 1d6 lightning damage to the target and wielder')

dark_art = str('\nDark Agreement: \n This weapon has the ability to grant extrodinary strength, but it comes at a cost.'+
'\n-The requirement for a critical hit is lowered to 15, however a critical failure is raised to 3 and will lead to the wielder losing half remaining HP, and falling unconcious for three turns of combat')

arcing_strike = str('\nArcing Strike: \n This weapon is built around a chain that the weilder can extend and restrict at will. This increases the range of attacks as well as the number of targets that can be hit one swing'+
'\n- While the chain is extended this weapons reach is doubled\n- Wide Swing - Attack three targets within range in one swing, dealing 1d6+5 to each target')

split_hilt = str('\nSplit Hilt: \nThis weapon is actually two smaller, lighter weapons that are held together by some foreign magic.'+
'\n- Each split weapon can be wielded with one hand and has a range of 30ft when thrown\n- A split weapon can be recalled as a free action \nas long as the wielder possesses the other split\n- Hit bonus of each split is 4+ wielders religion or arcana modifier. \n- Damage for each split is 1d10+3')

gw_special = ['Special Attack: N/A','Special Attack: N/A','Special Attack: N/A',split_hilt,arcing_strike,dark_art,repulsar_tech,concussive_force]