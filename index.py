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

