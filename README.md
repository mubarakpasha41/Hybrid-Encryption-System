Hybrid encryption combines the advantages of both algorithms:

```text
AES
│
├── Fast encryption
└── Encrypts the actual message/data

RSA
│
├── Public/private key system
└── Protects the AES session key

Together
│
└── Hybrid Encryption

🔄 System Workflow
Encryption Process
                 SENDER
                    │
                    ▼
          Generate RSA Key Pair
                    │
                    ▼
          Generate AES Session Key
                    │
                    ▼
             AES Encryption
                    │
                    ▼
            Encrypted Message
                    │
                    │
             AES Session Key
                    │
                    ▼
       RSA Public Key Encryption
                    │
                    ▼
        Encrypted AES Session Key
                    │
                    ▼
              TRANSMISSION

Decryption Process
              RECEIVER
                  │
                  ▼
       Encrypted AES Session Key
                  │
                  ▼
       RSA Private Key Decryption
                  │
                  ▼
        Recover AES Session Key
                  │
                  ▼
           AES Decryption
                  │
                  ▼
          Original Message

🧩 Complete Encryption and Decryption Flow
1. Generate RSA public/private key pair
                    ↓
2. Generate random AES session key
                    ↓
3. Encrypt the message using AES
                    ↓
4. Encrypt AES session key using RSA public key
                    ↓
5. Store/transmit:
       • Encrypted message
       • Encrypted AES key
       • Nonce
                    ↓
6. Receiver provides RSA private key
                    ↓
7. RSA decrypts the AES session key
                    ↓
8. Recover AES session key
                    ↓
9. AES decrypts the encrypted message
                    ↓
10. Original message is recovered

This follows the proposed methodology of the project. cns_report_hybrid_encryption_co…
🛡️ Cryptographic Algorithms
AES-256
AES is used to encrypt the actual message.
The current implementation uses:
- AES-256
- AES-GCM
- Randomly generated session key
- Random nonce
- Authenticated encryption
The AES session key is generated randomly for each encryption operation.
RSA-2048
RSA is used to protect the AES session key.
The current implementation uses:
- RSA-2048
- Public/private key pair
- RSA-OAEP
- SHA-256 with OAEP
- Public key for encryption
- Private key for decryption
RSA does not encrypt the entire message. It protects the AES session key.
🔑 Key Management
The system uses two types of cryptographic keys.
AES Session Key
A random AES-256 key is generated for encrypting the actual message.
Message
   │
   ▼
AES-256 Session Key
   │
   ▼
Encrypted Message

RSA Key Pair
RSA generates:
RSA Public Key
      │
      ▼
Encrypt AES Session Key


RSA Private Key
      │
      ▼
Decrypt AES Session Key

The receiver's private key must match the RSA public key used to protect the AES session key.
🏗️ Project Architecture
                         WEB INTERFACE
                              │
                ┌─────────────┴─────────────┐
                │                           │
             ENCRYPT                     DECRYPT
                │                           │
                ▼                           ▼
          AES Encryption              RSA Decryption
                │                           │
                ▼                           ▼
        Encrypted Message             AES Session Key
                │                           │
                ▼                           ▼
       RSA Key Encryption             AES Decryption
                │                           │
                └─────────────┬─────────────┘
                              │
                              ▼
                         RESULT

📁 Project Structure
Hybrid-Encryption-System/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── crypto/
│   ├── __init__.py
│   ├── aes_utils.py
│   └── rsa_utils.py
│
├── templates/
│   ├── index.html
│   ├── encrypt.html
│   ├── decrypt.html
│   ├── how-it-works.html
│   └── about.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   ├── js/
│   │   └── script.js
│   │
│   └── images/
│       └── security-illustration.svg
│
├── keys/
├── uploads/
└── encrypted/

🧩 Project Modules
1. RSA Key Management
Responsible for:
- Generating RSA public/private keys
- Converting keys to PEM format
- Loading private keys
- Managing RSA encryption/decryption
2. AES Key Management
Responsible for:
- Generating random AES-256 session keys
- Generating random nonces
3. AES Encryption
Responsible for:
- Encrypting the original message
- Generating ciphertext
- Generating the nonce required for decryption
4. RSA Key Encryption
Responsible for:
- Encrypting the AES session key using the RSA public key
5. RSA Key Decryption
Responsible for:
- Using the RSA private key to recover the AES session key
6. AES Decryption
Responsible for:
- Using the recovered AES key
- Decrypting the ciphertext
- Recovering the original message
7. Result Handling
Responsible for displaying:
- Encrypted message
- AES session key
- RSA-protected AES key
- Nonce
- RSA public key
- RSA private key
- Decrypted message
- Error messages
8. Web User Interface
The Flask application provides:
- Home page
- Encrypt page
- Decrypt page
- How It Works page
- About page
💻 Technologies Used
Technology	Purpose
Python	Main programming language
Flask	Web application framework
AES-256	Symmetric encryption
AES-GCM	Authenticated encryption
RSA-2048	Asymmetric encryption
RSA-OAEP	RSA encryption padding
SHA-256	Used with RSA-OAEP
Cryptography	Python cryptographic library
HTML	Web page structure
CSS	User interface design
JavaScript	Client-side interaction
Git	Version control
GitHub	Source-code hosting


The project proposal specifies Python, AES, RSA, and the Python cryptography library as the core technologies. cns_report_hybrid_encryption_co…
📦 Requirements
The project requires:
Flask
cryptography

These dependencies are also listed in:
requirements.txt

🚀 Installation and Setup
1. Clone the repository
git clone https://github.com/YOUR-USERNAME/Hybrid-Encryption-System.git

Replace:
YOUR-USERNAME

with your GitHub username.
2. Open the project
cd Hybrid-Encryption-System

3. Create a virtual environment
For Windows:
python -m venv venv

4. Activate the virtual environment
PowerShell:
.\venv\Scripts\Activate.ps1

You should see:
(venv)

at the beginning of the terminal.
5. Install dependencies
pip install -r requirements.txt

6. Run the Flask application
python app.py

The application will start at:
http://127.0.0.1:5000

Open this address in your web browser.
🌐 Application Pages
Home
The home page provides an overview of the Hybrid Encryption System and explains the role of AES and RSA.
Encrypt
The Encrypt page allows the user to enter a message and generate:
- Encrypted message
- AES-256 session key
- RSA-protected AES key
- Nonce
- RSA public key
- RSA private key
Decrypt
The Decrypt page accepts the encrypted information and matching RSA private key and attempts to recover the original message.
How It Works
Explains the complete AES + RSA hybrid encryption workflow.
About
Provides information about the project and its purpose.
🧪 Testing
The proposed project includes testing with different messages, files, keys, and modified encrypted data. cns_report_hybrid_encryption_co…
Test Case 1 — Normal Message
Input
Hello, this is my secure message.

Expected Result
Encryption Successful
Decryption Successful
Original Message Recovered

Test Case 2 — Correct RSA Private Key
Input
Encrypted message
+
Matching RSA private key

Expected Result
AES session key recovered
Original message recovered

Test Case 3 — Incorrect RSA Private Key
Input
Encrypted message
+
Incorrect RSA private key

Expected Result
Decryption Failed

Test Case 4 — Modified Ciphertext
Input
Modified encrypted message

Expected Result
Decryption Failed

Test Case 5 — Corrupted Encryption Data
Input
Corrupted ciphertext,
invalid nonce,
or invalid encryption parameters

Expected Result
Decryption Failed

The project's proposed testing specifically includes valid private keys, incorrect private keys, and modified/corrupted encrypted data. cns_report_hybrid_encryption_co…
📊 Expected Results
The system is expected to:
- Securely encrypt messages and files.
- Use AES for efficient data encryption.
- Use RSA for secure AES key exchange.
- Demonstrate symmetric and asymmetric cryptography.
- Recover original data using correct keys.
- Prevent successful decryption using incorrect or invalid keys.
These outcomes are part of the project's proposed expected results. cns_report_hybrid_encryption_co…
🧠 Learning Outcomes
Through this project, we gain practical understanding of:
- Symmetric cryptography
- Asymmetric cryptography
- AES
- RSA
- Key management
- Secure key exchange
- Confidentiality
- Encryption and decryption
- Cryptographic libraries
- Flask web application development
The project addresses the course outcomes related to public-key cryptosystems and analysis of symmetric and asymmetric cryptographic algorithms. cns_report_hybrid_encryption_co…
🔮 Future Enhancements
The project can be extended with:
- File upload encryption
- PDF encryption and decryption
- Downloadable encrypted files
- Secure private-key storage
- Password-protected private keys
- User authentication
- Encryption history
- Improved error handling
- HTTPS deployment
- Additional cryptographic algorithms
The original project proposal includes message/file handling and PDF/text-file testing as part of the planned system scope. cns_report_hybrid_encryption_co…
🔒 Security Considerations
This project is intended primarily for educational and academic purposes.
For a production system:
- Private keys should not be displayed unnecessarily.
- Private keys should be stored securely.
- Sensitive information should not be committed to GitHub.
- Authentication and authorization should be implemented.
- HTTPS should be used for network communication.
- Secure key-storage mechanisms should be used.
The repository uses .gitignore to prevent local virtual-environment files, generated keys, uploaded files, encrypted files, and other sensitive local data from being committed.
🎓 Academic Information
University: Alliance University
School: Alliance School of Advanced Computing
Course Code: EICSA311
Course: Cryptography and Network Security
Project Title: Hybrid Encryption System

Student
Mubarak Pasha	1410



📚 Project Methodology
The project follows these major stages:
RSA Key Generation
        ↓
AES Key Generation
        ↓
Data Encryption
        ↓
AES Key Encryption using RSA
        ↓
Secure Transmission / Storage
        ↓
RSA Key Decryption
        ↓
AES Decryption
        ↓
Original Data Recovery
        ↓
Testing and Result Analysis

This methodology is based on the proposed project workflow. cns_report_hybrid_encryption_co…
⭐ Project Status
Current Development
- [x] Flask application setup
- [x] Professional web interface
- [x] AES encryption
- [x] RSA key generation
- [x] RSA protection of AES session key
- [x] Message encryption
- [x] Message decryption
- [x] Git repository
- [x] GitHub repository
- [x] Project documentation
- [ ] File encryption
- [ ] PDF encryption/decryption
- [ ] Downloadable encrypted package
- [ ] Final testing and screenshots
⚠️ Disclaimer
This project has been developed for academic and educational purposes as part of the Cryptography and Network Security course.
It demonstrates the concepts of hybrid encryption using AES and RSA and should not be considered a complete production-grade secure communication system.
👨‍💻 Developed By
Mubarak Pasha

🔐 AES + RSA = Hybrid Encryption