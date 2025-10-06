def generate_autokey(key, plaintext):
    """Memperpanjang key dengan plaintext (sesuai Auto-Key Cipher)."""
    key = key.upper()
    plaintext = plaintext.upper()
    extended_key = key
    for char in plaintext:
        if char.isalpha():
            extended_key += char
    return extended_key


def encrypt(plaintext, key):
    plaintext = plaintext.upper()
    ciphertext = ""
    key = key.upper()
    j = 0  # indeks key

    for p in plaintext:
        if p.isalpha():
            shift = (ord(key[j]) - ord('A')) % 26
            encrypted_char = chr(((ord(p) - ord('A') + shift) % 26) + ord('A'))
            ciphertext += encrypted_char
            key += p  # tambahkan huruf plaintext ke key
            j += 1
        else:
            ciphertext += p  # biarkan spasi atau tanda baca apa adanya
    return ciphertext


def decrypt(ciphertext, key):
    ciphertext = ciphertext.upper()
    plaintext = ""
    key = key.upper()
    j = 0

    for c in ciphertext:
        if c.isalpha():
            shift = (ord(key[j]) - ord('A')) % 26
            decrypted_char = chr(((ord(c) - ord('A') - shift) % 26) + ord('A'))
            plaintext += decrypted_char
            key += decrypted_char  # tambahkan huruf plaintext ke key
            j += 1
        else:
            plaintext += c
    return plaintext


def show_debug_table(plaintext, key, ciphertext):
    """Menampilkan tabel debugging untuk proses enkripsi."""
    print("\n=== DEBUG TABLE ===")
    print("Plaintext : ", plaintext.upper())
    print("Key (awal): ", key.upper())
    print("Ciphertext: ", ciphertext)
    print("====================\n")


# ======================
#        MAIN
# ======================
if __name__ == "__main__":
    print("=== Auto-Key Vigenère Cipher ===")
    mode = input("Pilih mode (e untuk enkripsi / d untuk dekripsi): ").lower()
    text = input("Masukkan teks: ")
    key = input("Masukkan key awal: ")

    if mode == 'e':
        result = encrypt(text, key)
        print("\nHasil Enkripsi :", result)
        show_debug = input("Tampilkan tabel debug? (y/n): ").lower()
        if show_debug == 'y':
            show_debug_table(text, key, result)

    elif mode == 'd':
        result = decrypt(text, key)
        print("\nHasil Dekripsi :", result)

    else:
        print("Mode tidak dikenali! Gunakan 'e' untuk enkripsi atau 'd' untuk dekripsi.")
