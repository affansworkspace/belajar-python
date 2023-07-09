# Tebak Angka by Affan's Workspace
# 09/07/2023

# Import library
from random import randint # Library untuk menghasilkan angka random

# Nyawa
nyawa = 3

# Pengulangan
while nyawa > 0:
    print("Anda memiliki", nyawa, "nyawa") # print jumlah nyawa

    angka_rahasia = randint(1, 5) # Menghasilkan angka random dari 1 sampai 5
    angka_tebakan = int(input("Tebak angka dari 1 sampai 5: ")) # Input untuk mendapatkan angka tebakan dari user

    if angka_tebakan == angka_rahasia: # Jika sama, print("Tebakan kamu benar") dan break pengulangan
        print("Tebakan kamu benar")
        break # break berfungsi untuk menghentikan pengulangan secara paksa
    else: # Jika tidak, print("Tebakan kamu salah") dan kurangi 1 variabel nyawa
        print("Tebakan kamu salah")
        nyawa -= 1

if nyawa == 0: # Jika nyawa sama dengan 0 print("Game berakhir. Kamu kehabisan nyawa") dan program otomatis berhenti
    print("Game berakhir. Kamu kehabisan nyawa")