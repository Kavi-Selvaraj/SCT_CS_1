from caesar_cipher import encrypt, decrypt


def main():
    print("================================")
    print("       CAESAR CIPHER TOOL")
    print("================================")

    print("\n1. Encrypt")
    print("2. Decrypt")

    choice = input("\nEnter your choice (1/2): ")

    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))

    if choice == "1":
        result = encrypt(message, shift)
        print("\nEncrypted message:", result)

    elif choice == "2":
        result = decrypt(message, shift)
        print("\nDecrypted message:", result)

    else:
        print("\nInvalid choice. Please select 1 or 2.")


if __name__ == "__main__":
    main()