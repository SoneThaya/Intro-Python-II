class Item:
  def __init__(self, item_name, item_description):
    self.item_name = item_name
    self.item_description = item_description
    
  def __str__(self):
    print(f"{self.item_name}: {self.item_description}")
  
  def print_name(self):
    print(f"{self.item_name}: {self.item_descrption}")

  