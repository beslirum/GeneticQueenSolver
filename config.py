# config.py

#This file contains configuration values for the project.
#Bu dosya, projenin yapılandırma değerlerini içerir.

population_size = 100   #Popülasyon boyutu
board_size = 8          #Satranç tahta boyutu ve N Vezirdeki Vezir sayısı
#Bu değeri 1000 yaptığımda bilgisayarım kaldıramadı.
generations = 1000      # Genetik algoritmadaki jenerasyon (iterasyon) sayısı.
num_parents = 50        # Genetik algoritmanın çaprazlama işlemi için seçilen ebeveyn sayısı.
num_offsprings = 50     # Genetik algoritmanın her jenerasyonunda oluşturulan yavru sayısı.
mutation_rate = 0.1     # Mutasyon oranı, bir bireydeki her gen için mutasyon olasılığını temsil eder.


#Değerler hakkında notlarım:
'''
population_size: Popülasyon boyutu, genetik algoritmanın bir jenerasyonunda bulunan bireylerin toplam sayısını belirtir. 
Bu değer ne kadar büyükse, genetik algoritmanın çözümü arama uzayında daha fazla birey arasında gezinir, ancak hesaplama maliyeti de artar.

board_size: Satranç tahtasının boyutu ve dolayısıyla N Vezir problemi için vezir sayısını belirtir. 
Bu değer, genetik algoritmanın çözümünün arandığı tahtanın büyüklüğünü belirler.

generations: Genetik algoritmadaki jenerasyon (iterasyon) sayısını belirtir. 
Her bir jenerasyon, popülasyonun evrimleşmesini temsil eder. 
Daha fazla jenerasyon genellikle daha iyi sonuçlar elde etmenize yardımcı olabilir, ancak hesaplama maliyetini artırabilir.

num_parents: Her çaprazlama işlemi için seçilen ebeveyn sayısını belirtir. 
Çaprazlama, popülasyon içindeki bireyler arasında genetik materyalin değişimini sağlar. 
Bu sayı ne kadar büyükse, genetik çeşitlilik artar.

num_offsprings: Her jenerasyonda oluşturulan yavru sayısını belirtir. 
Yavrular, çaprazlama ve mutasyon işlemleri sonucunda elde edilen yeni bireylerdir.

mutation_rate: Mutasyon oranı, bir bireyin genlerinde herhangi bir değişiklik olasılığını belirtir. 
Mutasyon, genetik çeşitliliği artırmak ve potansiyel olarak daha iyi çözümleri keşfetmek için kullanılır.

'''
