# Cybersecurity and Information Protection
# Lab 1 - Monoalphabetic Replacement Cipher
# Caesar's Cipher
#
# Academic year: 2026/2027
# Student number: 2
# Encryption key = 2 * student number = 4


def caesar_encrypt(message, key):
    encrypted_message = ""

    for character in message:

        if character.isupper():
            encrypted_character = chr(
                (ord(character) - ord('A') + key) % 26 + ord('A')
            )
            encrypted_message += encrypted_character

        elif character.islower():
            encrypted_character = chr(
                (ord(character) - ord('a') + key) % 26 + ord('a')
            )
            encrypted_message += encrypted_character

        else:
            encrypted_message += character

    return encrypted_message


print("========================================")
print("          CAESAR CIPHER")
print("========================================")

message = input("Enter the message to encrypt: ")

student_number = int(input("Enter your student number: "))

key = 2 * student_number

encrypted_message = caesar_encrypt(message, key)

print("\n----------------------------------------")
print("Student number:", student_number)
print("Encryption key:", key)
print("Original message:", message)
print("Encrypted message:", encrypted_message)
print("----------------------------------------")
