#used OOP methods: @abstractmethod, inheritance, polymorphism, super()
from abc import ABC, abstractmethod
import time

class Teotl(ABC):
    def __init__(self, name, gender):
        self.name = name or "not entered"
        self.gender = gender or "not entered"

    @abstractmethod
    def channeling(self):
        pass
    @abstractmethod
    def offering(self):
        pass
    @abstractmethod
    def god_of(self):
        pass
    @abstractmethod
    def abilities(self):
        pass

class Tezcatlipoca(Teotl):
    def __init__(self, name, gender, is_toxcatl):
        super().__init__(name, gender)
        self.is_toxcatl = is_toxcatl if is_toxcatl is not None else "unknown..."

    def toxcatl(self):
        if self.is_toxcatl == True:
            print("Toxcatl is about to end, your god wants offering.")
            offering_knowledge = False  

            read_scrolls = str(input("Do you wish to know what your god accepts as offering? yes/no ")).upper()

            if read_scrolls == "YES":
                print(f"When {self.name} read the scrolls, they learnt that your god Tezcatlipoca accepts blood and heart of a young and beautiful man in the month of 'Toxcatl'.")
                offering_knowledge = True 
            elif read_scrolls == "NO":
                print("You haven't read the scroll.")
            else:
                print("Unknown action.")

            if offering_knowledge == True:
                print("Your god is satisfied with the offering.")
            else:
                print("Because you don't know what your god accepts, you couldn't complete the rite. Tezcatlipoca is angry!")
        else:
            print("It's not Toxcatl yet.")

    
    def abilities(self):
        print(f"{self.name} channels Tezcatlipoca's powers...")
        time.sleep(1)
        print("Tezcatlipoca grants you: Shadow Mimicry and Illusion Creation.")
    def shadow_mimicry(self):
      print("Used Skill: Shadow Mimicry. You disappear into the shadows.")
    def illusion_creation(self):
      print("Used Skill: Illusion Creation. You created 10 shadow clones of yourself.")
    def god_of(self):
        print("Tezcatlipoca is the god of Night, Sorcery, and Fate.")
    def offering(self):
        print("Requires a ritualistic human sacrifice offering during the Toxcatl festival.")
    def channeling(self):
        print("pass")

class Quetzalcoatl(Teotl):
    def abilities(self):
        print(f"{self.name} channels Quetzalcoatl's powers...")
        time.sleep(1)
        print("Quetzalcoatl grants you: Serpent Spawner and Viper Toxcin")
    def serpent_spawner(self):
      print("Used Skill: Serpent Spawner. You disappear into the shadows.")
    def viper_toxcin(self):
      print("Used Skill: Viper Toxcin. You .")
    def god_of(self):
        print("Quetzalcoatl is the god of Knowledge, Creation, and Civilisation.")
    def offering(self):
        print("accepts offerings such as jade, flowers, butterflies, and copal incense.")
    def channeling(self):
        print("pass")

tezcatlipoca_cleric = Tezcatlipoca("Eren", "Male", True)
tezcatlipoca_cleric.channeling()
tezcatlipoca_cleric.toxcatl()
quetzalcoatl_cleric = Quetzalcoatl("Nazli","Female")
quetzalcoatl_cleric.serpent_spawner()
quetzalcoatl_cleric.viper_toxcin()
