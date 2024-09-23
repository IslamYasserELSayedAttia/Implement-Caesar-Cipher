def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        # Encrypet uppercase letters
        if char.isupper():
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase letters
        elif char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # Non-alphabetic characters are added unchanged
            encrypted_text += char
    return encrypted_text

def caesar_decipher(text, shift):
    return caesar_cipher(text, -shift)

def main():
    print("Caesar Cipher Encryption/Decryption")
    choice = input("Would you like to (E)ncrypt or (D)ecrypt? ").strip().upper()

    if choice not in ['E', 'D']:
        print("Invalid choice. Please select 'E' to encrypt or 'D' to decrypt.")
        return

    message = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))

    if choice == 'E':
        encrypted_message = caesar_cipher(message, shift)
        print(f"Encrypted message: {encrypted_message}")
    else:
        decrypted_message = caesar_decipher(message, shift)
        print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()