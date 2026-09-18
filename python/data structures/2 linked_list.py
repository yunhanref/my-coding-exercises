# Bağlı liste, verileri hafızada yan yana değil, birbirini işaret eden düğümler (Node) şeklinde tutar.
#? Whats a linked list?
#? Linked Lists solves the index shifting cost of arrays by storing the values with a pointer that points to the next value.
#* Advantage: Easy to add values in between.
#! Disadvantage: Hard to access specific values.

# Nodes = (data,pointer to next node)
# Linked List = (Nodes)

class Dugum:
    def __init__(self, eklenecek_veri):
        self.veri = eklenecek_veri
        self.sonraki_dugum = None

class BagliListe:
    def __init__(self):
        self.baslangic_dugumu = None

    def sona_veri_ekle(self, yeni_veri):
        yeni_olusturulan_dugum = Dugum(yeni_veri)

        if self.baslangic_dugumu is None:
            self.baslangic_dugumu = yeni_olusturulan_dugum
            return

        gezinilen_dugum = self.baslangic_dugumu
        # Sonraki düğümü boş olan (yani kuyruğun sonu) düğümü bulana kadar ilerle
        while gezinilen_dugum.sonraki_dugum is not None:
            gezinilen_dugum = gezinilen_dugum.sonraki_dugum
            
        gezinilen_dugum.sonraki_dugum = yeni_olusturulan_dugum

dugum1 = Dugum(10)
dugum2 = Dugum(11)
linkedlist = BagliListe()


#! Kendim priority queue olusturmak istersem. Heap kullanmak yerine tum listeyi arayacak, tekrar sortlayacak
#! 