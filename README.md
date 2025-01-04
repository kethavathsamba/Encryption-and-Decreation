# Encryption and Decreation

## Overview

The **Encryption and Decreation** project is a Python-based application featuring a graphical user interface (GUI) for encrypting and decrypting text using a randomized substitution cipher. It provides an interactive experience for users to securely transform and revert text data.

## Features

- **Encrypt Text**: Input text is transformed using a randomized substitution cipher.
- **Decrypt Text**: Encrypted text is reverted to its original form using the same cipher key.
- **Random Key Generation**: A random substitution cipher key is generated for encryption and decryption.
- **User-Friendly GUI**: Interactive GUI for text encryption and decryption.

## Files

### 1. `encryption_decreation.py`
- The primary Python script containing all functionality, including key generation, encryption, decryption, and GUI components.
- Key functions:
  - `generate_key()`: Creates a randomized substitution cipher key.
  - `encrypt(text, key)`: Encrypts input text using the cipher key.
  - `decrypt(encrypted_text, key)`: Decrypts text using the cipher key.

### 2. `Screenshots`
- Folder containing screenshots demonstrating the GUI:
  - `main_window.png`: Displays the main menu with encryption and decryption options.
  - `encryption.png`: Shows the encryption interface.
  - `decryption.png`: Shows the decryption interface.

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/kethavathsamba/encryption-and-decreation.git
   cd encryption-and-decreation
   ```

2. Run the Python script:
   ```bash
   python encryption_decreation.py
   ```

3. Use the GUI to:
   - Encrypt text by entering plaintext and clicking the **Encrypt** button.
   - Decrypt text by entering encrypted text and clicking the **Decrypt** button.

## Future Enhancements

- Add functionality to save and load custom cipher keys.
- Implement export options for encrypted or decrypted text files.
- Enhance GUI design with advanced features like key visualization.

## Prerequisites

- Python 3.x installed on your system.
- Required libraries: `tkinter`, `random`, and `string` (all standard libraries).

## How to Contribute

Feel free to fork the repository and contribute to this project by:

- Fixing bugs.
- Adding new features.
- Improving the code structure or GUI design.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

