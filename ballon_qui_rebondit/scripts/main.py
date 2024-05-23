import tkinter as tk
import subprocess
import sys
from PIL import Image, ImageTk
from tkinter import messagebox

import pygame

pygame.init()

def launch_game_with_ai():
    subprocess.Popen([sys.executable, "game_with_ai.py"])

def launch_game_with_friend():
    subprocess.Popen([sys.executable, "game_with_friend.py"])

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

button_spacing = 100 
center_y = background_image.height // 2

create_round_button(canvas, background_image.width // 2, center_y - button_spacing, 50, "IA", launch_game_with_ai)
create_round_button(canvas, background_image.width // 2, center_y, 50, "Ami", launch_game_with_friend)
create_round_button(canvas, background_image.width // 2, center_y + button_spacing, 50, "Quitter", root.quit)

root.mainloop()
