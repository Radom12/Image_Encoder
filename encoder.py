import base64
import os
from cryptography.fernet import Fernet

def generate_key(password):
    # Derive a key from the password
    return base64.urlsafe_b64encode(password.ljust(32)[:32].encode())

def encode_images_with_password(input_folder, output_hashed_file, password):
    key = generate_key(password)
    fernet = Fernet(key)
    try:
        with open(output_hashed_file, "wb") as hashed_file:
            for filename in os.listdir(input_folder):
                file_path = os.path.join(input_folder, filename)
                if os.path.isfile(file_path):
                    with open(file_path, "rb") as image_file:
                        encoded_image = base64.b64encode(image_file.read())
                        encrypted_image = fernet.encrypt(encoded_image)
                        hashed_file.write(f"{filename}\n".encode())  # Save the filename
                        hashed_file.write(encrypted_image + b"\n")  # Save the encrypted image
        print("All images successfully encoded and saved to file.")
    except Exception as e:
        print(f"An error occurred: {e}")

encode_images_with_password("images", "hashed_images.txt", "Abhyudith@281")
