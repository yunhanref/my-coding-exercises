# SIMMPLER AND BETTER QUEUE UPDATE
# Update: Added utility method that constantly asks the operations user may want to do instead of typing everythin statically in the source code.
#! queue
class Queue():
    def __init__(self):
        self.queue = []
        self.first = 0 #! to avoid magic numbers inside code. Reading ease
    def add_list(self,liste:list):
        for i in liste:
            print(f"adding element '{i}' of '{liste}' to the queue.")
            self.queue.append(i)
    def add_one(self,sayi:int):
        print(f"adding {sayi} to the queue")
        self.queue.append(sayi)
    def display(self):
        print(self.queue)
    def input_delete(self):
        while True:
            print(f"current: {self.queue}")
            tip = input("delete all or one (all: a / one: o / quit deletion: q):        ").lower()
            if tip == "a":
                while len(self.queue) > 0:
                    for i in range(len(self.queue)):
                        print(f"deleting element '{self.queue[self.first]}'")
                        self.queue.pop(self.first)
                print("queue emptied")
                break
            elif tip == "o":
                one_input = input(f"delete first element {self.queue[self.first]}? y(es)/q(uit):  ")
                if one_input == "y" and self.queue:
                    print(f"deleting element '{self.queue[self.first]}'")
                    self.queue.pop(self.first)
                    continue
                elif one_input == "q" and self.queue:
                    break
                else:
                    print("unknown input try agin:  ")
                    continue
            elif tip == "q":
                print("quitting")
                break
            else:
                print("unknown input try again")
                continue
    def display(self):
        print(self.queue)
    def utility(self):
        while True:
            utilin = input("which operation do you want? addone:ao, addlist:al, deletion_operations:d, quit:q, display:disp     ").lower()
            if utilin == "ao":
                aoin = int(input("type an input to add:  "))
                self.add_one(aoin)
                continue
            elif utilin == "al":
                alin = input("Sayıları aralarına boşluk bırakarak girin: ")
                liste = [int(x) for x in alin.split()]
                self.add_list(liste)
                continue
            elif utilin == "d":
                self.input_delete()
                continue
            elif utilin == "q":
                print("quitting")
                break
            elif utilin == "disp":
                print(f"current {self.queue}")
                continue
            else:
                print("unknown try again.")
                continue

my_queue = Queue()
my_queue.utility()


'''
# İlk giren ilk çıkar (FIFO) mantığıyla çalışır. Market sırası gibi düşünebilirsiniz.

class Kuyruk:
    def __init__(self):
        self.bekleme_sirasi = []
    def toplu_kuyruga_gir(self, toplu=list):
        for siradaki in toplu:
            print(f"--adding {siradaki} to the queue--")
            self.bekleme_sirasi.append(siradaki)
        print("END")

    def bireysel_kuyruga_gir(self, bireysel=str):
        print(f"--adding {bireysel} to the queue--")
        self.bekleme_sirasi.append(bireysel) # Sıranın en sonuna geç
        print("END")
    def sirayi_bir_ilerlet(self):
        if len(self.bekleme_sirasi) > 0:
            # 0. indeks her zaman sıranın en başındaki kişidir
            print(f"{self.bekleme_sirasi[0]} kuyruktan cikti")
            return self.bekleme_sirasi.pop(0) 
        else:
            return "Kuyrukta kimse yok!"
    def sirayi_tamamen_ilerlet(self):
        # Bekleme sırasında eleman olduğu sürece döngüye devam et
        while len(self.bekleme_sirasi) > 0:
            cikan_kisi = self.bekleme_sirasi.pop(0)
            print(f"{cikan_kisi} kuyruktan cikti")

    def kuyruk_goster(self):
        if self.bekleme_sirasi == []:
            print("No value in queue")
        else:
            print(self.bekleme_sirasi)


kuyruk = Kuyruk()
kuyruk.toplu_kuyruga_gir(["eren","nazli","irem","nurgul","akif"])
kuyruk.bireysel_kuyruga_gir("stranger")
kuyruk.sirayi_bir_ilerlet()
kuyruk.kuyruk_goster()
kuyruk.sirayi_tamamen_ilerlet()
kuyruk.kuyruk_goster()

WITHOUT CODE IMPLEMENTATION
people = ["eren","nazli","irem","nurgul","akif"]
for comesin in people:
    print(f"adding {comesin} to the queue...")
    kuyruk.kuyruga_gir(comesin)
kuyruk.kuyruk_goster()

LONG WAY
kuyruk.siraya_gir("eren")
kuyruk.siraya_gir("nazli")
kuyruk.siraya_gir("irem")
kuyruk.siraya_gir("nurgul")
kuyruk.siraya_gir("akif")

kuyruk.sira_goster()
kuyruk.siradan_cik()
kuyruk.siradan_cik()
kuyruk.siradan_cik()
kuyruk.siradan_cik()
kuyruk.siradan_cik()
'''



