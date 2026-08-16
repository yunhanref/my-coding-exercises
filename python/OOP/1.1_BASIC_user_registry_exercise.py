#we will make an user registry class. If the user is not over 18, things will happen
import time
def dots():
  time.sleep(1)
  print(".")
  time.sleep(1)
  print("..")
  time.sleep(1)
  print("...")
class registry:
  def __init__(self,name,age):
    self.n = name
    self.a = age

  def greeter_age_checker(self):
    print(f"Hello {self.n}, after the age registration, you will be directed to the main page!")
    dots()
    if self.a < 18:
      print("no!")
    else:
      print("welcome in!")
  def get_info(self): #get_info = method
    print(f"name:{self.n},age:{self.a}")

eren = registry("eren",19)
eren.greeter_age_checker()
nazli = registry("nazli",17)
nazli.greeter_age_checker()
eren.get_info()