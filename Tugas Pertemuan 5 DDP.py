Kendaraan = ["NamaKendaraan", "JenisKendaraan", "CcKendaraan", "WarnaKendaraan", "RodaKendaraan"]
Kendaraan.append ("HargaKendaraan")
Kendaraan.append ("TipeKendaraan")
Kendaraan.insert (2, "MerkKendaraan")
print(Kendaraan)

menghitung = input ("""Anda ingin menghitung luas bangun datar apa?
                    ***PILIHAN OPERASI***
                    1.Hitung Persegi
                    2.Hitung Lingkaran
                    3.Hitung Segitiga""")
match menghitung:
  case "1":
    sisi= int(input("masukan nilai sisi:"))
    luas= sisi*sisi
    print (luas)
  case "2":
    jari_jari= int(input("masukan nilai jari jari:"))
    luas=3.14*jari_jari*jari_jari
    print (luas)
  case "3":
    alas= int(input("masukan nilai alas:"))
    tinggi= int(input("masukan nilai tinggi:"))
    luas=0.5*alas*tinggi
    print (luas)
  case _:
    print("Pilihan Tidak Tersedia")