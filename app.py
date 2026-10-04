import base64

from flask import Flask, render_template, request

from crypto.aes_utils import (
    generate_aes_key,
    encrypt_message,
    decrypt_message
)

from crypto.rsa_utils import (
    generate_rsa_keys,
    encrypt_aes_key,
    decrypt_aes_key,
    private_key_to_pem,
    public_key_to_pem,
    load_private_key
)


app = Flask(__name__)


# =========================
# HOME PAGE
# =========================

@app.route("/")
def home():
    return render_template("index.html")


# =========================
# ENCRYPTION
# =========================

@app.route("/encrypt", methods=["GET", "POST"])
def encrypt():

    result = None
    error = None

    if request.method == "POST":

        message = request.form.get("message", "").strip()

        if message:

            # 1. Generate AES-256 session key
            aes_key = generate_aes_key()

            # 2. Generate RSA key pair
            private_key, public_key = generate_rsa_keys()

            # 3. Encrypt message using AES
            encrypted_data = encrypt_message(
                message,
                aes_key
            )

            # 4. Encrypt AES key using RSA public key
            encrypted_aes_key = encrypt_aes_key(
                aes_key,
                public_key
            )

            # Convert AES key to Base64
            aes_key_b64 = base64.b64encode(
                aes_key
            ).decode("utf-8")

            # Convert RSA keys to PEM
            public_key_pem = public_key_to_pem(
                public_key
            )

            private_key_pem = private_key_to_pem(
                private_key
            )

            # Send everything to HTML
            result = {
                "success": True,

                "encrypted_message":
                    encrypted_data["ciphertext"],

                "nonce":
                    encrypted_data["nonce"],

                "aes_key":
                    aes_key_b64,

                "encrypted_aes_key":
                    encrypted_aes_key,

                "public_key":
                    public_key_pem,

                "private_key":
                    private_key_pem
            }

        else:

            error = "Please enter a message before encrypting."

    return render_template(
        "encrypt.html",
        result=result,
        error=error
    )


# =========================
# DECRYPTION
# =========================

@app.route("/decrypt", methods=["GET", "POST"])
def decrypt():

    result = None
    error = None

    if request.method == "POST":

        try:

            # Get values from decrypt form
            encrypted_message = request.form.get(
                "encrypted_message",
                ""
            ).strip()

            encrypted_aes_key = request.form.get(
                "encrypted_aes_key",
                ""
            ).strip()

            nonce_b64 = request.form.get(
                "nonce",
                ""
            ).strip()

            private_key_pem = request.form.get(
                "private_key",
                ""
            ).strip()


            # Check required fields
            if not encrypted_message:
                raise ValueError(
                    "Encrypted message is missing."
                )

            if not encrypted_aes_key:
                raise ValueError(
                    "RSA-protected AES key is missing."
                )

            if not nonce_b64:
                raise ValueError(
                    "Nonce is missing."
                )

            if not private_key_pem:
                raise ValueError(
                    "RSA private key is missing."
                )


            # ---------------------------------
            # STEP 1
            # Convert encrypted message from Base64
            # ---------------------------------

            ciphertext = base64.b64decode(
                encrypted_message
            )


            # ---------------------------------
            # STEP 2
            # Convert nonce from Base64
            # ---------------------------------

            nonce = base64.b64decode(
                nonce_b64
            )


            # ---------------------------------
            # STEP 3
            # Load RSA private key
            # ---------------------------------

            private_key = load_private_key(
                private_key_pem
            )


            # ---------------------------------
            # STEP 4
            # RSA decrypts the AES session key
            # ---------------------------------

            aes_key = decrypt_aes_key(
                encrypted_aes_key,
                private_key
            )


            # ---------------------------------
            # STEP 5
            # AES decrypts the original message
            # ---------------------------------

            decrypted_message = decrypt_message(
                ciphertext,
                nonce,
                aes_key
            )


            # Send decrypted message to HTML
            result = decrypted_message


        except Exception:

            error = (
                "Decryption failed. "
                "Please check that all values are correct "
                "and that you are using the matching RSA "
                "private key."
            )


    return render_template(
        "decrypt.html",
        result=result,
        error=error
    )


# =========================
# HOW IT WORKS
# =========================

@app.route("/how-it-works")
def how_it_works():

    return render_template(
        "how-it-works.html"
    )


# =========================
# ABOUT
# =========================

@app.route("/about")
def about():

    return render_template(
        "about.html"
    )


# =========================
# RUN APPLICATION
# =========================

if __name__ == "__main__":

    app.run(
        debug=True
    )