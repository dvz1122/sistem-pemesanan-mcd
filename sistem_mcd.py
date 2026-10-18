#sistem mesin pemesanan McD
#Self Ordering Kiosk

 # 1. Raisha Aqila (16726033)
 # 2. David Fernando Sitorus (16726134)
 # 3. Nayaka Chesta Ahmada (16728190) 
 # 4. Sofia Anindita Maheswari (16726339)
 # 5. Fairul Alif Zidandie (16726183)

#kamus

#menu = (burger              ===
#        ayam                ====
#        nasi                =====
#        nasi ayam           ======>str (string)
#        coca cola           ======>str (string)
#        air putih           =====
#        mcflurry            ====
#        kentang goreng      ===
#        )

#harga=int(integer)

#menampilkan opsi take away atau dine in 
print ("selamat datang di McDonalds")
print ("silahkan pilih opsi pemesanan")
print ("1.take away")
print ("2.dine in")

#pembeli memilih pesanan untuk di take away atau dine in (conditional)
pilihan = input("Masukkan pilihan (1/2): ")
if pilihan == "1":
    print ("Menu take away")

elif pilihan == "2":
#pembeli memasukkan nomor meja
     no_meja = int(input("masukkan nomor meja anda (1-30) : " ))
     print (f"nomor meja {no_meja}")

#daftar list menu yang ada di McD (array)
menu =("burger", "ayam", "nasi", "nasi_ayam", "coca_cola", "air_putih", "kentang_goreng", "mcflurry" )
harga = (20000, 15000, 5000, 18000, 8000, 4000, 13500, 10000)
total = 0

#ingin tambah pesanan atau tidak(looping)
tambah = "ya"

while (tambah == "ya"):

    #Menampilkan menu Mcd di layar (gabungan sequence dan looping)
    print ('Menu McDonalds')  # >>sequence (menampilkan urutan menu dan harga)
    for i in range(8):        # >>looping  (mengulang urutan yang ada di menu dan harga)
        print(i + 1, menu[i], "- Rp", harga[i])

    #pembeli memasukkan jumlah menu McD yang ingin di pesan(sequence)
    jumlah_pesanan = int(input('masukkan jumlah menu McD yang ingin di pesan : '))

    #pembeli memasukkan no menu dan jumlah menunya(looping)
    for i in range(jumlah_pesanan):
        pilih_menu = int(input('pilih no menu yang ingin di pesan (1-8) :'))
        jumlah = int(input("masukkan jumlahnya : "))

        #menghitung subtotal dan menambahkannya ke total (sequence)
        subtotal = harga[pilih_menu - 1] * jumlah
        total = total + subtotal
        print (f"{menu[pilih_menu - 1]} x {jumlah} = Rp {subtotal}")

    print (f"Total sementara : Rp {total}")

    #menanyakan apakah mau tambah pesanan(looping)
    tambah = input("Apakah mau tambah pesanan? (ya/tidak) : ")

#menampilkan struk pembayaran
print ("STRUK PEMBAYARAN")

#conditional 
if pilihan == "1": 
    print ("Tipe Pesanan : Take Away")
elif pilihan == "2":
    print (f"Tipe Pesanan : Dine In (Meja {no_meja})")

print (f"Total pembayaran : Rp {total}")
print ("Terima kasih telah memesan di McD!")
