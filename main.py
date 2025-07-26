def encode_caesar(message, shift):
    result = ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap around alphabet
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decode_caesar(message, shift):
    # Decoding is just encoding with negative shift
    return encode_caesar(message, -shift)


# Example usage
if __name__ == "__main__":
    msg = "Hello, Caesar!"
    shift = 3

    encoded = encode_caesar(msg, shift)
    decoded = decode_caesar(encoded, shift)

    print(f"Original Message: {msg}")
    print(f"Encoded Message:  {encoded}")
    print(f"Decoded Message:  {decoded}")
