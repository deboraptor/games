import tkinter as tk
from tkinter import messagebox
import random


class JeuDesGobelets:
    def __init__(self, root):
        self.root = root
        self.root.title("Jeu des Trois Gobelets")

        self.gobelets = ["Vide", "Vide", "Objet"]
        random.shuffle(self.gobelets)

        self.canvas = tk.Canvas(self.root, width=800, height=600, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.images = [
            tk.PhotoImage(file="gobelet.png"),
            tk.PhotoImage(file="gobelet.png"),
            tk.PhotoImage(file="gobelet.png")
        ]

        self.image_etoile = tk.PhotoImage(file="etoile.png")
        self.image_gobelet_renverse = tk.PhotoImage(file="gobelet_renverse.png")

        self.gobelet_ids = [
            self.canvas.create_image(0, 0, image=self.images[0], tags="gobelet1"),
            self.canvas.create_image(0, 0, image=self.images[1], tags="gobelet2"),
            self.canvas.create_image(0, 0, image=self.images[2], tags="gobelet3")
        ]

        self.canvas.tag_bind("gobelet1", "<Button-1>", lambda e: self.reveal(0))
        self.canvas.tag_bind("gobelet2", "<Button-1>", lambda e: self.reveal(1))
        self.canvas.tag_bind("gobelet3", "<Button-1>", lambda e: self.reveal(2))

        self.canvas.bind("<Configure>", self.on_resize)
        self.on_resize(None)

    def on_resize(self, event):
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()

        x_coords = [canvas_width // 4, canvas_width // 2, 3 * canvas_width // 4]
        y_coord = canvas_height // 2

        self.canvas.coords(self.gobelet_ids[0], x_coords[0], y_coord)
        self.canvas.coords(self.gobelet_ids[1], x_coords[1], y_coord)
        self.canvas.coords(self.gobelet_ids[2], x_coords[2], y_coord)

    def reveal(self, index):
        if self.gobelets[index] == "Objet":
            self.canvas.itemconfig(self.gobelet_ids[index], image=self.image_etoile)
            messagebox.showinfo("Félicitations !", "Vous avez trouvé l'objet !")
        else:
            self.canvas.itemconfig(self.gobelet_ids[index], image=self.image_gobelet_renverse)
            messagebox.showinfo("Dommage !", "Vous n'avez pas trouvé l'objet.")
        self.reset_game()  

    def reset_game(self):
        random.shuffle(self.gobelets)
        for i in range(3):
            self.canvas.itemconfig(self.gobelet_ids[i], image=self.images[i])
        self.canvas.tag_bind("gobelet1", "<Button-1>", lambda e: self.reveal(0))
        self.canvas.tag_bind("gobelet2", "<Button-1>", lambda e: self.reveal(1))
        self.canvas.tag_bind("gobelet3", "<Button-1>", lambda e: self.reveal(2))

if __name__ == "__main__":
    root = tk.Tk()
    app = JeuDesGobelets(root)
    root.mainloop()
