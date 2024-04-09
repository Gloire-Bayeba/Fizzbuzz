def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if character is alphabetic
            shifted = ord(char) + shift  # Apply shift to Unicode code point
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def main():
    plaintext = input("Please enter a sentence: ").lower()  # Convert input to lowercase
    encrypted_sentence = caesar_cipher(plaintext, 5)
    print("The encrypted sentence is:", encrypted_sentence)

if __name__ == "__main__":
    main()