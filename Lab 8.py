from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64


def pad(data):
    """Додаємо заповнення до даних, щоб їх довжина була кратна розміру блоку AES (16 байтів)."""
    pad_len = 16 - len(data) % 16
    return data + bytes([pad_len]) * pad_len


def unpad(data):
    """Видаляємо заповнення з даних."""
    return data[:-data[-1]]


def encrypt_aes_cbc(key, plaintext):
    """
    Шифрує дані у режимі AES-CBC.
    :param key: Ключ шифрування (16, 24 або 32 байти).
    :param plaintext: Вихідний текст.
    :return: Зашифровані дані у форматі base64.
    """
    iv = get_random_bytes(16)  # Ініціалізаційний вектор (IV)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext.encode('utf-8')))
    return base64.b64encode(iv + ciphertext).decode('utf-8')


def decrypt_aes_cbc(key, encrypted_data):
    """
    Розшифровує дані у режимі AES-CBC.
    :param key: Ключ шифрування (16, 24 або 32 байти).
    :param encrypted_data: Зашифровані дані у форматі base64.
    :return: Розшифрований текст.
    """
    raw_data = base64.b64decode(encrypted_data)
    iv = raw_data[:16]  # Виділяємо IV
    ciphertext = raw_data[16:]  # Виділяємо зашифровані дані
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext))
    return plaintext.decode('utf-8')


# Приклад використання
if __name__ == "__main__":
    # AES ключ має бути 16, 24 або 32 байти
    secret_key = get_random_bytes(16)

    original_text = "Це тестове повідомлення для AES у режимі CBC."
    print("Оригінальний текст:", original_text)

    # Шифрування
    encrypted_text = encrypt_aes_cbc(secret_key, original_text)
    print("Зашифрований текст (base64):", encrypted_text)

    # Розшифрування
    decrypted_text = decrypt_aes_cbc(secret_key, encrypted_text)
    print("Розшифрований текст:", decrypted_text)
