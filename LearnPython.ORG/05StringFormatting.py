# Output : Hello, Miftah
name = "Miftah"
print("Hello, %s" %name)

# Output : Ikki, 17 Tahun
name = "Ikki"
years = 17
print("Namanya, %s dan Umurnya %d" %(name, years))

# List String Formatting
# multiList = ["Miftah", 18, 168.1] ???
mylist = [1, 2, 3]
print("List: %s" %mylist)

# Fix Problem
data = ("Miftah", 18, 167.1, 5.00000012)
val = "Nama %s, Umur %d, Tinggi %f, Saldo IDR.%.6f"
print(val %data)

'''
Information
%s - String
%d - Integer
%f - Floating
%.(Angka)f - Bilangan Floating dengan jumlah Digit tetap disebelah kanan titik desimal
%x/%X - Integer yang direpresentasikan dalam hexadescimal(lowercase/uppercase)
'''

# --- %. Float ---------
pi = 3.14159
print("Nilai Lingkaran : %.2f" %pi)
# Output : 3.14

berat = 65.5
print("Berat badan: %f kg" % berat)
# Output: Berat badan: 65.500000 kg

# Mengatur agar hanya ada 1 angka di belakang koma (dibulatkan)
print("Berat badan: %.1f kg" % berat)
# Output: Berat badan: 65.5 kg

# Mengatur agar ada 3 angka di belakang koma
print("Berat badan: %.3f kg" % berat)
# Output: Berat badan: 65.500 kg
# -----------------------------

# --- Hex Formatting ---
angka = 255
# Huruf kecil
print("Nilai hex (kecil): %x" % angka)  
# Output: ff

# Huruf besar
print("Nilai hex (besar): %X" % angka)  
# Output: FF

angka = 15

# Mengatur lebar karakter menjadi 4 (spasi di depan)
print("Padded hex: %4x" % angka)  
# Output:    f

# Menambahkan angka 0 di depan untuk memenuhi lebar karakter
print("Zero-padded hex: %04x" % angka)  
# Output: 000f

# ----------------------
