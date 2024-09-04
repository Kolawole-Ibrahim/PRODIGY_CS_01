def encrypt_caesar_cipher(text, shift):
    """
    Encrypts the given text using Caesar cipher with the specified shift.
    
    :param text: The plaintext to encrypt
    :param shift: The number of positions to shift each letter
    :return: The encrypted ciphertext
    """
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            start = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr(start + (ord(char) - start + shift_amount) % 26)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_caesar_cipher(text, shift):
    """
    Decrypts the given text using Caesar cipher with the specified shift.
    
    :param text: The ciphertext to decrypt
    :param shift: The number of positions each letter was shifted in encryption
    :return: The decrypted plaintext
    """
    return encrypt_caesar_cipher(text, -shift)

def main():
    choice = input("Would you like to (E)ncrypt or (D)ecrypt? ").upper()
    if choice not in ['E', 'D']:
        print("Invalid choice. Please choose 'E' to encrypt or 'D' to decrypt.")
        return

    text = input("Enter the text: ")
    shift = int(input("Enter the shift value: "))

    if choice == 'E':
        result = encrypt_caesar_cipher(text, shift)
        print(f"Encrypted text: {result}")
    else:
        result = decrypt_caesar_cipher(text, shift)
        print(f"Decrypted text: {result}")

if __name__ == "__main__":
    main()
