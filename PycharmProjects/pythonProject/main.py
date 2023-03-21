import cv2
import numpy as np
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk


'class ImageCorrectionApp:
    def __init__(self, master):
        self.master = master
        master.title("Aplikasi Perbaikan Citra")

        # membuat tombol untuk memilih gambar
        self.select_button = Button(master, text="Pilih Gambar", command=self.select_image)
        self.select_button.pack()

        # membuat tombol untuk metode pertama
        self.method_1_button = Button(master, text="Metode 1", command=self.method_1)
        self.method_1_button.pack()

        # membuat tombol untuk metode kedua
        self.method_2_button = Button(master, text="Metode 2", command=self.method_2)
        self.method_2_button.pack()

        # membuat canvas untuk menampilkan gambar
        self.canvas = Canvas(master, width=400, height=400)
        self.canvas.pack()

        # variabel untuk menyimpan gambar yang dipilih
        self.image = None

    def select_image(self):
        # membuka dialog untuk memilih gambar
        file_path = filedialog.askopenfilename()

        # membaca gambar dan menampilkan pada GUI
        self.image = Image.open(file_path)
        self.image.thumbnail((400, 400))
        self.photo = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor=NW, image=self.photo)

    def method_1(self):
        # melakukan perbaikan citra menggunakan metode pertama
        if self.image is not None:
            img = cv2.cvtColor(np.array(self.image), cv2.COLOR_RGB2GRAY)
            img = cv2.equalizeHist(img)
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
            img = Image.fromarray(img)
            img.thumbnail((400, 400))
            self.photo = ImageTk.PhotoImage(img)
            self.canvas.create_image(0, 0, anchor=NW, image=self.photo)

    def method_2(self):
        # melakukan perbaikan citra menggunakan metode kedua
        if self.image is not None:
            img = cv2.cvtColor(np.array(self.image), cv2.COLOR_RGB2GRAY)
            img = cv2.medianBlur(img, 5)
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
            img = Image.fromarray(img)
            img.thumbnail((400, 400))
            self.photo = ImageTk.PhotoImage(img)
            self.canvas.create_image(0, 0, anchor=NW, image=self.photo)


root = Tk()
app = ImageCorrectionApp(root)
root.mainloop()
