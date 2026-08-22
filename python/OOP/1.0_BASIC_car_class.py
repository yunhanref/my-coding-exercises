#make a car class that has brand, color and hp attributes.
class car:
  def __init__(self,brand,color,hp):
    self.brand = brand or "not spesified"
    self.color = color or "not spesified"
    self.hp = hp or "not spesified"
  def features(self):
    print(f"brand:  {self.brand}, color:  {self.color}, hp: {self.hp}")
  def move(self,distance):
    self.distance = distance or "didn't move"
    print(f"{self} moved {self.distance} kilometers.") #{self} = car() class.
    print(f"{self.brand} moved {self.distance} kilometers.")


araba1 = car("mercedes-benz","bright pink",180)
araba2 = car()
araba3 = car('','',200)
araba3.features()
araba2.features()
araba1.features()


#lets move them
lotus = car("lotus","black",500)
lotus.move(400)