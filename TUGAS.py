from abc import ABC, abstractmethod

# 1. Abstraction: Abstract Class Pengguna
class Pengguna(ABC):
    """Abstract Base Class untuk pengguna."""
    def __init__(self, nama):
        self.nama = nama

    @abstractmethod
    def akses(self):
        """Abstract method untuk menampilkan hak akses."""
        pass


# Class turunan untuk mengaktifkan abstraksi
class Member(Pengguna):
    """Class turunan yang merepresentasikan Member."""
    def __init__(self, nama, poin):
        super().__init__(nama)
        self.poin = poin

    # Implementasi abstract method
    def akses(self):
        return f"Member {self.nama} memiliki akses penuh ke fitur dasar."

    # 2. Special Methods
    def __str__(self):
        return f"Member: {self.nama} – Poin: {self.poin}"

    def __add__(self, other):
        return self.poin + other.poin

    def __len__(self):
        return len(self.nama)


# 4. Custom Exception
class PoinTidakValidError(Exception):
    """Kesalahan kustom jika poin yang dimasukkan negatif."""
    pass


# --- Fungsi Utama dan Exception Handling ---
def buat_member(nama):
    """Fungsi untuk meminta input poin dan membuat objek Member."""
    while True:
        poin_str = input(f"Masukkan poin untuk Member {nama}: ").strip()

        try:
            if not poin_str:
                raise ValueError("Input kosong. Poin harus diisi.")

            poin_input = int(poin_str)

            if poin_input < 0:
                raise PoinTidakValidError("Poin tidak boleh negatif. Masukkan angka positif.")

            return Member(nama, poin_input)

        except ValueError as ve:
            print(f"ERROR: {ve}")
        except PoinTidakValidError as ptve:
            print(f"ERROR KHUSUS: {ptve}")
        except Exception as e:
            print(f"ERROR TAK TERDUGA: {e}")


# --- 5. Program Utama dan Pengujian ---
if __name__ == "__main__":
    print("--- Pembuatan Objek Member ---")

    m1 = buat_member("Pouster")
    print("-" * 30)

    m2 = buat_member("Ahmad")
    print("=" * 30)

    # 1. Info Member
    print("1. Informasi Member (metode __str__):")
    print(f"Info m1: {m1}")
    print(f"Info m2: {m2}")
    print(f"Hak Akses m1: {m1.akses()}")
    print("-" * 30)

    # 2. Jumlah poin
    total_poin = m1 + m2
    print(f"2. Jumlah Poin (m1 + m2): {m1.poin} + {m2.poin} = {total_poin}")
    print("-" * 30)

    # 3. Panjang nama
    panjang_nama_m1 = len(m1)
    print(f"3. Panjang Nama m1 ({m1.nama}): {panjang_nama_m1} karakter")
    print("-" * 30)
