import base64
import sys

def caesar_cipher(text, shift, decrypt=False):
    if decrypt:
        shift = -shift
    
    result = []
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - start + shift) % 26 + start)
            result.append(shifted_char)
        else:
            result.append(char)
    return "".join(result)

def xor_cipher(text, key):
    if not key:
        return text
    
    result = []
    key_length = len(key)
    for i, char in enumerate(text):
        key_char = key[i % key_length]
        xor_result = chr(ord(char) ^ ord(key_char))
        result.append(xor_result)
    return "".join(result)

def base64_encode(text):
    text_bytes = text.encode('utf-8')
    base64_bytes = base64.b64encode(text_bytes)
    return base64_bytes.decode('utf-8')

def base64_decode(text):
    try:
        base64_bytes = text.encode('utf-8')
        text_bytes = base64.b64decode(base64_bytes)
        return text_bytes.decode('utf-8')
    except Exception as e:
        return f"Error decoding Base64: {e}"

def vigenere_cipher(text, key, decrypt=False):
    if not key:
        return text
    
    result = []
    key_index = 0
    key = key.upper()
    
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            if decrypt:
                shift = -shift
            
            start = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - start + shift) % 26 + start)
            result.append(shifted_char)
            key_index += 1
        else:
            result.append(char)
    return "".join(result)

def get_input(prompt):
    return input(prompt).strip()

def main():
    while True:
        print("\n--- Mini Encryption/Decryption Tool ---")
        print("1. Caesar Cipher")
        print("2. XOR Cipher")
        print("3. Base64 Encoder/Decoder")
        print("4. Vigenère Cipher")
        print("5. Exit")
        
        choice = get_input("Select an option (1-5): ")
        
        if choice == '1':
            text = get_input("Enter text: ")
            try:
                shift = int(get_input("Enter shift value (integer): "))
            except ValueError:
                print("Invalid shift value. Please enter an integer.")
                continue
            
            mode = get_input("Encrypt or Decrypt? (E/D): ").upper()
            if mode.startswith('D'):
                print(f"Result: {caesar_cipher(text, shift, decrypt=True)}")
            else:
                print(f"Result: {caesar_cipher(text, shift, decrypt=False)}")
                
        elif choice == '2':
            text = get_input("Enter text: ")
            key = get_input("Enter key: ")
            print(f"Result: {xor_cipher(text, key)}")
            
        elif choice == '3':
            mode = get_input("Encode or Decode? (E/D): ").upper()
            text = get_input("Enter text: ")
            
            if mode.startswith('D'):
                print(f"Result: {base64_decode(text)}")
            else:
                print(f"Result: {base64_encode(text)}")
        
        elif choice == '4':
            text = get_input("Enter text: ")
            key = get_input("Enter key: ")
            mode = get_input("Encrypt or Decrypt? (E/D): ").upper()
            
            if mode.startswith('D'):
                print(f"Result: {vigenere_cipher(text, key, decrypt=True)}")
            else:
                print(f"Result: {vigenere_cipher(text, key, decrypt=False)}")
                
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
