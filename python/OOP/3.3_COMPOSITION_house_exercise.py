#composition: owns-a relationship.
class Room:
  def __init__(self,name,sqm):
    self.name = name
    self.sqm = sqm
class House:
  def __init__(self,address):
    self.address = address
    #create individual Room instances inside House, so it becomes connected.
    self.rooms = [
            Room("Salon", 35),
            Room("Yatak Odası", 20),
            Room("Mutfak", 15)
        ]
  def yazdir(self):
    for r in self.rooms:
      print(f"name: {r.name},sqm: {r.sqm}")
ev = House("erenin evi")
ev.yazdir()