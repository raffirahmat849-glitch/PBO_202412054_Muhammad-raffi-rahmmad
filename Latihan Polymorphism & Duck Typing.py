class Laptop:
    def nyalakan(self):
        return "Laptop dinyalakan"

class Smartphone:
    def nyalakan(self):
        return "Smartphone dinyalakan"

# Fungsi dengan Duck Typing
def tes_nyala(obj):
    print(obj.nyalakan())

# Objek dari kedua class
l = Laptop()
s = Smartphone()

# Demonstrasi Duck Typing
tes_nyala(l)
tes_nyala(s)
