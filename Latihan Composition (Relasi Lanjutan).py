class Penulis:
    def __init__(self, nama):
        self.nama = nama


class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis  # Composition

    def info(self):
        return f"Judul: {self.judul}, Penulis: {self.penulis.nama}"


# Instansiasi objek
penulis1 = Penulis("Tere Liye")
buku1 = Buku("Bumi", penulis1)

# Mengakses data penulis dari objek buku
print(buku1.info())
