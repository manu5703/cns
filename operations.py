def main():
    str_input = "Hello World"
    str1 = []
    str2 = []
    str3 = []
    
    print("The Plain Text: ", end="")
    for ch in str_input:
        print(ch, end="")
    
    print("\nCipher text after AND Operation: ", end="")
    for ch in str_input:
        encrypted_ch = chr(ord(ch) & 127)
        str1.append(encrypted_ch)
        print(encrypted_ch, end="")
    
    print("\nCipher text XOR Operation: ", end="")
    for ch in str_input:
        encrypted_ch = chr(ord(ch) ^ 127)
        str3.append(encrypted_ch)
        print(encrypted_ch, end="")
    
    print("\nCipher text OR Operation: ", end="")
    for ch in str_input:
        encrypted_ch = chr(ord(ch) | 127)
        str2.append(encrypted_ch)
        print(encrypted_ch, end="")
    
    print()

if __name__ == "__main__":
    main()
