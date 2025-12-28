def input_angka(pesan):
    angka_str = input(pesan)

    # b. Jika input kosong
    if angka_str.strip() == "":
        raise ValueError("Input tidak boleh kosong!")

    try:
        angka = float(angka_str)
    except ValueError:
        raise ValueError("Input harus berupa angka!")

    # c. Validasi angka positif
    if angka < 0:
        raise ValueError("Angka tidak boleh negatif!")

    return angka


def kalkulasi():
    try:
        print("\n=== Program Kalkulator Sederhana ===")
        print("1. Pembagian")
        print("2. Perkalian")
        pilihan = input("Pilih operasi (1/2): ")

        # Input angka
        a = input_angka("Masukkan angka pertama: ")
        b = input_angka("Masukkan angka kedua: ")

        if pilihan == "1":
            # Kasus pembagian
            hasil = a / b
            print(f"Hasil pembagian: {hasil}")

        elif pilihan == "2":
            hasil = a * b
            print(f"Hasil perkalian: {hasil}")

        else:
            print("Pilihan tidak valid.")

    # Penanganan error
    except ZeroDivisionError:
        print("Error: Tidak dapat membagi dengan angka 0!")
    except ValueError as e:
        print(f"Error:", e)

    # d. ELSE → hanya dieksekusi jika TIDAK ada error
    else:
        print("Operasi berhasil tanpa error.")

    # e. FINALLY → selalu dieksekusi
    finally:
        print("Selesai memproses input.\n")


# Running program
kalkulasi()
