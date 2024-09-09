def main():
    str_input = "Hello World"
    str1 = []

    print("The Plain Text: ", end="")
    for ch in str_input:
        print(ch, end="")
    
    print("\nThe Cipher Text: ", end="")
    for ch in str_input:
        encrypted_ch = chr(ord(ch) ^ 0)
        str1.append(encrypted_ch)
        print(encrypted_ch, end="")
    
    print()

if __name__ == "__main__":
    main()
