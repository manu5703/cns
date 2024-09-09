import numpy as np

N = 3  # Matrix size

# Function to encrypt the message
def encrypt(key, message):
    key_matrix = np.zeros((N, N), dtype=int)
    message_vector = np.zeros(N, dtype=int)
    
    # Convert message into a numerical matrix (A=0, B=1, ..., Z=25)
    for i in range(N):
        message_vector[i] = ord(message[i]) - ord('A')
    
    # Convert key into a numerical matrix
    k = 0
    for i in range(N):
        for j in range(N):
            key_matrix[i][j] = ord(key[k]) - ord('A')
            k += 1

    # Perform matrix multiplication and mod 26
    encrypted_vector = np.dot(key_matrix, message_vector) % 26
    
    # Convert numbers back to characters
    encrypted_message = ''.join(chr(int(i) + ord('A')) for i in encrypted_vector)
    return encrypted_message

# Function to decrypt the message
def decrypt(inverse_key_matrix, encrypted_message):
    encrypted_vector = np.zeros(N, dtype=int)
    
    # Convert encrypted message into a numerical matrix
    for i in range(N):
        encrypted_vector[i] = ord(encrypted_message[i]) - ord('A')
    
    # Perform matrix multiplication with the inverse key matrix and mod 26
    decrypted_vector = np.dot(inverse_key_matrix, encrypted_vector) % 26
    
    # Handle negative numbers by adding 26
    decrypted_vector = [int(i) + 26 if i < 0 else int(i) for i in decrypted_vector]
    
    # Convert numbers back to characters
    decrypted_message = ''.join(chr(i + ord('A')) for i in decrypted_vector)
    return decrypted_message

# Main function
def main():
    key = "GYBNQKURP"  # 3x3 key
    message = "ACT"  # Message to be encrypted

    # Inverse key matrix for decryption (manually calculated or using a tool)
    inverse_key_matrix = np.array([[8, 5, 10],
                                   [21, 8, 21],
                                   [21, 12, 8]])
    
    # Encrypt the message
    encrypted_message = encrypt(key, message)
    print(f"Encrypted Message: {encrypted_message}")
    
    # Decrypt the message
    decrypted_message = decrypt(inverse_key_matrix, encrypted_message)
    print(f"Decrypted Message: {decrypted_message}")

if __name__ == "__main__":
    main()
