##pip install pycryptodome
#!/usr/bin/env python3

import hashlib
import itertools
import string
import time
from datetime import datetime, timedelta
from Crypto.Hash import MD2, MD4

def calculate_md2(s):
    hash_obj = MD2.new()
    hash_obj.update(s.encode('utf-8'))
    return hash_obj.hexdigest()

def calculate_md3(s):
    # MD3 desteklenmemektedir. MD2 ve MD4 mevcut.
    print("MD3 algoritması desteklenmemektedir.")
    return None

def calculate_md4(s):
    hash_obj = MD4.new()
    hash_obj.update(s.encode('utf-8'))
    return hash_obj.hexdigest()

def check_hash(hash_func, wordlist_path, target_hash):
    if not wordlist_path:
        wordlist_path = "rockyou.txt"
    try:
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as file:
            for line in file:
                password = line.strip()
                hash_value = hash_func(password)
                print(f"Trying: {password} -> {hash_value}")
                if hash_value == target_hash:
                    print(f"Password found: {password}")
                    return password
        print("Password not found in wordlist.")
    except FileNotFoundError:
        print(f"Wordlist file {wordlist_path} not found.")

def brute_force_hash(hash_func, target_hash, min_length, max_length, charset):
    start_time = datetime.now()
    try:
        for length in range(min_length, max_length + 1):
            for guess in itertools.product(charset, repeat=length):
                guess_str = ''.join(guess)
                hash_value = hash_func(guess_str)
                print(f"Trying: {guess_str} -> {hash_value}")
                if hash_value == target_hash:
                    end_time = datetime.now()
                    elapsed_time = end_time - start_time
                    print(f"Password found: {guess_str}")
                    print_elapsed_time(elapsed_time)
                    return guess_str
        end_time = datetime.now()
        elapsed_time = end_time - start_time
        print("Password not found.")
        print_elapsed_time(elapsed_time)
    except KeyboardInterrupt:
        end_time = datetime.now()
        elapsed_time = end_time - start_time
        print("\nProcess interrupted.")
        print_elapsed_time(elapsed_time)

def print_elapsed_time(elapsed_time):
    seconds = elapsed_time.total_seconds()
    years = int(seconds // (365 * 24 * 3600))
    seconds %= (365 * 24 * 3600)
    days = int(seconds // (24 * 3600))
    seconds %= (24 * 3600)
    hours = int(seconds // 3600)
    seconds %= 3600
    minutes = int(seconds // 60)
    seconds = int(seconds % 60)

    print(f"Time taken: {years} years, {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")

def main():
    print("Select an option:")
    print("1. Check hash against a wordlist (default: rockyou.txt)")
    print("2. Brute force hash")
    print("3. Convert a string to its hash")
    option = input("Enter option (1, 2, or 3): ")

    hash_func = None
    if option == '1':
        hash_type = input("Enter hash type (md2, md4): ").strip().lower()
        if hash_type == 'md2':
            hash_func = calculate_md2
        elif hash_type == 'md4':
            hash_func = calculate_md4
        else:
            print("Invalid hash type.")
            return
        
        wordlist_path = input("Enter path to wordlist file (leave blank to use default rockyou.txt): ")
        target_hash = input("Enter hash to crack: ").lower()
        check_hash(hash_func, wordlist_path, target_hash)
    elif option == '2':
        hash_type = input("Enter hash type (md2, md4): ").strip().lower()
        if hash_type == 'md2':
            hash_func = calculate_md2
        elif hash_type == 'md4':
            hash_func = calculate_md4
        else:
            print("Invalid hash type.")
            return
        
        target_hash = input("Enter hash to crack: ").lower()
        min_length = int(input("Enter minimum length of passwords to try: "))
        max_length = int(input("Enter maximum length of passwords to try: "))
        print("Select character set:")
        print("1. Numeric (0-9)")
        print("2. Alphanumeric (0-9, a-z, A-Z)")
        print("3. Alphanumeric with special characters")
        charset_option = input("Enter option (1, 2, or 3): ")

        if charset_option == '1':
            charset = string.digits
        elif charset_option == '2':
            charset = string.ascii_letters + string.digits
        elif charset_option == '3':
            additional_chars = input("Enter additional characters to include: ")
            charset = string.ascii_letters + string.digits + additional_chars
        else:
            print("Invalid option.")
            return

        brute_force_hash(hash_func, target_hash, min_length, max_length, charset)
    elif option == '3':
        string_to_convert = input("Enter the string to convert to hash: ")
        hash_type = input("Enter hash type (md2, md4): ").strip().lower()
        if hash_type == 'md2':
            hash_value = calculate_md2(string_to_convert)
        elif hash_type == 'md4':
            hash_value = calculate_md4(string_to_convert)
        else:
            print("Invalid hash type.")
            return
        
        print(f"Hash value: {hash_value}")
    else:
        print("Invalid option.")

if __name__ == '__main__':
    main()


