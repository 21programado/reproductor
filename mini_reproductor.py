import tkinter as tk
from tkinter import filedialog
import winsound
import os

archivo_actual = None

def cargar_audio():
    global archivo_actual
    archivo = filedialog.askopenfilename(
        filetypes=[("Archivos WAV", "*.wav")]
    )
    if archivo:
        archivo_actual = archivo
        label_archivo.config(text=os.path.basename(archivo))

def reproducir():
    if archivo_actual:
        winsound.PlaySound(archivo_actual, winsound.SND_FILENAME | winsound.SND_ASYNC)

def detener():
    winsound.PlaySound(None, winsound.SND_PURGE)

root = tk.Tk()
root.title("Mini Reproductor WAV")
root.geometry("300x180")

label_archivo = tk.Label(root, text="Ningún archivo cargado")
label_archivo.pack(pady=10)

tk.Button(root, text="Cargar WAV", command=cargar_audio).pack(pady=5)
tk.Button(root, text="Reproducir", command=reproducir).pack(pady=5)
tk.Button(root, text="Detener", command=detener).pack(pady=5)

root.mainloop()
