import os
import base64
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def generate_aes_key():
    """Generate a random 256-bit AES key."""
    return AESGCM.generate_key(bit_length=256)


def encrypt_message(message, key):
    """Encrypt a text message using AES-GCM."""

    aes = AESGCM(key)

    # Generate a unique 12-byte nonce
    nonce = os.urandom(12)

    # Convert message into bytes
    plaintext = message.encode("utf-8")

    # Encrypt the message
    ciphertext = aes.encrypt(
        nonce,
        plaintext,
        None
    )

    return {
        "ciphertext": base64.b64encode(ciphertext).decode("utf-8"),
        "nonce": base64.b64encode(nonce).decode("utf-8")
    }


def decrypt_message(ciphertext, nonce, key):
    """Decrypt an AES-GCM encrypted message."""

    aes = AESGCM(key)

    plaintext = aes.decrypt(
        nonce,
        ciphertext,
        None
    )

    return plaintext.decode("utf-8")