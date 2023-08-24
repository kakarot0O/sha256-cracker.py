# sha256-cracker.py
**SHA-256 Cracker Script**
This is a Python script designed to perform brute-force attacks on SHA-256 hashed passwords using a dictionary of common passwords. It takes a target SHA-256 hash and a password list as input, attempting to find a matching password.

Note: This script is intended for educational and ethical purposes only. Unauthorized use against systems you do not own or have permission to test is illegal.

**Features**
Performs a brute-force attack on a given SHA-256 hash using a dictionary of passwords.
Provides real-time progress updates during the cracking process.
Automatically stops when a matching password is found or the password list is exhausted.

**Prerequisites**
Python 3.x
pwntools library (install using pip install pwntools)

**Usage**
1. Clone this repository to your local machine.
    - git clone https://github.com/your-username/sha256-cracker.git
    - cd sha256-cracker

2. Run the script with the target SHA-256 hash as an argument.
    - python sha256_cracker.py <sha256sum>

3. Replace <sha256sum> with the target SHA-256 hash you want to crack.

**Example**
    python sha256_cracker.py e63e1afb7e21846e833cef8b6703ea9a9ef1db8a90304f74d16a66f9e9703e3d

**Disclaimer**
This script is provided for educational purposes only. Unauthorized use of this script against systems you do not own or have explicit permission to test is illegal. The author is not responsible for any misuse or damage caused by this script.

**Contributing**
Contributions to the project are welcome. Feel free to submit issues and pull requests if you find any improvements or fixes.
