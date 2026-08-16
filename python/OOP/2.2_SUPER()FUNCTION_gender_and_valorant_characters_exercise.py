#super() function
#lets you add new attributes to spesific classes without overriding the inherited attributes by writing them all over again!!!!
#The example above this block is an excellent example to this, at the time i've finished the code above, i didnt know i could add new attributes to other classes...
#So instead of adding attributes that i wanted such as abilities, rank etc. i added ordinary print statements that had no functionability.

#REVAMP OF THE CODE ABOVE !!**

#INSAN - ERKEK/KADIN - KARAKTERLER, YETENEKLERI, ROLU, ALLIGNMENT

class Human:
  def __init__(self,name: str,age: int,ethnicity: str): #all humans have name ethnicity and age attributes (not methods! methods are functions itself!!)
    self.name = name
    self.age = age
    self.ethnicity = ethnicity
  def describe(self):
    print(f"name: {self.name},age:  {self.age},eth: {self.ethnicity}")
  def specie(self):
    print(f"{self.name} is human.")
  def sleep(self):
    print(f"{self.name} sleeps.")
  def eat(self):
    print(f"{self.name} eats.")
class Female(Human): #All females are human, therefore they inherit human attributes and methods(actions)!
  def vagina(self):
    print(f"{self.name} has vagina.")
  def ovulate(self):
    print(f"{self.name} ovulate.")
class Male(Human): #All males are human, therefore they inherit human attributes and methods(actions)!
  def penis(self):
    print(f"{self.name} has penis.")
  def erection(self):
    print(f"{self.name} has erection.")
class ValorantChar(Human):
    def __init__(self, name: str, age: int, ethnicity: str, superpower: str, role: str, alignment: str):
        super().__init__(name, age, ethnicity)
        self.superpower = superpower or "None"
        self.role = role
        self.alignment = alignment
    def describeValo(self):
      print(f"name: {self.name},\nage:  {self.age},\neth: {self.ethnicity},\nsuperpower: {self.superpower},\nrole: {self.role},\nallignment: {self.alignment}")
class FemValo(Female, ValorantChar):
    def __init__(self, name: str, age: int, ethnicity: str, superpower: str, role: str, alignment: str):
        # ValorantChar üzerinden tüm unisex nitelikler ve Human nitelikleri yüklenir
        ValorantChar.__init__(self, name, age, ethnicity, superpower, role, alignment)
class MascValo(Male, ValorantChar):
    def __init__(self, name: str, age: int, ethnicity: str, superpower: str, role: str, alignment: str):
        ValorantChar.__init__(self, name, age, ethnicity, superpower, role, alignment)
cypher = MascValo("cypher",39,"Morroco","","controller","good",)
cypher.describeValo()
cypher.penis()
print("\n")
jett = FemValo("jett",21,"South Korea","wind manipulation","duelist","good",)
jett.describeValo()
jett.vagina()