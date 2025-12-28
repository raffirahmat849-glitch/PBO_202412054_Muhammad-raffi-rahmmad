import tkinter as tk
from tkinter import messagebox


class KonversiSuhu:
    def __init__(self, root):
        self.root = root
        self.root.title("Konversi Suhu")
        self.root.geometry("300x200")

        # Label
        self.label = tk.Label(root, text="Celsius", font=("Arial", 12))
        self.label.pack(pady=10)

        # Entry
        self.entry = tk.Entry(root, width=25)
        self.entry.pack(pady=5)

        # Button Konversi
        self.btn_konversi = tk.Button(
            root,
            text="Konversi ke Fahrenheit",
            command=self.konversi
        )
        self.btn_konversi.pack(pady=5)

        # Label Hasil
        self.label_hasil = tk.Label(root, text="", font=("Arial", 12))
        self.label_hasil.pack(pady=10)

    def konversi(self):
        try:
            celsius = float(self.entry.get())
            fahrenheit = (celsius * 9 / 5) + 32
            self.label_hasil.config(
                text=f"Hasil: {fahrenheit:.2f} °F"
            )
        except ValueError:
            messagebox.showwarning(
                "Input Salah",
                "Masukkan angka yang valid!"
            )


# Program utama
if __name__ == "__main__":
    root = tk.Tk()
    app = KonversiSuhu(root)
    root.mainloop()
