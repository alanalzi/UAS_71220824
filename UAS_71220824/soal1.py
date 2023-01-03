print ("*"*6, "Kredit Keaktifan Mahasiswa", "*"*6)
print ("(Student Activities Credit)")
print ("1. Menambahkan Kegiatan")
print ("2. Menampilkan Jumlah Poin")
print ("3. Keluar ")
print ("-"*28)
p = int(input("Silahkan Masukan Pilihan Anda: "))
while True :
    if p == "1":
        k = input("Nama Kegiatan")
        kk = input("Tanggal Kegiatan")  
        print("Pilihan Kategori Kegiatan: ")
        print("- Prestasi")
        print("- Organisasi")
        print("- Kepanitiaan")
        print("- Rekognisi")
        kkk = input("Masukan Kategori Kegiatan: ")
        print("")
        x = print("Kegiatan Berhasil Ditambahkan.")
        if kkk == ("Organisasi", "oRgAnIsAsI"):
            print("Kegiatan Berhasil Ditambahkan.")
           
        elif kkk == ("Kepanitiaan","kepanitiaan"):
            print("Kegiatan Berhasil Ditambahkan.")
        
        elif kkk == ("Prestasi","PRESTASI"):
            print("Kegiatan Berhasil Ditambahkan")
        
        elif kkk == ("Rekognisi","rekognisi"):
            print("Kegiatan Berhasil Ditambahkan.")