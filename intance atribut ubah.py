class Kendaraan:
    # Class attribute
    bahan_bakar = "Bensin"

    # Constructor
    def __init__(self, merk, warna, tahun):
        self.merk = merk
        self.warna = warna
        self.tahun = tahun

    def info(self):
        return f"{self.merk}, warna {self.warna}, tahun {self.tahun}"


# Instansiasi object
kendaraan1 = Kendaraan("Toyota", "Hitam", 2022)
kendaraan2 = Kendaraan("Honda", "Putih", 2023)

# Akses instance attribute
print(kendaraan1.info())
print(kendaraan2.info())

# Akses class attribute melalui object
print("Bahan bakar kendaraan1:", kendaraan1.bahan_bakar)
print("Bahan bakar kendaraan2:", kendaraan2.bahan_bakar)

# Akses class attribute melalui class
print("Bahan bakar (class):", Kendaraan.bahan_bakar)
