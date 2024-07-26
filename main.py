import tkinter as tk
from tkinter import messagebox
import PIL
from tkinter import *
from PIL import Image, ImageTk, ImageOps
import pygame
import time

pygame.mixer.init() # nos permite cargar sonidos

def load_sound(filename):
    try:
        return pygame.mixer.Sound(filename)
    except FileNotFoundError:
        print("No se encontro el archivo de sonido")
        return None

def load_image(filename):
    try:
        image = Image.open(filename)
        image = image.resize((200,200), Image.LANCZOS)
        image = ImageOps.grayscale(image) #Pasamos a Blanco y Negro
        image = ImageOps.colorize(image, "#1C2833", "#5DADE2") # Recolorizamos
        return ImageTk.PhotoImage(image) 
    except FileNotFoundError:
        print(f"No se encontro el archivo de imagen")
        return None


def preparar_cafe(tipo_cafe, coffe_sound, mensaje, imagen_label, cafe_preparado_imagen):
    if coffee_sound:
        coffee_sound.play()
    mensaje.set(f"Preparando {tipo_cafe}... ")
    root.update() #Forzamos la actulizada de la ventana
    time.sleep(5) #Esperamos que termine el audio
    mensaje.set(f"!Tu {tipo_cafe} esta listo")
    messagebox.showinfo("!Listo¡", f"Tu {tipo_cafe} virtual esta listo¡")

    if cafe_preparado_imagen and imagen_label:
        imagen_label.config(image=cafe_preparado_imagen)
        imagen_label.image = cafe_preparado_imagen

def añadir_leche(mensaje):
    mensaje.set("Añadiendo leche...")
    root.update()
    time.sleep(1) #Simula añadir leche
    mensaje.set("Leche Añadida")
    root.update()

def añadir_azucar(mensaje):
    mensaje.set("Añadiendo Azucar...")
    root.update()
    time.sleep(1) #Simula añadir leche
    mensaje.set("Azucar Añadida")
    root.update()

def limpiar_seleccion(mensaje, cafe_preparado_imagen, cafe_imagen):
    mensaje.set("Selecciona tu tipo de Cafe")
    if cafe_preparado_imagen and imagen_label:
        imagen_label.config(image=cafe_imagen)
        imagen_label.image = cafe_imagen

root = tk.Tk()
root.title("Simulador de Café Virtuál")
root.geometry("500x700")
root.configure(bg="#2E4053")

coffee_sound = load_sound(r".\static\coffee_sound_lite.mp3")
cafe_imagen = load_image(r".\static\Maquina_Hacer_Cafe.jpg")
cafe_preparado_imagen = load_image(r".\static\cafe_preparado.png")



tk.Label(root, text="Simulador de Cafe Virtual", font=('Arial', 16), bg="#2E4053", 
         fg="#ECF0F1").pack(pady=10)
imagen_label = tk.Label(root, image=cafe_imagen, bg="#2E4053")
imagen_label.pack(pady=10)

mensaje = tk.StringVar()
mensaje.set("Seleccionar un tipo de cafe")
tk.Label(root, textvariable=mensaje, font=("Arial", 14), bg="#2E4053", fg="#ECF0F1").pack(pady=10)

botones_cafe = [
    ("Espresso", "Espresso"),
    ("Cappuccino", "Cappuccino"),
    ("Latte", "Latte"),
    ("Americano", "Americano"),
    ("Mocha", "Mocha")
]

for nombre, tipo in botones_cafe: #leemos la dupla A, B
    tk.Button(root, text=f"Preparar {nombre}", 
              command=lambda t=tipo: preparar_cafe(t, coffee_sound, mensaje, imagen_label, 
                                                   cafe_preparado_imagen), font=("Arial", 14),
                                                   bg="#5DADE2", width=20).pack(pady=5)

tk.Button(root, text="Añadir Leche", command=lambda: añadir_leche(mensaje),font=("Arial", 14),
                                                   bg="#5DADE2", width=20).pack(pady=5)
tk.Button(root, text="Añadir Azucar", command=lambda: añadir_azucar(mensaje),font=("Arial", 14),
                                                   bg="#5DADE2", width=20).pack(pady=5)
tk.Button(root, text="Limpiar Seleccion", command=lambda: limpiar_seleccion(mensaje, imagen_label, cafe_imagen),font=("Arial", 14),
                                                   bg="#5DADE2", width=20).pack(pady=5)

root.mainloop()