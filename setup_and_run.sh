#!/bin/bash

# Termux'ta Python kurulumu
echo "Installing Python..."
pkg install -y python

# Depoyu klonlama veya güncelleme (kullanıcının zaten klonladığı varsayılır)
# echo "Cloning or updating the repository..."
# git clone https://github.com/kullaniciadi/md5-checker.git || (cd md5-checker && git pull)

# Python scriptine çalıştırma izni verme
echo "Setting execute permission for the Python script..."
chmod +x md5_checker.py

# Python programını çalıştırma
echo "Running the Python script..."
./md5_checker.py
