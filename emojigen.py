import os
from PIL import Image

# Define the input and output folders
input_folder = 'input'
output_folder = 'output'

# Sizes for resizing
# sizes = [16, 24, 32, 64]
sizes = [16, 24, 32, 48, 64, 72, 96, 128, 160, 256]

# Ensure output folder and subfolders exist
os.makedirs(output_folder, exist_ok=True)
for size in sizes:
    os.makedirs(os.path.join(output_folder, f'{size}x'), exist_ok=True)

# Function to resize images
def resize_image(image_path, sizes):
    try:
        # Open the image
        image = Image.open(image_path)
        filename = os.path.basename(image_path)
        
        # Save the raw image into the 72x subfolder
        image.save(os.path.join(output_folder, '72x', filename))
        
        # Resize and save the image to different sizes
        for size in sizes:
            resized_image = image.resize((size, size))
            resized_image.save(os.path.join(output_folder, f'{size}x', filename.replace(".png", f"_{size}.png")))
            print(f"Resized {filename} to {size}x{size}")
    
    except Exception as e:
        print(f"Error processing {image_path}: {e}")

# Loop through the input folder to get all images
for filename in os.listdir(input_folder):
    input_image_path = os.path.join(input_folder, filename)
    if os.path.isfile(input_image_path) and filename.endswith('.png'):
        resize_image(input_image_path, sizes)
