from concurrent.futures import ThreadPoolExecutor
from PIL import Image, ImageFilter

def aplicar_filtro(imagen_path):
    img = Image.open(imagen_path)
    img = img.filter(ImageFilter.GaussianBlur(5))
    img.save(f"{imagen_path}_blurred.jpg")
    print(f"Filtro aplicado a {imagen_path}")

imagenes = ["image1.jpg", "image2.jpg", "image3.jpg"]

with ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(aplicar_filtro, imagenes)
