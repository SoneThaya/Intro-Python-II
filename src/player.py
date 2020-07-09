# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
  
  def __init__(self, location, player_name, inventory=[]):
    self.location = location
    self.player_name = player_name
    self.inventory = inventory
    
  def __str__(self):
    return f"{self.player_name} items: {self.inventory}"
  
  def print_status(self):
    print(f"{self.player_name}")
    print("Inventory: ")
    for p in self.inventory:
      p.print_name()
    
  def add_to_inventory(self, item):
    self.inventory.append(item)
    
  def drop_from_inventory(self, item):
    self.inventory.remove(item)
    
  def print_inventory(self):
    for i in self.inventory:
      print(f"{i.item_name}: {i.item_description}")
    
  # def move_direction(player, direction):
  #   attribute = direction + '_to'
    
  #   if hasattr(self.location, attribute):
  #       self.location = getattr(self.location, attribute)
  #   else:
  #       print("Can not move in that direction!")
    
    
  