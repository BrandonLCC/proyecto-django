from cryptography.fernet import Fernet
import base64

## genero una clave para cifrar y descifrar
key = Fernet.generate_key()
cipher_suite = Fernet(key)

#Funcion para cifrar
def encrypt_message(message):
    cipher_text = cipher_suite.encrypt(message.encode())
    return base64.urlsafe_b64encode(cipher_text).decode()

#funcion para decifrar
def decrypt_message(cipher_text):
    decoded_cipher_text = base64.urlsafe_b64decode(cipher_text)
    decrypted_mesagge = cipher_suite.decrypt(decoded_cipher_text).decode()
    return decrypted_mesagge