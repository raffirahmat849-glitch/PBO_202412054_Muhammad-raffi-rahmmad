# Class Parent
class Karyawan:
    def __init__(self, nama, gaji_pokok):
        self.nama = nama
        self.gaji_pokok = gaji_pokok

    def info_gaji(self):
        return f"{self.nama} memiliki gaji pokok: Rp {self.gaji_pokok}"


# Child Class Manager (Inheritance + Override)
class Manager(Karyawan):
    def __init__(self, nama, gaji_pokok, tunjangan):
        super().__init__(nama, gaji_pokok)
        self.tunjangan = tunjangan

    def info_gaji(self):
        total = self.gaji_pokok + self.tunjangan
        return f"Manager {self.nama} memiliki total gaji: Rp {total}"


# Child Class Programmer (Inheritance + Override)
class Programmer(Karyawan):
    def __init__(self, nama, gaji_pokok, bonus):
        super().__init__(nama, gaji_pokok)
        self.bonus = bonus

    def info_gaji(self):
        total = self.gaji_pokok + self.bonus
        return f"Programmer {self.nama} memiliki total gaji: Rp {total}"


# Composition: Departemen memiliki daftar objek Karyawan
class Departemen:
    def __init__(self, nama):
        self.nama = nama
        self.karyawan_list = []

    def tambah_karyawan(self, karyawan):
        self.karyawan_list.append(karyawan)

    def tampilkan_karyawan(self):
        print(f"Daftar Karyawan di Departemen {self.nama}:")
        for k in self.karyawan_list:
            print(k.info_gaji())


# Instansiasi objek
manager1 = Manager("Rina", 5000000, 2000000)
manager2 = Manager("Tono", 6000000, 2500000)

programmer1 = Programmer("Budi", 4500000, 1500000)
programmer2 = Programmer("Siti", 4000000, 1000000)

# Buat objek departemen dan tambahkan karyawan
dept_it = Departemen("IT")
dept_it.tambah_karyawan(manager1)
dept_it.tambah_karyawan(manager2)
dept_it.tambah_karyawan(programmer1)
dept_it.tambah_karyawan(programmer2)

# Tampilkan semua karyawan
dept_it.tampilkan_karyawan()
