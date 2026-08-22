#abstract method
from abc import ABC, abstractmethod
#used when you want all the inheritants to have same spesific methods (function doesnt matter the function name be the same) whithout exception. Unless, the code doesnt run.
class Human(ABC):
  @abstractmethod
  def eat(self):
    print("humans eat.")
  @abstractmethod
  def sleep(self):
    print("humans sleep.")

class fem(Human):
  def eat(self):
    print("humans eat.")
  def sleep(self):
    print("humans sleep.")
  def femme(self):
    print("half of the humans are female")
female = fem()
female.femme() #this class will work fine without errors because it has the neccesary methods.

class masc(Human):
  def mascule(self):
    print("half of the humans are male")
male = masc()
male.mascule() #Will throw an error saying: "Can't instantiate abstract class masc without an implementation for abstract methods 'eat', 'sleep'"
# because we didnt include the abstract methods of the inherited class.
