from cryptography.fernet import Fernet

"""
TODO:
- Generate a key once and reuse it for both pseudonymization and restoration. In a real system, this key would be securely stored.
"""
key = Fernet.generate_key()
fernet = Fernet(key)

def pseudonymize_names(names):
    """
    Encrypt each name with Fernet symmetric encryption.
    - return list of encrypted names
    """
    return [fernet.encrypt(name.encode()).decode() for name in names]


def restore_names(encrypted):
    """
    Decrypt previously pseudonymized names.
    - return list of decrypted names
    """
    return [fernet.decrypt(name.encode()).decode() for name in encrypted]