import hashlib

# Database sederhana
database = {}

# Fungsi hash password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

while True:
    print("\n" + "="*40)
    print("      SISTEM LOGIN SHA-256")
    print("="*40)
    print("1. Registrasi")
    print("2. Login")
    print("3. Keluar")

    pilih = input("Pilih menu (1-3): ")

    # REGISTRASI
    if pilih == "1":
        print("\n--- REGISTRASI USER ---")

        username = input("Username Baru : ")
        password = input("Password Baru : ")

        hash_pass = hash_password(password)

        database[username] = hash_pass

        print("\nRegistrasi Berhasil!")
        print("Username :", username)
        print("Hash SHA-256 :")
        print(hash_pass)

    # LOGIN
    elif pilih == "2":
        print("\n--- LOGIN USER ---")

        username = input("Username : ")
        password = input("Password : ")

        hash_input = hash_password(password)

        if username in database:

            print("\n--- VERIFIKASI ---")
            print("Hash Input    :", hash_input)
            print("Hash Database :", database[username])

            if hash_input == database[username]:
                print("\nLogin BERHASIL!")
                print(f"Selamat datang, {username}")
            else:
                print("\nLogin GAGAL! Password salah.")

        else:
            print("\nUsername tidak ditemukan!")

    # KELUAR
    elif pilih == "3":
        print("\nProgram selesai.")
        break

    else:
        print("\nMenu tidak valid!")