class FactoryStaff:
  def __init__(self,name: str,age: int,shift: str):
    self.name = name
    self.age = age
    self.shift = shift
  def get_shift(self): 
    print(f"{self.name} has shift in {self.shift}")
  def get_staff_info(self): 
    print(self.name,self.age,self.shift)
class Ceo(FactoryStaff):
  def ceo_role(self):
    print("factory is managed succesfully!")
class Worker(FactoryStaff):
  def worker_role(self,boxcount):
    print(f"{self.name} had opened {boxcount} boxes today.")
class Chief(FactoryStaff):
  def chief_role(self):
    print(f"{self.name} have helped the work.")

mudur = Ceo("savas",39,"morning")
mudur.get_staff_info()
mudur.ceo_role()
eren = Worker("eren",19,"all day")
eren.get_staff_info()
eren.worker_role(100)
asiye = Chief("asiye",20,"morning")
asiye.get_staff_info()
asiye.chief_role()
