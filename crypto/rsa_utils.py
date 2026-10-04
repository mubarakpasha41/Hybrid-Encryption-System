import base64

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization


def generate_rsa_keys():
    """Generate an RSA public/private key pair."""

    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    public_key = private_key.public_key()

    return private_key, public_key


def encrypt_aes_key(aes_key, public_key):
    """Encrypt the AES session key using RSA."""

    encrypted_key = public_key.encrypt(
        aes_key,

        padding.OAEP(
            mgf=padding.MGF1(
                algorithm=hashes.SHA256()
            ),

            algorithm=hashes.SHA256(),

            label=None
        )
    )

    return base64.b64encode(
        encrypted_key
    ).decode("utf-8")


def decrypt_aes_key(encrypted_key, private_key):
    """Decrypt the AES session key using RSA private key."""

    encrypted_key_bytes = base64.b64decode(
        encrypted_key
    )

    aes_key = private_key.decrypt(
        encrypted_key_bytes,

        padding.OAEP(
            mgf=padding.MGF1(
                algorithm=hashes.SHA256()
            ),

            algorithm=hashes.SHA256(),

            label=None
        )
    )

    return aes_key


def private_key_to_pem(private_key):
    """Convert private key to PEM format."""

    pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,

        format=serialization.PrivateFormat.PKCS8,

        encryption_algorithm=serialization.NoEncryption()
    )

    return pem.decode("utf-8")


def public_key_to_pem(public_key):
    """Convert public key to PEM format."""

    pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,

        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    return pem.decode("utf-8")


def load_private_key(private_key_pem):
    """Load an RSA private key from PEM text."""

    return serialization.load_pem_private_key(
        private_key_pem.encode("utf-8"),
        password=None
    )


def load_public_key(public_key_pem):
    """Load an RSA public key from PEM text."""

    return serialization.load_pem_public_key(
        public_key_pem.encode("utf-8")
    )