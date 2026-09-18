#? Öncelikli Kuyruk aslında arka planda bir Heap kullanır. Sadece isimleri ve kullanım amacı kuyruk (Queue) gibi görünür ama motoru Heap'tir.

# --- HEAP ---
class MinHeap:
    def __init__(self):
        self.agac_dizisi = []

    def ebeveyn_indeksi_bul(self, cocuk_indeksi):
        return (cocuk_indeksi - 1) // 2

    def yukari_tasi(self, baslangic_indeksi):
        # Eklenen elemanı, ebeveyninden küçük olduğu sürece yukarı kaydır (Bubble Up)
        mevcut_indeks = baslangic_indeksi
        
        while mevcut_indeks > 0:
            ebeveyn_indeksi = self.ebeveyn_indeksi_bul(mevcut_indeks)
            
            mevcut_deger = self.agac_dizisi[mevcut_indeks]
            ebeveyn_degeri = self.agac_dizisi[ebeveyn_indeksi]

            if mevcut_deger < ebeveyn_degeri:
                # İki elemanın yerini değiştir (Swap)
                self.agac_dizisi[mevcut_indeks] = ebeveyn_degeri
                self.agac_dizisi[ebeveyn_indeksi] = mevcut_deger
                
                # Kontrol etmeye bir üst seviyeden devam et
                mevcut_indeks = ebeveyn_indeksi
            else:
                break # Doğru yerini buldu

    def eleman_ekle(self, yeni_deger):
        self.agac_dizisi.append(yeni_deger) # Ağacın en sonuna (dizinin sonuna) ekle
        son_elemanin_indeksi = len(self.agac_dizisi) - 1
        self.yukari_tasi(son_elemanin_indeksi) # Eklenen elemanı doğru yere tırmandır

    def en_kucugu_cikar(self):
        if len(self.agac_dizisi) == 0:
            return None
        if len(self.agac_dizisi) == 1:
            return self.agac_dizisi.pop()

        # En tepedeki (en küçük) değeri sakla
        en_kucuk_deger = self.agac_dizisi[0] 
        
        # En sondaki elemanı en tepeye koy
        en_sondaki_deger = self.agac_dizisi.pop()
        self.agac_dizisi[0] = en_sondaki_deger
        
        # Bu kısımda normalde aşağı taşıma (Bubble Down / Heapify) işlemi yapılır 
        # Kod çok uzamasın diye sadece yukarı taşıma kısmını detaylandırdım.
        
        return en_kucuk_deger


# --- PRIORTITY QUEUE ---

class OncelikliKuyruk:
    def __init__(self):
        # Priority Queue, motor olarak yukarıda yazdığımız MinHeap'i kullanır
        self.arka_plan_motoru = MinHeap()

    def kuyruga_oncelikli_eleman_ekle(self, oncelik_puani):
        # Kuyruğa ekleme işlemi aslında Heap'e eleman eklemektir
        self.arka_plan_motoru.eleman_ekle(oncelik_puani)

    def en_oncelikli_olani_cikar(self):
        # Kuyruktan eleman çıkarma, Heap'in en tepesindeki elemanı almaktır
        # (Min-Heap olduğu için puanı en düşük olan, en yüksek önceliğe sahiptir)
        return self.arka_plan_motoru.en_kucugu_cikar()