def encrypt(message, key):
    encrypted_message = []
    for char in message:
        if 'a' <= char <= 'z':  # Encrypt only lowercase letters
            encrypted_message.append(key[ord(char) - ord('a')])
        else:
            encrypted_message.append(char)  # Keep other characters unchanged
    return ''.join(encrypted_message)

def decrypt(message, key):
    decrypted_message = []
    for char in message:
        if char in key:  # Decrypt only if the character exists in the key
            decrypted_message.append(chr(key.index(char) + ord('a')))
        else:
            decrypted_message.append(char)  # Keep other characters unchanged
    return ''.join(decrypted_message)

def main():
    key = input("Enter the substitution key (26 lowercase letters in random order): ")
    
    if len(key) != 26 or not all('a' <= char <= 'z' for char in key):
        print("Invalid key. Please provide 26 lowercase letters.")
        return

    message = input("Enter the message to encrypt: ")
    
    encrypted_message = encrypt(message, key)
    print(f"Encrypted message: {encrypted_message}")
    
    decrypted_message = decrypt(encrypted_message, key)
    print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
