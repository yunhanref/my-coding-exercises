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

''' WITHOUT CODE IMPLEMENTATION
people = ["eren","nazli","irem","nurgul","akif"]
for comesin in people:
    print(f"adding {comesin} to the queue...")
    kuyruk.kuyruga_gir(comesin)
kuyruk.kuyruk_goster()
'''

''' LONG WAY
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



