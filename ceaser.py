def encrypt(text, key):
    encrypted_text = []
    
    for ch in text:
        if ch.isalnum():  # Check if the character is alphanumeric
            if ch.islower():
                ch = chr((ord(ch) - ord('a') + key) % 26 + ord('a'))
            elif ch.isupper():
                ch = chr((ord(ch) - ord('A') + key) % 26 + ord('A'))
            elif ch.isdigit():
                ch = chr((ord(ch) - ord('0') + key) % 10 + ord('0'))
        else:
            print("Invalid Message")
            return None
        encrypted_text.append(ch)
    
    return ''.join(encrypted_text)

def decrypt(text, key):
    decrypted_text = []
    
    for ch in text:
        if ch.isalnum():  # Check if the character is alphanumeric
            if ch.islower():
                ch = chr((ord(ch) - ord('a') - key) % 26 + ord('a'))
            elif ch.isupper():
                ch = chr((ord(ch) - ord('A') - key) % 26 + ord('A'))
            elif ch.isdigit():
                ch = chr((ord(ch) - ord('0') - key) % 10 + ord('0'))
        else:
            print("Invalid Message")
            return None
        decrypted_text.append(ch)
    
    return ''.join(decrypted_text)

def main():
    text = input("Enter a message to encrypt: ")
    key = int(input("Enter the key: "))
    
    encrypted_message = encrypt(text, key)
    if encrypted_message:
        print(f"Encrypted message: {encrypted_message}")
        
        decrypted_message = decrypt(encrypted_message, key)
        if decrypted_message:
            print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
