from PIL import Image # biblioteca usada para manipulação de imagens

image_path = "src/LLMcourse/Reduction_Dimension/images/sagrada_familia_spain.jpg"
origin_image = Image.open(image_path)

if origin_image is None:
    raise FileNotFoundError("The image file could not be loaded. Check the path and file integrity.")

# function to convert image to gray scale
def convert_to_gray(image):
    width, height = image.size
    image_gray = Image.new("L", (width, height))
    
    for y in range(height):
        for x in range(width):
            r, g, b = image.getpixel((x, y))
            gray_value = int(0.299*r + 0.587*g + 0.114*b)
            image_gray.putpixel((x, y), gray_value)
    return image_gray

# Function to binarize image
def binarize_image(image_gray, threshold=127):
    width, height = image_gray.size
    image_bin = Image.new("L", (width, height))
    
    for y in range(height):
        for x in range(width):
            gray_value = image_gray.getpixel((x, y))
            bin_value = 255 if gray_value > threshold else 0
            image_bin.putpixel((x, y), bin_value)
    return image_bin

# Convert the image to gray scale
image_gray = convert_to_gray(origin_image)

# Binarize the image
image_bin = binarize_image(image_gray)

# Display the images
print("Original Image")
origin_image.show()

print("Imagem em escala de cinza")
image_gray.show()

print("Imagem binarizada")
image_bin.show()