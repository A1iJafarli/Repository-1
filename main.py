import time

meme_dict = {
    "CRINGE": "garip ya da utandırıcı bir şey",
    "LOL": "komik bir şeye verilen cevap",
    "ROFL": "bir şakaya karşılık cevap",
    "SHEESH": "onaylamamak",
    "CREEPY": "korkunç",
    "AGGRO": "agresifleşmek/sinirlenmek",
    "SUS": "şüpheli, garip davranan kişi",
    "NO CAP": "gerçekten, cidden (şaka yapmıyorum)",
    "GOAT": "tüm zamanların en iyisi (greatest of all time)",
    "BRUH": "şaşkınlık, hayal kırıklığı zamanı verilen cevap",
    "FR": "gerçekten (for real)",
}

print("Merhaba, MEME DICTIONARY'e hoş geldiniz!")
print()
time.sleep(1)
running = True
while running:
    word = input('''
Anlamadığınız bir kelime yazın: ''').upper()
    print()
    if word == "DURDUR":
        print()
        print("Durduruluyor...")
        time.sleep(0.75)
        print("Durduruldu!")
        running = False
    elif word in meme_dict.keys():
        print("Anlamı: ", meme_dict[word])
        print()
        time.sleep(1)
    else:
        print("Bu kelime henüz sözlüğe eklenmedi.")
        print()
        time.sleep(1)
