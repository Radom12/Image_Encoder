# Image Encryption and Decoding with Password Protection

## Overview
This repository provides Python scripts for securely encoding and decoding images using password-based encryption. It ensures that image data is safely stored or transmitted by encrypting it into a hashed format.

## Features
- Encode multiple images from a specified folder into a single encrypted file.
- Password-protected encryption for secure data handling.
- Decode encrypted files to restore original images with the correct password.
- Supports easy customization of folder paths and passwords.

## Requirements
- Python 3.7+
- `cryptography` library

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Radom12/Image_Encoder
   cd Image_Encoder
   ```

2. Install required dependencies:
   ```bash
   pip install cryptography
   ```

## Usage
### Encoding Images
1. Place the images you want to encode in the `images` folder.
2. Run the encoding script:
   ```bash
   python encoder.py
   ```

### Decoding Images
1. Run the decoding script. You will be prompted to enter the password:
   ```bash
   python decoder.py
   ```

2. Decoded images will be saved to the `image-restored` folder.

## Notes
- The encryption key is derived from the password. Use a strong and secure password.
- Ensure the `hashed_images.txt` file is stored securely, as it contains the encrypted image data.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contribution
Contributions are welcome! Feel free to fork the repository and submit a pull request.
