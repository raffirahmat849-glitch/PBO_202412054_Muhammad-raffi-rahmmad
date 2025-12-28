from abc import ABC, abstractmethod
import math

# =========================
# KELAS ABSTRAK
# =========================
class Bentuk(ABC):

    @abstractmethod
    def luas(self):
        pass

    @abstractmethod
    def keliling(self):
        pass


# =========================
# KELAS LINGKARAN
# =========================
class Lingkaran(Bentuk):

    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def luas(self):
        return math.pi * (self.jari_jari ** 2)

    def keliling(self):
        return 2 * math.pi * self.jari_jari


# =========================
# KELAS PERSEGI PANJANG (DITAMBAH WARNA)
# =========================
class PersegiPanjang(Bentuk):

    def __init__(self, panjang, lebar, warna):
        self.panjang = panjang
        self.lebar = lebar
        self.warna = warna

    def luas(self):
        return self.panjang * self.lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)

    def info(self):
        return f"Persegi Panjang warna {self.warna}"


# =========================
# KELAS PERSEGI (BARU DITAMBAHKAN)
# =========================
class Persegi(Bentuk):

    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi ** 2

    def keliling(self):
        return 4 * self.sisi


# =========================
# CONTOH PENGGUNAAN PROGRAM
# =========================
if __name__ == "__main__":
    # Objek Lingkaran
    l = Lingkaran(5)

    # Objek Persegi Panjang dengan warna
    p = PersegiPanjang(4, 3, "Merah")

    # Objek Persegi
    s = Persegi(6)

    # OUTPUT
    print(f"Luas Lingkaran: {l.luas():.2f}")
    print(f"Keliling Lingkaran: {l.keliling():.2f}\n")

    print(p.info())
    print(f"Luas Persegi Panjang: {p.luas()}")
    print(f"Keliling Persegi Panjang: {p.keliling()}\n")

    print(f"Luas Persegi: {s.luas()}")
    print(f"Keliling Persegi: {s.keliling()}")
