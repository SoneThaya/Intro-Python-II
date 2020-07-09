# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
  def __init__(self, name, description, item=[]):
    self.name = name
    self.description = description
    self.item = item
    
  def __str__(self):
    return f"{self.name}: {self.description} \n items: {self.room_item()}"
  
  def room_item(self):
    for i in self.item:
      print(f"{i.item_name}: {i.item_description}")
    
  def add_to_inventory(self, item):
    self.item.append(item)
    
  def drop_from_inventory(self, item):
    self.item.remove(item)