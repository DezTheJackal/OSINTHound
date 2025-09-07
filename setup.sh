#!/bin/bash
set -e

echo "[*] Installing OSINTHound..."

# make script executable
chmod +x osinthound.py

# copy it globally
sudo cp osinthound.py /usr/local/bin/osinthound

echo "[+] OSINTHound installed!"
echo "Usage examples:"
echo "  osinthound consent"
echo "  osinthound user dezthejackal"
echo "  osinthound domain example.com"
echo "  osinthound email test@example.org"
