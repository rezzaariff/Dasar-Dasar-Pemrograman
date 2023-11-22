#Nomer 1
#deklarasi
def say(nama,alamat,gender,umur,hoby):
    print("Nama saya adalah: ",nama)
    print("Saya tinggal di:",alamat)
    print("Gender saya",gender)
    print("Umur saya:",umur)
    print("Hoby saya:",hoby)

#panggil
say("Reja","Depok","Laki-Laki","18","Bermain Badminton")

#Nomer 2
#deklarasi
def kelulusan(nilai):
    if nilai < 60:
        return "Gagal"
    elif 61 <= nilai <= 70:
        return "Baik"
    elif 71 <= nilai <= 80:
        return "Sangat Baik"
    elif 81 <= nilai <= 100:
        return "Istimewa"
    else:
        return "Nilai tidak valid"
#panggil
hasil = kelulusan(100)
print("Hasil Kelulusan: ",hasil)

#Nomer 3
#deklarasi
def ganjil(batas):
    for i in range(1, batas + 1,2):
        print(i)
#panggilan
ganjil(10)