def encrypt(message, shift):
    encrypted_message = ""

    for char in message:
        if char.isalpha():
            if char.isupper():
                position = ord(char) - ord('A')
                new_position = (position + shift) % 26
                encrypted_message += chr(new_position + ord('A'))
            else:
                position = ord(char) - ord('a')
                new_position = (position + shift) % 26
                encrypted_message += chr(new_position + ord('a'))
        else:
            encrypted_message += char

    return encrypted_message


def decrypt(message, shift):
    decrypted_message = ""

    for char in message:
        if char.isalpha():
            if char.isupper():
                position = ord(char) - ord('A')
                new_position = (position - shift) % 26
                decrypted_message += chr(new_position + ord('A'))
            else:
                position = ord(char) - ord('a')
                new_position = (position - shift) % 26
                decrypted_message += chr(new_position + ord('a'))
        else:
            decrypted_message += char

    return decrypted_message