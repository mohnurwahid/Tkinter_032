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

