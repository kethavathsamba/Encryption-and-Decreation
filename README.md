Encryption and Decreation

A simple GUI-based encryption and decryption application that uses a substitution cipher to secure your text. The application is built with Python and Tkinter, providing an intuitive interface for encrypting and decrypting messages.

Features

Encryption: Convert plaintext into an encrypted format using a randomly generated substitution key.

Decryption: Revert encrypted text back to plaintext using the same substitution key.

User-Friendly Interface: Clean and simple GUI with dedicated windows for encryption and decryption tasks.

Clear Functionality: Easy-to-use buttons to clear input and output text areas.

Screenshots

Main Menu
/assessts/Main_Window.png


Encryption Window
/assessts/Encryption.png


Decryption Window
/assessts/Decryption.png


How to Run

Prerequisites

Python 3.x installed on your system.

Required modules:

tkinter

random

string

Steps to Run

Clone the repository:

git clone https://github.com/your-username/Encryption-and-Decreation.git
cd Encryption-and-Decreation

Run the script:

python encryption_decreation.py

Use the GUI to encrypt or decrypt text.

How It Works

Key Generation:

A random substitution cipher is generated, mapping each letter of the alphabet to a unique letter.

Encryption:

Input text is transformed based on the substitution key.

Uppercase letters are maintained, while other characters remain unchanged.

Decryption:

The encrypted text is reverted to its original form using the reverse of the substitution key.

File Structure

Encryption-and-Decreation/
|-- encryption_decreation.py  
|-- assets/
    |-- screenshots/        
|-- README.md                 

Future Improvements

Add functionality to save and load encryption keys.

Support for additional encryption methods.

Cross-platform installer for easier deployment.

Contributing

Contributions are welcome! If you find any issues or want to enhance the project, feel free to open a pull request.

License

This project is licensed under the MIT License. See the LICENSE file for details.

