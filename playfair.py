SIZE = 5

def generate_key_table(key):
    key_table = [['' for _ in range(SIZE)] for _ in range(SIZE)]
    dict_set = set()
    k = 0
    l = 0
    
    # Fill the key_table with the unique letters from the key (excluding 'j')
    for char in key:
        if char != 'j' and char not in dict_set:
            key_table[k][l] = char
            dict_set.add(char)
            l += 1
            if l == SIZE:
                k += 1
                l = 0
    
    # Fill the remaining spaces with the rest of the alphabet, excluding 'j'
    for i in range(26):
        letter = chr(i + ord('a'))
        if letter not in dict_set and letter != 'j':
            key_table[k][l] = letter
            l += 1
            if l == SIZE:
                k += 1
                l = 0
                
    return key_table

def search(key_table, a, b):
    if a == 'j': a = 'i'
    if b == 'j': b = 'i'
    pos = [-1, -1, -1, -1]
    
    for i in range(SIZE):
        for j in range(SIZE):
            if key_table[i][j] == a:
                pos[0] = i
                pos[1] = j
            elif key_table[i][j] == b:
                pos[2] = i
                pos[3] = j
    return pos

def encrypt(text, key_table):
    encrypted = list(text)
    
    for i in range(0, len(encrypted), 2):
        a, b = encrypted[i], encrypted[i+1]
        pos = search(key_table, a, b)
        
        if pos[0] == pos[2]:
            encrypted[i] = key_table[pos[0]][(pos[1] + 1) % SIZE]
            encrypted[i+1] = key_table[pos[2]][(pos[3] + 1) % SIZE]
        elif pos[1] == pos[3]:
            encrypted[i] = key_table[(pos[0] + 1) % SIZE][pos[1]]
            encrypted[i+1] = key_table[(pos[2] + 1) % SIZE][pos[3]]
        else:
            encrypted[i] = key_table[pos[0]][pos[3]]
            encrypted[i+1] = key_table[pos[2]][pos[1]]
    
    return ''.join(encrypted)

def decrypt(text, key_table):
    decrypted = list(text)
    
    for i in range(0, len(decrypted), 2):
        a, b = decrypted[i], decrypted[i+1]
        pos = search(key_table, a, b)
        
        if pos[0] == pos[2]:
            decrypted[i] = key_table[pos[0]][(pos[1] - 1) % SIZE]
            decrypted[i+1] = key_table[pos[2]][(pos[3] - 1) % SIZE]
        elif pos[1] == pos[3]:
            decrypted[i] = key_table[(pos[0] - 1) % SIZE][pos[1]]
            decrypted[i+1] = key_table[(pos[2] - 1) % SIZE][pos[3]]
        else:
            decrypted[i] = key_table[pos[0]][pos[3]]
            decrypted[i+1] = key_table[pos[2]][pos[1]]
    
    return ''.join(decrypted)

def main():
    key = input("Enter the key (in lowercase, without 'j'): ").replace('j', 'i')
    message = input("Enter the message to encrypt/decrypt (in lowercase, without 'j'): ").replace('j', 'i')
    
    if len(message) % 2 != 0:
        message += 'x'  # Pad message with 'x' if its length is odd

    key_table = generate_key_table(key)
    
    encrypted_message = encrypt(message, key_table)
    print(f"Encrypted Message: {encrypted_message}")
    
    decrypted_message = decrypt(encrypted_message, key_table)
    print(f"Decrypted Message: {decrypted_message}")

if __name__ == "__main__":
    main()
