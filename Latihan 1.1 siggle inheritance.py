class Person:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def info(self):
        return f"Nama: {self.nama}, Umur: {self.umur} tahun"


class Mahasiswa(Person):
    def __init__(self, nama, umur, nim):
        super().__init__(nama, umur)  # pewarisan atribut dari parent
        self.nim = nim

    def info(self):
        return f"Mahasiswa: {self.nama}, Umur: {self.umur} tahun, NIM: {self.nim}"


# Instansiasi objek
p = Person("Budi", 25)
m = Mahasiswa("Adit", 20, "202412054")

# Panggil method info()
print(p.info())
print(m.info())
