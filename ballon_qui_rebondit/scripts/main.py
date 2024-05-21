import tkinter as tk
import subprocess
import sys
from PIL import Image, ImageTk
import pygame

pygame.init()

def launch_bouncing_balloon():
    subprocess.Popen([sys.executable, "bouncing_balloon.py"])

def yeepee():
    pygame.mixer.Sound("../music/yeepee.mp3").play()

root = tk.Tk()
root.title("Menu Principal")

background_image = Image.open("../img/maison.jpg")
background_photo = ImageTk.PhotoImage(background_image)

canvas = tk.Canvas(root, width=background_image.width, height=background_image.height)
canvas.pack(fill="both", expand=True)

canvas.create_image(0, 0, image=background_photo, anchor="nw")

def create_round_button(canvas, x, y, radius, text, command):
    button = canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="pink", outline="pink")
    button_text = canvas.create_text(x, y, text=text, font=("Times New Roman", 14, "bold"), fill="white")

    def on_click(event):
        command()

    canvas.tag_bind(button, "<Button-1>", on_click)
    canvas.tag_bind(button_text, "<Button-1>", on_click)

background_item = canvas.create_image(0, 0, image=background_photo, anchor="nw")

button_spacing = 120 

create_round_button(canvas, background_image.width // 2, background_image.height // 2 - button_spacing, 50, "Lancer le jeu", launch_bouncing_balloon)
create_round_button(canvas, background_image.width // 2, background_image.height // 2, 50, "Quitter", root.quit)
create_round_button(canvas, background_image.width // 2, background_image.height // 2 + button_spacing, 50, "Yeepee", yeepee)

root.mainloop()
