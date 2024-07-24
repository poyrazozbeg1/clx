#!/usr/bin/env python3

import hashlib
import itertools
import string
from datetime import datetime

def calculate_sha224_with_salt(password, salt):
    if salt:
        salted_password = salt + password
    else:
        salted_password = password
    return hashlib.sha224(salted_password.encode('utf-8')).hexdigest()

def check_sha224(wordlist_path, target_hash, salt):
    if not wordlist_path:
        wordlist_path = "rockyou.txt"
    try:
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as file:
            for line in file:
                password = line.strip()
                sha224_hash = calculate_sha224_with_salt(password, salt)
                print(f"Trying: {password} -> {sha224_hash}")
                if sha224_hash == target_hash:
                    print(f"Password found: {password}")
                    return password
        print("Password not found in wordlist.")
    except FileNotFoundError:
        print(f"Wordlist file {wordlist_path} not found.")

def brute_force_sha224(target_hash, salt, min_length, max_length, charset):
    start_time = datetime.now()
    try:
        for length in range(min_length, max_length + 1):
            for guess in itertools.product(charset, repeat=length):
                guess_str = ''.join(guess)
                sha224_hash = calculate_sha224_with_salt(guess_str, salt)
                print(f"Trying: {guess_str} -> {sha224_hash}")
                if sha224_hash == target_hash:
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

def main_sha224():
    print("SHA-224 Hash Cracker")
    print("1. Check SHA-224 hash against a wordlist")
    print("2. Brute force SHA-224 hash")
    option = input("Enter option (1 or 2): ")

    if option == '1':
        wordlist_path = input("Enter path to wordlist file (leave blank to use default rockyou.txt): ")
        target_hash = input("Enter SHA-224 hash to crack: ").lower()
        salt = input("Enter the salt value (leave blank for no salt): ")
        check_sha224(wordlist_path, target_hash, salt)
    elif option == '2':
        target_hash = input("Enter SHA-224 hash to crack: ").lower()
        salt = input("Enter the salt value (leave blank for no salt): ")
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

        brute_force_sha224(target_hash, salt, min_length, max_length, charset)
    else:
        print("Invalid option.")

if __name__ == '__main__':
    main_sha224()
