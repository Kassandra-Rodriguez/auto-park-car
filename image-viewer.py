from PIL import Image

image_path = '/home/kassandrarodriguez/auto-park-car/photos/24-04-16_16-50-12.jpg'  # Replace <filename> with your actual file name
image = Image.open(image_path)
image.show()
