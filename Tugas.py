# Latihan Komparasi dan Logika

# membuat gabungan area rentang dari angka

# +++++++3---------10+++++++++
inputUser = float(input("Masukkan angka yang bernilai\nkurang dari 3 \natau \nlebih besar dari 10\n:"))
# memeriksa angka inputan

isKurangDari = (inputUser < 3)
print("Kurang Dari 3 =", isKurangDari)

isLebihBesarDari = (inputUser > 10)
print("Lebih Dari 10 =", isLebihBesarDari)

isCorrect = isKurangDari or isLebihBesarDari
print("Angka yang anda masukkan :", isCorrect)

# ---------3++++++++10---------
# kasus irisan
print("\n",10*"=","\n")
inputUser = float(input("Masukkan angka yang bernilai\nlebih dari 3 \ndan \nkurang dari 10\n:"))

# Lebih dari 3
isLebihDari = inputUser > 3
print("Lebih Dari 3 =", isLebihDari)

isKurangDariSepuluh = inputUser < 10
print("Kurang Dari 10 =", isKurangDariSepuluh)

# ---------3++++++++10---------
isCorrect = isLebihDari and isKurangDariSepuluh
print("Angka yang anda masukkan :", isCorrect)


# Latihan Komparasi dan Logika

# Latihan Soal No. 1
# -----0+++++5------8+++++11------
print("\n",10*"=","\n")
inputUser = float(input("Masukkan angka Inputan\n:"))

# Memeriksa angka inputan
isCorrect1 = inputUser > 0 and inputUser < 5
print("Angka ",inputUser,"Lebih dari 0 dan Kurang dari 5 bernilai =", isCorrect1)

isCorrect2 = inputUser > 8 and inputUser < 11
print("Angka ",inputUser,"Lebih dari 8 dan Kurang dari 11 bernilai", isCorrect2)

isCorrect = isCorrect1 or isCorrect2
print("Angka yang dimasukkan bernilai :", isCorrect)

# Latihan Soal No. 2
# +++++++0------5++++++8------11++++++3

print("\n",10*"=","\n")
inputUser = float(input("Masukkan angka Inputan\n:"))

isCorrect1 = inputUser < 0 or inputUser > 5
print("Angka ",inputUser,"Kurang dari 0 atau Lebih dari 5 bernilai=", isCorrect1)

isCorrect2 = inputUser < 8 or inputUser > 11
print("Angka ",inputUser,"Kurang dari 8 dan Lebih dari 11 bernilai", isCorrect2)

isCorrect = isCorrect1 and isCorrect2
print("Angka yang dmasukkan bernilai :", isCorrect2)








