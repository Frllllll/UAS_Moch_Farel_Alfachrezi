import csv
import os

FILE_CSV = os.path.join(os.path.dirname(__file__), "tiket.csv")


def baca_data():
    data = []

    try:
        with open(FILE_CSV, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                data.append(row)

    except FileNotFoundError:
        pass

    return data


def simpan_data(data):
    fieldnames = [
        "id_tiket",
        "nama_pelanggan",
        "film",
        "jam_tayang",
        "kursi",
        "harga"
    ]

    with open(FILE_CSV, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(data)


def tambah_tiket():
    data = baca_data()

    id_tiket = input("ID Tiket : ")

    for tiket in data:
        if tiket["id_tiket"] == id_tiket:
            print("ID Tiket sudah digunakan!")
            return

    tiket_baru = {
        "id_tiket": id_tiket,
        "nama_pelanggan": input("Nama Pelanggan : "),
        "film": input("Nama Film : "),
        "jam_tayang": input("Jam Tayang : "),
        "kursi": input("Nomor Kursi : "),
        "harga": input("Harga Tiket : ")
    }

    data.append(tiket_baru)
    simpan_data(data)

    print("Tiket berhasil ditambahkan.")


def tampilkan_tiket():
    data = baca_data()

    if not data:
        print("Belum ada data tiket.")
        return

    print("\n===== DATA TIKET =====")

    for tiket in data:
        print("-" * 40)
        print("ID Tiket       :", tiket["id_tiket"])
        print("Nama Pelanggan :", tiket["nama_pelanggan"])
        print("Film           :", tiket["film"])
        print("Jam Tayang     :", tiket["jam_tayang"])
        print("Kursi          :", tiket["kursi"])
        print("Harga          :", tiket["harga"])


def update_tiket():
    data = baca_data()

    id_tiket = input("Masukkan ID Tiket yang ingin diupdate : ")

    ditemukan = False

    for tiket in data:
        if tiket["id_tiket"] == id_tiket:
            ditemukan = True

            tiket["nama_pelanggan"] = input("Nama Pelanggan Baru : ")
            tiket["film"] = input("Film Baru : ")
            tiket["jam_tayang"] = input("Jam Tayang Baru : ")
            tiket["kursi"] = input("Kursi Baru : ")
            tiket["harga"] = input("Harga Baru : ")

            break

    if ditemukan:
        simpan_data(data)
        print("Data berhasil diupdate.")
    else:
        print("ID Tiket tidak ditemukan.")


def hapus_tiket():
    data = baca_data()

    id_tiket = input("Masukkan ID Tiket yang ingin dihapus : ")

    data_baru = []

    ditemukan = False

    for tiket in data:
        if tiket["id_tiket"] == id_tiket:
            ditemukan = True
        else:
            data_baru.append(tiket)

    if ditemukan:
        simpan_data(data_baru)
        print("Data berhasil dihapus.")
    else:
        print("ID Tiket tidak ditemukan.")