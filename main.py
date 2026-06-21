from collections import deque
from database import *

antrian = deque()

while True:

    print("\n")
    print("===== SISTEM PEMESANAN TIKET BIOSKOP =====")
    print("1. Tambah Tiket")
    print("2. Tampilkan Tiket")
    print("3. Update Tiket")
    print("4. Hapus Tiket")
    print("5. Tambah Antrian")
    print("6. Layani Antrian")
    print("7. Lihat Antrian")
    print("0. Keluar")

    pilihan = input("Pilih Menu : ")

    if pilihan == "1":
        tambah_tiket()

    elif pilihan == "2":
        tampilkan_tiket()

    elif pilihan == "3":
        update_tiket()

    elif pilihan == "4":
        hapus_tiket()

    elif pilihan == "5":
        nama = input("Nama Pelanggan : ")

        antrian.append(nama)

        print(f"{nama} masuk ke antrian.")

    elif pilihan == "6":

        if len(antrian) > 0:
            pelanggan = antrian.popleft()
            print(f"Sedang melayani {pelanggan}")

        else:
            print("Antrian kosong.")

    elif pilihan == "7":

        if len(antrian) == 0:
            print("Antrian kosong.")

        else:
            print("\n===== DAFTAR ANTRIAN =====")

            nomor = 1

            for nama in antrian:
                print(f"{nomor}. {nama}")
                nomor += 1

    elif pilihan == "0":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak tersedia.")