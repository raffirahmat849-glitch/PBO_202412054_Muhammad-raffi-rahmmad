class Mahasiswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai

    def __str__(self):
        return f"Nama: {self.nama}, Nilai: {self.nilai}"

    def __gt__(self, other):
        return self.nilai > other.nilai

    def __add__(self, other):
        return self.nilai + other.nilai

    def __mul__(self, faktor):
        return self.nilai * faktor

    def __len__(self):
        return len(self.nama)

    def __eq__(self, other):
        return self.nilai == other.nilai


# ==============================
# Contoh penggunaan program
# ==============================

m1 = Mahasiswa("Raffi", 85)
m2 = Mahasiswa("Fajar", 85)
m3 = Mahasiswa("Doni", 70)

# Representasi string
print(m1)
print(m2)

# Perbandingan kesetaraan nilai
print("m1 == m2 :", m1 == m2)

# Operasi matematika
print("m1 + m3 =", m1 + m3)
print("m1 * 2 =", m1 * 2)

# Panjang nama
print("len(m1) =", len(m1))
print("len(m2) =", len(m2))

# Sorting tanpa __lt__
list_mhs = [m1, m2, m3]
sorted_list = sorted(list_mhs, key=lambda x: x.nilai)

print("\nHasil sorting berdasarkan nilai:")
for m in sorted_list:
    print(f"{m.nama} - {m.nilai}")
