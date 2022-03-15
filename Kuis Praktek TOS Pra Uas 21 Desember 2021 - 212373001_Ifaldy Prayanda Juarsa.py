total = 0
barang = []
harga = []

while True:
    print("Daftar Barang\n"
    "1. Roti \t 5000 \n" 
    "2. Es Krim \t 7000 \n"
    "3. Keripik \t 8000 \n"
    "4. Cokelat \t 12000 \n"
    "5. Buku \t 10000 \n"
    "6. Pensil \t 4000 \n"
    "7. Penghapus 3000 \n"
          "")

    kode = int(input("Masukkan Kode Barang :"))
    if kode == 1:
        barang.append("Roti")
        harga.append(5000)
        total += 5000
    elif kode == 2:
        barang.append("Es Krim")
        harga.append(7000)
        total += 7000
    elif kode == 3:
        barang.append("Keripik")
        harga.append(8000)
        total += 8000
    elif kode == 4:
        barang.append("Cokelat")
        harga.append(12000)
        total += 12000
    elif kode == 5:
        barang.append("Buku")
        harga.append(10000)
        total += 10000
    elif kode == 6:
        barang.append("Pensil")
        harga.append(4000)
        total += 4000
    elif kode == 7:
        barang.append("Penghapus")
        harga.append(3000)
        total += 3000
    else:
        print("Kode yang dimasukkan salah")

    lanjut = input("Lanjut Belanja (y/t) : ")
    if lanjut == 't':
        print("")
        break

    print("Barang yang anda beli : ", barang)
    print("Harga Barang : ", harga)
    print("Total yang dibayar : ", total, '\n')

    bayar = int(input("Masukin uang yang Harus Dibayar"))
    if  bayar > total:
        print("Kembalian : ", bayar - total)
    elif bayar == total:
        print("Uang Pas-pasan")
    else:
        print("uang yang anda Bayar kurang", bayar - total)










