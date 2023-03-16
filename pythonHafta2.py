#dizi oluşturuldu
ogrenciler = ["Sema Nur Şakar","Ali Ulu","Ahmet Türk"]
#işlem menüsü yazdırıldı
print('''      
                     ***Işlem Menüsü***
      //Listeye Bir Ogrenci Eklemek Icin             --> 1
      //Listeye Birden Fazla Ogrenci Eklemek Icin    --> 2
      //Listeden Bir Ogrenci Kaldirmak Icin          --> 3
      //Listeden Birden Fazla Ogrenci Kaldirmak Icin --> 4
      //Listeyi Ekrana Yazdirmak Icin                --> 5
      //Ogrenci Numarasi Ogrenmek Icin               --> 6
         ''')

secim = int(input("Yapmak Istediginiz Islem Numarasini Tuslayiniz : "))
if secim == 1:
    ogrenciBilgi = input("Listeye Eklemek Istediginiz Ogrenci Adi Ve Soyadi :")
    ogrenciler.append(ogrenciBilgi)
elif secim == 2:
    yeniOgrenciSayisi = int(input("Kaç Ogrenci Eklemek Istersiniz? "))
    for i in range(yeniOgrenciSayisi):
         ogrenciBilgi = input("Listeye Eklemek Istediginiz Ogrenci Adi Ve Soyadi :")
         ogrenciler.append(ogrenciBilgi)
         i += 1
elif secim == 3:
     print(ogrenciler)
     ogrenciBilgi = input("Listeden Kaldirmak Istediginiz Ogrenci Adi Ve Soyadi :")
     ogrenciler.remove(ogrenciBilgi)   
elif secim == 4:
    yeniOgrenciSayisi = input("Kaç Ogrenci Silmek Istersiniz? ")
    for i in range(yeniOgrenciSayisi):
         ogrenciBilgi = input("Listeden Silmek Istediginiz Ogrenci Adi Ve Soyadi :")
         ogrenciler.remove(ogrenciBilgi)
         i += 1           
elif secim == 5:
     print(ogrenciler)
elif secim == 6:
     i = 0
     while i < len(ogrenciler):
      print(f'{i} Numaralı Ogrenci : {ogrenciler[i]}')  
      i += 1 
else :
     print("Hatali Tuslama Yaptiniz")


