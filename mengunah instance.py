class ManajerInventori:
    def __init__(self):
        # Instance attribute: dictionary untuk menyimpan {nama_barang: stok}
        self.inventori = {}

    # 1) Method untuk menambahkan atau memperbarui stok barang
    def tambah_barang(self, nama_barang, jumlah_stok):
        if jumlah_stok > 0:
            if nama_barang in self.inventori:
                # Menambahkan stok jika barang sudah ada
                self.inventori[nama_barang] += jumlah_stok
                pesan = "Stok diperbarui."
            else:
                # Menambahkan barang baru
                self.inventori[nama_barang] = jumlah_stok
                pesan = "Barang baru ditambahkan."
            
            return f"{pesan} {nama_barang}: Stok sekarang {self.inventori[nama_barang]}"
        else:
            return "Jumlah stok harus positif untuk penambahan."

    # 2) Method untuk menghapus (mengurangi) stok barang
    def hapus_barang(self, nama_barang, jumlah_stok):
        if nama_barang not in self.inventori:
            return f"Error: Barang '{nama_barang}' tidak ada dalam inventori."
        
        stok_saat_ini = self.inventori[nama_barang]

        if jumlah_stok > stok_saat_ini:
            return f"Error: Stok '{nama_barang}' ({stok_saat_ini}) tidak mencukupi untuk pengurangan {jumlah_stok}."
        
        # Pengurangan stok
        self.inventori[nama_barang] -= jumlah_stok

        if self.inventori[nama_barang] == 0:
            del self.inventori[nama_barang]  # Hapus dari dict jika stok habis
            return f"Stok '{nama_barang}' habis dan dihapus dari inventori."
        else:
            return f"Berhasil mengurangi {jumlah_stok} unit {nama_barang}. Stok sekarang {self.inventori[nama_barang]}."

    # 3) Method untuk melihat seluruh inventori
    def lihat_inventori(self):
        if not self.inventori:
            return "Inventori kosong."
        
        laporan = "\n--- LAPORAN INVENTORI SAAT INI ---\n"
        for barang, stok in self.inventori.items():
            laporan += f"- {barang}: {stok} unit\n"
        laporan += "----------------------------------"
        return laporan


# --- DEMONSTRASI SEMUA METHOD ---

# Instansiasi objek Manajer Inventori
gudang = ManajerInventori()

print("== Langkah 1: Penambahan Barang Awal ==")
print(gudang.tambah_barang("Laptop Gaming", 10))
print(gudang.tambah_barang("Monitor 27-inch", 5))

print("\n== Langkah 2: Lihat Inventori ==")
print(gudang.lihat_inventori())

print("\n== Langkah 3: Penambahan Stok (Update) dan Pengurangan ==")
print(gudang.tambah_barang("Laptop Gaming", 2))        # update stok
print(gudang.hapus_barang("Monitor 27-inch", 3))       # kurangi stok

print("\n== Langkah 4: Pengurangan Sampai Habis & Lihat Inventori Akhir ==")
print(gudang.hapus_barang("Monitor 27-inch", 2))       # stok habis
print(gudang.lihat_inventori())                        # tampilkan inventori terbaru
