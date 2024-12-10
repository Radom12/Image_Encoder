import base64
import os
from cryptography.fernet import Fernet

from encoder import generate_key


def decode_images_with_password(input_hashed_file, output_folder):
    password = input("Enter the password to decode images: ")
    key = generate_key(password)
    fernet = Fernet(key)
    try:
        with open(input_hashed_file, "rb") as hashed_file:
            lines = hashed_file.readlines()
            for i in range(0, len(lines), 2):
                filename = lines[i].strip().decode()  # Get the filename
                encrypted_image = lines[i + 1].strip()  # Get the encrypted image
                decoded_image = base64.b64decode(fernet.decrypt(encrypted_image))
                output_image_path = os.path.join(output_folder, filename)
                with open(output_image_path, "wb") as image_file:
                    image_file.write(decoded_image)
        print("All images successfully decoded and saved to folder.")
    except Exception as e:
        print(f"An error occurred: {e}")

decode_images_with_password("hashed_images.txt", "image-restored")

