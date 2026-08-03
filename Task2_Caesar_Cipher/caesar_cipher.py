# caesar_cipher.py
# Small script to encrypt/decrypt text using a Caesar cipher.
# Idea: shift every letter by a fixed number of positions in the alphabet.
# Example with shift = 3 -> 'a' becomes 'd', 'b' becomes 'e', and so on.
# Non-letter characters (numbers, spaces, punctuation) are left untouched.


def encrypt_text(text, shift):
    result = ""
    for ch in text:
        if ch.isupper():
            # shift within A-Z, wrap around using % 26
            new_pos = (ord(ch) - ord('A') + shift) % 26
            result += chr(new_pos + ord('A'))
        elif ch.islower():
            # shift within a-z, wrap around using % 26
            new_pos = (ord(ch) - ord('a') + shift) % 26
            result += chr(new_pos + ord('a'))
        else:
            # keep spaces, digits, punctuation as they are
            result += ch
    return result


def decrypt_text(text, shift):
    # decryption is basically encryption with a negative shift
    return encrypt_text(text, -shift)


def get_valid_shift():
    # keep asking until we get a proper number, don't want the program to crash
    while True:
        raw = input("Enter shift value (e.g. 3): ")
        try:
            return int(raw)
        except ValueError:
            print("That's not a number, try again.")


def main():
    print("---- Simple Caesar Cipher Tool ----")
    message = input("Enter the text you want to encrypt: ")
    shift = get_valid_shift()

    encrypted = encrypt_text(message, shift)
    decrypted = decrypt_text(encrypted, shift)

    print("\nOriginal Text :", message)
    print("Encrypted Text:", encrypted)
    print("Decrypted Text:", decrypted)

    # quick sanity check - decrypted should always match the original
    if decrypted == message:
        print("\n(Check passed: decrypted text matches the original)")
    else:
        print("\n(Something's off, decrypted text doesn't match original)")


if __name__ == "__main__":
    main()
