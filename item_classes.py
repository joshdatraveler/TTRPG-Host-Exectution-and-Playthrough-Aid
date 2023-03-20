#####################################################
class Sword:
  def __init__(self,sword_type,dmg_type,hit_bonus,special_attack):
    self.__sword_type = sword_type
    self.__dmg_type = dmg_type
    self.__hit_bonus = hit_bonus
    self.__special_attack = special_attack

  def set_sword_type(self,sword_type):
    self.__sword_type = sword_type
  def set_dmg_type(self,dmg_type):
    self._sword_type = dmg_type
  def set_hit_bonus(self,hit_bonus):
    self.__hit_bonus = hit_bonus
  def set_special_attack(self,special_attack):
    self.__special_attack = special_attack
  
  def get_sword_type(self):
    return self.__sword_type
  def get_dmg_type(self):
    return self.__dmg_type
  def get_hit_bonus(self):
    return self.__hit_bonus
  def get_special_attack(self):
    return self.__special_attack

  def __str__(self):
    return('Sword Type: '+str(self.get_sword_type())+'\nHit Bonus: '+str(self.get_hit_bonus())+\
    '\nDamage: '+ str(self.get_dmg_type())+
    '\n'+str(self.get_special_attack()))
################################################################################################################  
class Great_Weapons:
  def __init__(self,gw_type,gw_dmg_type,gw_hit_bonus,gw_special_attack):
    self.__gw_type = gw_type
    self.__gw_dmg_type = gw_dmg_type
    self.__gw_hit_bonus = gw_hit_bonus
    self.__gw_special_attack = gw_special_attack

  def set_gw_type(self,gw_type):
    self.__gw_type = gw_type
  def set_gw_dmg_type(self,gw_dmg_type):
    self._gw_sword_type = gw_dmg_type
  def set_gw_hit_bonus(self,gw_hit_bonus):
    self.__gw_hit_bonus = gw_hit_bonus
  def set_gw_special_attack(self,gw_special_attack):
    self.__gw_special_attack = gw_special_attack
  
  def get_gw_type(self):
    return self.__gw_type
  def get_gw_dmg_type(self):
    return self.__gw_dmg_type
  def get_gw_hit_bonus(self):
    return self.__gw_hit_bonus
  def get_gw_special_attack(self):
    return self.__gw_special_attack

  def __str__(self):
    return('Great Weapon Type: '+str(self.get_gw_type())+'\nHit Bonus: '+str(self.get_gw_hit_bonus())+\
    '\nDamage: '+ str(self.get_gw_dmg_type())+
    '\n'+str(self.get_gw_special_attack()))

################################################################################################################
class Assorted_Items:
  def __init__(self,item_details,special_mods):
    self.__item_details = item_details
    self.__special_mods = special_mods

  def set_item_details(self,item_details):
    self.__item_details = item_details
  def set_special_mods(self,special_mods):
    self.__special_mods = special_mods

  def get_item_details(self):
    return self.__item_details
  def get_special_mods(self):
    return self.__special_mods

  def __str__(self):
    return('Item: '+ str(self.get_item_details()) + '\nAbnormalities: '+ str(self.get_special_mods()))
################################################################################################################
class Shields:
  def __init__(self,ac_buff,strength_req,sh_special):
    self.__ac_buff = ac_buff
    self.__strength_req = strength_req
    self.__sh_special = sh_special

  def set_ac_buff(self,ac_buff):
    self.__ac_buff = ac_buff
  def set_strenth_req(self,strength_req):
    self.__strength_req = strength_req
  def set_sh_special(self,sh_special):
    self.__sh_special = sh_special

  def get_ac_buff(self):
    return self.__ac_buff
  def get_strength_req(self):
    return self.__strength_req
  def get_sh_special(self):
    return self.__sh_special

  def __str__(self):
    return('Sheild Stats\n'+'AC Boost: '+str(self.get_ac_buff())+'\nStrength Requirement: '+str(self.get_strength_req())+ '\n'+str(self.get_sh_special()))


################################################################################################################
class Ranged:
  def __init__(self):
    pass


################################################################################################################

class Polearms:
  def __init__(self):
    pass

class Trident(Polearms):
  def __init__(self):
    pass

