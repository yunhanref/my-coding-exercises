#Gerçek bir dizi bellekte sabit boyutludur. Bu yüzden başlangıçta belirli bir kapasite ile oluşturup, içini boş (None) bırakarak doldurma mantığıyla yazdım.

#? Arrayler nedir? 
#? Desc: Arrayler sirali ve genellikle sabit boyutlu lineer dizilerdir.

#* Advantage: Degerler "index" adi verilen 0dan n elemana kadar ilerleyen adreslerde tutulur. Arama karmasikligi O(1)'dir.
#! Disadvantage: Ekleme ve silme islemleri tum indexlerin yeniden shiftlenmsine sebep olacagindan karmasikligi O(n)'dir.

class FixedSizeArray():
    def __init__(self, capacity):
        self.capacity = capacity
        self.current_values = 0
        self.current_array = [None] * capacity
    def add(self, userinput):
        if self.current_values < self.capacity:
            print("add")
            index = self.current_values
            self.current_array[index] = userinput
            self.current_values += 1
        else:
            print("already reached capacity")
    def show(self):
        print("printing the array")
        print(self.current_array)

    def show_index_value(self,showindex):
        print(f"value at index {showindex} is {self.current_array[showindex]}")

    def delete(self, index_to_delete):
        #Once silinmek istenen indexin varligi kontrol edilecek
        self.current_array.pop(index_to_delete)

array = FixedSizeArray(10)
array.add(1)
array.add(2)
array.add(3)
array.delete(1) # must pop value 2
array.show()
array.show_index_value(1)