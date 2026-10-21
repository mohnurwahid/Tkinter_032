import tkinter as tk
from tkinter import ttk 

class AplikasiPrediksiProdi:
    
         BG_UTAMA = "#ffffff"
         BG_HEADER = "#4a4a4a"
         BG_PANEL = "#f2f2f2"
         BG_HASIL = "#e6e6e6"
         FG_TEKS = "#333333"
         FG_HEADER = "#ffffff"
         BTN_BG = "#6b6b6b"
         BTN_ACTIVE = "#4a4a4a"
         BORDER = "#bdbdbd"

         def __init__(self, root):
            self.root = root
            self.root.title("Aplikasi Prediksi Prodi Pilihan")
            self.root.geometry("460x640")
            self.root.resizable(False, False)
            self.root.configure(bg=self.BG_UTAMA)

            style = ttk.Style()
            style.theme_use("clam")
            style.configure(
            "Abu.TEntry",
            fieldbackground="#ffffff",
            foreground=self.FG_TEKS,
            bordercolor=self.BORDER,
            lightcolor=self.BORDER,
            darkcolor=self.BORDER,
            padding=4,
        )
            self.mapel = [
            "Matematika", "Bahasa Indonesia", "Bahasa Inggris",
            "Fisika", "Kimia", "Biologi",
            "Ekonomi", "Geografi", "Sejarah", "Sosiologi",
        ]

            self.entries = []

            self.buat_widget()

         def buat_widget(self):
            lbl_judul = tk.Label(
            self.root,
            text="Aplikasi Prediksi Prodi Pilihan",
            font=("Segoe UI", 16, "bold"),
            bg=self.BG_HEADER,
            fg=self.FG_HEADER,
            pady=16,
        )
            lbl_judul.pack(fill="x")

       
            frame_input = tk.LabelFrame(
            self.root,
            text=" Input Nilai Mata Pelajaran ",
            font=("Segoe UI", 10, "bold"),
            bg=self.BG_PANEL,
            fg=self.FG_TEKS,
            bd=1,
            relief="solid",
            padx=20,
            pady=10,
        )
         frame_input.pack(padx=25, pady=15, fill="x")
         frame_input.columnconfigure(0, weight=1)
         frame_input.columnconfigure(1, weight=1)

         for i, nama in enumerate(self.mapel):
            lbl = tk.Label(
                frame_input,
                text=f"{i + 1}. {nama}",
                font=("Segoe UI", 10),
                bg=self.BG_PANEL,
                fg=self.FG_TEKS,
                anchor="w",
            )
            lbl.grid(row=i, column=0, sticky="w", pady=4)

            entry = ttk.Entry(
                frame_input, width=14, justify="center", style="Abu.TEntry"
            )
            entry.grid(row=i, column=1, sticky="e", pady=4)
            self.entries.append(entry)

            btn_prediksi = tk.Button(
            self.root,
            text="Hasil Prediksi",
            font=("Segoe UI", 11, "bold"),
            bg=self.BTN_BG,
            fg="white",
            activebackground=self.BTN_ACTIVE,
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            padx=20,
            pady=8,
            command=self.hasil_prediksi,
        )
         btn_prediksi.pack(pady=10)
         self.lbl_hasil = tk.Label(
            self.root,
            text="Hasil prediksi akan tampil di sini",
            font=("Segoe UI", 12, "bold"),
            bg=self.BG_HASIL,
            fg="#777777",
            relief="solid",
            bd=1,
            width=36,
            pady=14,
        )
         self.lbl_hasil.pack(pady=10)
         def hasil_prediksi(self):
            self.lbl_hasil.config(
                text="Prodi: Teknologi Informasi",
                fg=self.FG_TEKS,
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiPrediksiProdi(root)
    root.mainloop()

