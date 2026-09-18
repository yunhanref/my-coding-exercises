import math

def bubble_sort_descending(arr):
    n = len(arr)
    # Dıştaki döngü tüm dizi elemanları boyunca ilerler
    for i in range(n):
        # İçteki döngü yan yana olan elemanları karşılaştırır
        for j in range(0, n - i - 1):
            # arr[j] artık ('isim', deger) şeklinde bir tuple.
            # Karşılaştırmayı tuple'ın 1. indeksindeki 'deger' üzerinden yapıyoruz.
            if arr[j][1] < arr[j + 1][1]:
                # Eğer sağdaki değer daha büyükse yer değiştir (Swap)
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

class PriorityQ:
    def __init__(self):
        self.queue = []
        self.first_index = 0
        
    def add(self, eklenecek_sozluk):
        # Sözlüğün (dictionary) içindeki anahtar(isim) ve değer(puan) çiftlerini dolaş
        for isim, puan in eklenecek_sozluk.items():
            print(f"adding {isim}:{puan} to the queue.")
            # Kuyruğa bir "tuple" olarak ekliyoruz: ('eren', 10) gibi
            self.queue.append((isim, puan))
            
    def proceed(self):
        # 1. ADIM: İşleme başlamadan önce kuyruğu puana göre sırala (En yüksek puan başa)
        print("\n--- Sorting the queue from highest to lowest value ---")
        self.queue = bubble_sort_descending(self.queue)
        
        # 2. ADIM: Sıralanmış kuyruğu baştan başlayarak boşalt
        print("the queue proceeds. Highest Priority First. pop(0)")
        while len(self.queue) > 0:
            # 0. indeksteki (en yüksek puanlı) elemanı listeden çıkar
            cikan_kisi = self.queue.pop(self.first_index)
            # cikan_kisi[0] -> isim, cikan_kisi[1] -> puan
            print(f"deleting {cikan_kisi[0]} (Priority: {cikan_kisi[1]})")
            
        print("queue empty\n")
        
    def show(self):
        print(f"queue: {self.queue}")

# KULLANIM KISMI
my_dict = {"eren": 10, "nazli": 999, "irem": 9}
myqueue = PriorityQ()

# Elemanları ekle
myqueue.add(my_dict)

print("\n--- Before Proceed ---")
myqueue.show()

# Kuyruğu sırala ve işle (Boşalt)
myqueue.proceed()

print("--- After Proceed ---")
myqueue.show()
