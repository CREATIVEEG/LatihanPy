#Masukan nilai variabel
a = input("Masukan nilai a:")
b = input("Masukan nilai b:")

#Mencetak nilai variabel
print("Variabel A =",a)
print("Variabel B =",b)

#Mencetak hasil kedua variabel dengan string format
print("Hasil penggabungan {1}+{0}=".format(a,b) +str(a+b))

#Mengkonversi nilai variabel
a = int(a)
b = int(b)
print("Hasil penjumlahan {1}+{0}=%d".format(a,b) %(a+b))
print("Hasil pembagian {1}/{0}=%d".format(a,b) %(a/b))
