#!/bin/bash

# Termux'ta Python kurulumu
echo "Installing Python..."
pkg install -y python
pkg install -y wget
pip install pycryptodome

# Wordlist dosyasının URL'den indirilmesi
cd prodoc
echo "Downloading the wordlist from github"
curl -L -o rockyou.txt https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt



# Depoyu klonlama veya güncelleme (kullanıcının zaten klonladığı varsayılır)
# echo "Cloning or updating the repository..."
# git clone https://github.com/kullaniciadi/md5-checker.git || (cd md5-checker && git pull)

# Python scriptine çalıştırma izni verme
echo "Setting execute permission for the Python script..."
chmod a+x clx.py
cd ..

# Run dosyasına çalıştırma izni verme
echo "Setting execute permission for the run script..."
chmod +x run.sh

# Python programını çalıştırma
echo "Running the Python script..."
./run.sh


