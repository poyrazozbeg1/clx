import hashlib

# MD5 hash hesaplama fonksiyonu
def calculate_md5(s):
    return hashlib.md5(s.encode()).hexdigest()

# Dil seçimi
print("Dil Seçimi / Language Selection:")
print("1. Türkçe")
print("2. English")
language_choice = input("Bir seçenek girin / Enter a choice (1 or 2): ")

# Türkçe mesajlar
if language_choice == '1':
    msg_md5_prompt = 'Hesaplamak isteğiniz MD5 hash değerini girin: '
    msg_wordlist = 'rockyou.txt'
    msg_search_md5 = 'Aranan MD5 hash değeri: '
    msg_trying = 'Deneniyor: '
    msg_computed_md5 = ' -> Hesaplanan MD5: '
    msg_found = '\nEşleşen parola bulundu: '
    msg_not_found = '\nParola bulunamadı.\n'
    msg_options = "Seçenekler:"
    msg_option1 = "1. Belirli bir MD5 hash değerinin karşılığını bulmaya çalış (Muhtemelen yapmak istediğin şey bu)"
    msg_option2 = "2. Bir inputun MD5 hash değerini hesapla"
    msg_invalid_choice = 'Geçersiz seçenek.'
    msg_input_string = 'MD5 hash değeri hesaplanacak stringi girin: '
    msg_input_result = 'Input: '
    msg_md5_result = ' -> MD5 hash: '
# İngilizce mesajlar
elif language_choice == '2':
    msg_md5_prompt = 'Enter the MD5 hash value: '
    msg_wordlist = 'rockyou.txt'
    msg_search_md5 = 'Searching for MD5 hash value: '
    msg_trying = 'Trying: '
    msg_computed_md5 = ' -> Computed MD5: '
    msg_found = '\nMatching password found: '
    msg_not_found = '\nNo matching password found.\n'
    msg_options = "Options:"
    msg_option1 = "1. Try to calculate a value of MD5 hash (This is probably what you looking for )"
    msg_option2 = "2. Calculate the MD5 hash value of an input string"
    msg_invalid_choice = 'Invalid choice.'
    msg_input_string = 'Enter the string to calculate its MD5 hash: '
    msg_input_result = 'Input: '
    msg_md5_result = ' -> MD5 hash: '
else:
    print("Geçersiz seçenek / Invalid choice.")
    exit()

# Kullanıcıdan işlem seçeneğini al
print(msg_options)
print(msg_option1)
print(msg_option2)
choice = input("Bir seçenek girin / Enter a choice (1 or 2): ")

if choice == '1':
    # Kullanıcıdan hash ve wordlist dosyası yolunu al
    known_md5 = input(msg_md5_prompt)
    wordlist_file = msg_wordlist

    print(f'{msg_search_md5} {known_md5}\n')

    # Wordlist dosyasını açıp her bir parolayı okuyarak karşılaştırma
    with open(wordlist_file, 'r') as file:
        for line in file:
            password = line.strip()  # Satır sonundaki boşlukları kaldır
            md5_hash = calculate_md5(password)
            print(f'{msg_trying} {password} {msg_computed_md5} {md5_hash}')
            if md5_hash == known_md5:
                print(f'{msg_found} {password}\n')
                break
        else:
            print(msg_not_found)

elif choice == '2':
    # Kullanıcıdan input al ve MD5 hashini hesapla
    input_string = input(msg_input_string)
    md5_hash = calculate_md5(input_string)
    print(f'{msg_input_result} {input_string} {msg_md5_result} {md5_hash}')

else:
    print(msg_invalid_choice)
