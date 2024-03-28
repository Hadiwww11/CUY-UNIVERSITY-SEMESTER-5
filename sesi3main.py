import random
from libs import welcome_message


welcome_message ("SELAMAT DATANG DI CUYPY")

nama_user = input("Masukkan nama kamu: ")

while nama_user == "":
    nama_user = input("isi dulu nama anda: ")
while True:
    bentuk_goa = "|_|"
    goa_kosong = [bentuk_goa] * 4 # INI TETAP HARUS KOSONG

    cuypy_position = random.randint(1, 4)
    goa = goa_kosong.copy() #INI ADALAH TEMPAT BARU UNTUK SI CUYPY

    goa[cuypy_position - 1] = "|0_0|"
    goa_kosong = ' '.join(goa_kosong)
    goa = ' '.join(goa)
    print(f'''
    Halo {nama_user}! Coba perhatikan goa dibawah ini
    {goa_kosong}
    ''')


    pilihan_user = int(input("Menurut kamu di goa nomor berapa CUYPY berada? [1 / 2 / 3 / 4]: "))


    if pilihan_user == cuypy_position:
        print(f"\n{goa}\n\nSelamat kamu menang ")
    else:
        print(f"\n{goa}\n\nMaaf kamu kalah")
        
    play_again = input("\n\nApakah ingin melanjutkan gamenya lagi? [y/n]")
    if play_again == "n":
        break
print("Program Selesai !")