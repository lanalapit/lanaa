# List untuk menyimpan data siswa
data_siswa = []

# Fungsi menampilkan menu
def tampilkan_menu():
    print("\n=== Menu Manajemen Siswa ===")
    print("1. Tambah Siswa")
    print("2. Lihat Siswa")
    print("3. Edit Siswa")
    print("4. Hapus Siswa")
    print("5. Keluar")

# Fungsi menambah siswa
def tambah_siswa():
    nama = input("Masukkan Nama: ")
    usia = input("Masukkan Usia: ")
    nilai = input("Masukkan Nilai Rata-rata: ")
    data_siswa.append({"Nama": nama, "Usia": usia, "Nilai": nilai})
    print(f"[Siswa {nama} berhasil ditambahkan!]")

# Fungsi melihat daftar siswa
def lihat_siswa():
    if not data_siswa:
        print("[Belum ada data siswa]")
    else:
        print("\n=== Daftar Siswa ===")
        for i, siswa in enumerate(data_sisw…