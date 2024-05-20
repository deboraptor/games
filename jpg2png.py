from PIL import Image

img = Image.open("./gobelet_renverse.jpg")
img = img.convert("RGBA")  # Convert to RGBA to ensure compatibility
img.save("./gobelet_renverse.png")