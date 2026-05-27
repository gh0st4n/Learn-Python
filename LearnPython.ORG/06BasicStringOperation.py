# Menyelesaiakan masalah quote dalam quote
print("Test Qute ' '")
print('Test Qute " "')

astring = "Miftahul Jannah & Kue Pie!!!!"
print(len(astring))
# Output : 29, Sudah Terhitung dengan Spasi dan Tanda

print(astring.index("Pie"))
# Output :  22, pada karakter 22 ditemukan ad kalimat Pie

print(astring.count("n"))
# Output : 2, Karena karakter n hanya ada dua pada kalimat "Jannah"

print(astring[11:15])
print(astring[11:15:1])
# Masih Bingung

salinan = "Miftahul Jannah & Kue Pie!!!!"
print(salinan[11:13:2])
# Masih Bingung

print(salinan[::-8])
# Masih Bingung
