def encrypt(plaintext, key):
    plaintext = plaintext.upper()
    ciphertext = ""
    key = key.upper()
    expanded_key = key
    j = 0

    for p in plaintext:
        if p.isalpha():
            shift = (ord(key[j]) - ord('A')) % 26
            encrypted_char = chr(((ord(p) - ord('A') + shift) % 26) + ord('A'))
            ciphertext += encrypted_char
            key += p  # tambahkan plaintext ke key
            expanded_key += p
            j += 1
        else:
            ciphertext += p
            expanded_key += " "  # biar posisi tetap sejajar
    return ciphertext, expanded_key


def decrypt(ciphertext, key):
    ciphertext = ciphertext.upper()
    plaintext = ""
    key = key.upper()
    expanded_key = key
    j = 0

    for c in ciphertext:
        if c.isalpha():
            shift = (ord(key[j]) - ord('A')) % 26
            decrypted_char = chr(((ord(c) - ord('A') - shift) % 26) + ord('A'))
            plaintext += decrypted_char
            key += decrypted_char  # tambahkan plaintext ke key
            expanded_key += decrypted_char
            j += 1
        else:
            plaintext += c
            expanded_key += " "
    return plaintext, expanded_key


def show_debug_table(plaintext, key_expanded, ciphertext):
    print("\n=== DEBUG TABLE ===")
    print(f"Plaintext :  {plaintext.upper()}")
    print(f"Key (exp) :  {key_expanded}")
    print(f"Ciphertext:  {ciphertext}")
    print("====================\n")


if __name__ == "__main__":
    print("=== Auto-Key Vigenère Cipher ===")
    mode = input("Pilih mode (e untuk enkripsi / d untuk dekripsi): ").lower()
    text = input("Masukkan teks: ")
    key = input("Masukkan key awal: ")

    if mode == 'e':
        result, expanded_key = encrypt(text, key)
        print("\nHasil Enkripsi :", result)
        show_debug = input("Tampilkan tabel debug? (y/n): ").lower()
        if show_debug == 'y':
            show_debug_table(text, expanded_key, result)

    elif mode == 'd':
        result, expanded_key = decrypt(text, key)
        print("\nHasil Dekripsi :", result)
        show_debug = input("Tampilkan tabel debug? (y/n): ").lower()
        if show_debug == 'y':
            show_debug_table(result, expanded_key, text)

    else:
        print("Mode tidak dikenali! Gunakan 'e' untuk enkripsi atau 'd' untuk dekripsi.")
