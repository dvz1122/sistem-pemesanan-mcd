# sistem mesin pemesanan McD
# Self Ordering Kiosk

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

# menampilkan opsi take away atau dine in (Sequence)
print("selamat datang di McDonalds")
print("silahkan pilih opsi pemesanan")
print("1.take away")
print("2.dine in")

# pembeli memilih pesanan untuk di take away atau dine in (Kondisional)
pilihan = input("Masukkan pilihan (1/2): ")
if pilihan == "1":
    print("Menu take away")
elif pilihan == "2":
    # pembeli memasukkan nomor meja
    no_meja = int(input("masukkan nomor meja anda (1-30) : "))
    print(f"nomor meja {no_meja}")

# daftar list menu dan harga yang ada di McD (Array)
menu = (
    "burger",
    "ayam",
    "nasi",
    "nasi_ayam",
    "coca_cola",
    "air_putih",
    "kentang_goreng",
    "mcflurry",
)
harga = (20000, 
         15000, 
         5000, 
         18000, 
         8000, 
         4000, 
         13500, 
         10000)

#digunakan untuk menampung loopingan dari menu tambahan (array) (maks 50)
nama_pesanan = [""] * 50
jumlah_pesanan = [0] * 50
subtotal_pesanan = [0] * 50

total = 0 # penanda dan penyimpan total harga
banyak_pesanan = 0  # Penanda buat array/list menu dan harga yang di loopingkan (yang dipilih oleh customer)

# Menampilkan menu Mcd di layar ( gabungan Sequence & Looping)
print("\nMenu McDonalds")
for i in range(8):
    print(i + 1, menu[i], "- Rp", harga[i])

tambah = "ya" # kondisi dimana ketika customer memilih "ya" maka sistem akan kembali kebagian pilih_menu (Looping)

while tambah == "ya": # kondisi dimana ketika customer memilih "ya" maka sistem akan kembali kebagian pilih_menu (Looping)

    # pembeli memilih nomor menu dan jumlahnya (Sequence)
    pilih_menu = int(input("\npilih no menu yang ingin di pesan (1-8) : "))
    jumlah = int(input("masukkan jumlahnya : "))

    # sistem menghitung subtotal dan total (Sequence)
    subtotal = harga[pilih_menu - 1] * jumlah
    total = total + subtotal

    # Menyimpan data ke Array sebelum di tampilkan kedalam output (struk) 
    nama_pesanan[banyak_pesanan] = menu[pilih_menu - 1]
    jumlah_pesanan[banyak_pesanan] = jumlah
    subtotal_pesanan[banyak_pesanan] = subtotal

    # Menambah hitungan berapa jenis menu yang sudah dipesan
    banyak_pesanan = banyak_pesanan + 1

    print(f"{menu[pilih_menu - 1]} x {jumlah} = Rp {subtotal}")
    print(f"Total sementara : Rp {total}")

    # customer menginput apakah mau tambah pesanan atau tidak (Looping)
    tambah = input("Apakah mau tambah pesanan? (ya/tidak) : ")

#
# MENAMPILKAN STRUK PEMBAYARAN
print("\n==============================")
print("       STRUK PEMBAYARAN       ")
print("==============================")

# Kondisional tipe pesanan
if pilihan == "1":
    print("Tipe Pesanan : Take Away")
elif pilihan == "2":
    print(f"Tipe Pesanan : Dine In (Meja {no_meja})")

print("\nRincian Pesanan:")

# Looping untuk mencetak (print) Array/list dari loopingan menu awal dan menu tambahan customer dari awal sampai habis
for i in range(banyak_pesanan):
    print(
        f"{i + 1}. {nama_pesanan[i]} x {jumlah_pesanan[i]} = Rp {subtotal_pesanan[i]}"
    )

print("------------------------------")
print(f"Total pembayaran : Rp {total}")
print("==============================")
print("Terima kasih telah memesan di McD!")
