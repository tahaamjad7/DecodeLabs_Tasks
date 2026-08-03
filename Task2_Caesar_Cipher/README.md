# Task 2: Caesar Cipher Tool

A Python implementation of the classic Caesar cipher for encrypting and
decrypting text.

## How it works
Every letter is shifted by a fixed number of positions in the alphabet
(wrapping around from z back to a). Non-letter characters (spaces, numbers,
punctuation) are left unchanged. Decryption simply reverses the shift.

## How to run
```bash
python3 caesar_cipher.py
```
You'll be asked for a message and a shift value. The script prints the
original, encrypted, and decrypted text, and verifies that decryption
correctly recovers the original message.

## Key Skills
Basic cryptography concepts, string manipulation, ASCII/character arithmetic.
