import math

# a. Class Bentuk
class Bentuk:
    def luas(self):
        return 0

# b. Class Persegi
class Persegi(Bentuk):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi * self.sisi

# b. Class Lingkaran
class Lingkaran(Bentuk):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def luas(self):
        return math.pi * self.jari_jari * self.jari_jari

# c. Demonstrasi Polymorphism
bentuk1 = Bentuk()
bentuk2 = Persegi(5)
bentuk3 = Lingkaran(7)

print("Luas Bentuk:", bentuk1.luas())
print("Luas Persegi:", bentuk2.luas())
print("Luas Lingkaran:", bentuk3.luas())
