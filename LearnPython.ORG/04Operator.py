# Operator Python
## Penambahan (+)
## Pengurangan (-)
## Pembagian (/)
## Sisa Bagi (%)
## Perkalian (*)
## Perpangkatan (**)

# Operator Arimatika
nambah = 10 + 2
kurang = 10 - 2
bagi = 10 / 2
sisaBagi = 10 % 2
kali = 10 * 2
pangkatan = 10 ** 2

print(f"Operator Penambahan = {nambah}")
print(f"Operator Pengurangan = {kurang}")
print(f"Operator Pembagian = {bagi}")
print(f"Operator Sisa Bagi = {sisaBagi}")
print(f"Operator Perkalian = {kali}")
print(f"Operator Perpangkatan = {pangkatan}")
print("=" * 10, "\n")

# Operator Pada String
heloworld = "Hello" + " " + "World"
print(heloworld, "\n")

banyakHalo = "Halo" * 15
print(banyakHalo, "\n")

# Operator Pada List
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
allList = list1 + list2
print(allList, "\n")

lsi = list1.copy() * 3
print(lsi, "\n")


#Tujuan dari latihan ini adalah untuk membuat dua daftar yang disebut x_list dan y_list,

#yang masing-masing berisi 10 instance dari variabel x dan y.

#Anda juga diharuskan membuat daftar bernama big_list, yang berisi

#variabel x dan y, masing-masing 10 kali, dengan menggabungkan kedua daftar yang telah Anda buat.
# Exercises
x = object()
y = object()

# TODO: change this code
x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")
