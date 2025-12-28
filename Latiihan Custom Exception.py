class UmurTerlaluMudaError(Exception):
    """Umur kurang dari 5 tahun."""
    pass

class UmurTerlaluTuaError(Exception):
    """Umur lebih dari 100 tahun."""
    pass

class AkunTidakDiizinkanError(Exception):
    """Umur kurang dari 18 tidak boleh daftar akun."""
    pass


def set_umur(umur):
    if umur < 5:
        raise UmurTerlaluMudaError("Umur terlalu muda! Minimal 5 tahun.")
    if umur > 100:
        raise UmurTerlaluTuaError("Umur terlalu tua! Maksimal 100 tahun.")
    return umur


def daftar_akun(umur):
    if umur < 18:
        raise AkunTidakDiizinkanError("Umur kurang dari 18 tahun, tidak boleh daftar akun!")
    return "Akun berhasil didaftarkan."


if __name__ == "__main__":
    while True:  # terus minta input sampai valid
        try:
            u = int(input("Masukkan umur: "))
            umur = set_umur(u)
            break  # keluar jika umur valid
        except ValueError:
            print("Input harus berupa angka!")
        except (UmurTerlaluMudaError, UmurTerlaluTuaError) as e:
            print(e)

    try:
        hasil = daftar_akun(umur)
        print(hasil)
    except AkunTidakDiizinkanError as e:
        print(e)

