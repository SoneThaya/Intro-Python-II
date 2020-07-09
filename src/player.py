# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
  
  def __init__(self, location, player_name):
    self.location = location
    self.player_name = player_name
    
  # def move_direction(player, direction):
  #   attribute = direction + '_to'
    
  #   if hasattr(self.location, attribute):
  #       self.location = getattr(self.location, attribute)
  #   else:
  #       print("Can not move in that direction!")
    
    
  