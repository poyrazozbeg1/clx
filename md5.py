#!/usr/bin/env python3

import hashlib
import itertools
import string
import time
from datetime import datetime, timedelta

def calculate_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

def check_md5(wordlist_path, target_hash):
    if not wordlist_path:
        wordlist_path = "rockyou.txt"
    try:
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as file:
            for line in file:
                password = line.strip()
                md5_hash = calculate_md5(password)
                print(f"Trying: {password} -> {md5_hash}")
                if md5_hash == target_hash:
                    print(f"Password found: {password}")
                    return password
        print("Password not found in wordlist.")
    except FileNotFoundError:
        print(f"Wordlist file {wordlist_path} not found.")

def brute_force_md5(target_hash, min_length, max_length, charset):
    start_time = datetime.now()
    try:
        for length in range(min_length, max_length + 1):
            for guess in itertools.product(charset, repeat=length):
                guess_str = ''.join(guess)
                md5_hash = calculate_md5(guess_str)
                print(f"Trying: {guess_str} -> {md5_hash}")
                if md5_hash == target_hash:
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
    print("1. Check MD5 hash against a wordlist (default: rockyou.txt)")
    print("2. Brute force MD5 hash")
    print("3. Convert a string to its MD5 hash")
    option = input("Enter option (1, 2, or 3): ")

    if option == '1':
        wordlist_path = input("Enter path to wordlist file (leave blank to use default rockyou.txt): ")
        target_hash = input("Enter MD5 hash to crack: ")
        check_md5(wordlist_path, target_hash)
    elif option == '2':
        target_hash = input("Enter MD5 hash to crack: ")
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

        brute_force_md5(target_hash, min_length, max_length, charset)
    elif option == '3':
        string_to_convert = input("Enter the string to convert to MD5: ")
        md5_hash = calculate_md5(string_to_convert)
        print(f"MD5 hash: {md5_hash}")
    else:
        print("Invalid option.")

if __name__ == '__main__':
    main()
