#!/bin/bash
set -e

echo "════════════════════════════════════════"
echo "  🐺 OSINTHound Installation Script"
echo "════════════════════════════════════════"
echo ""

# Check for Python 3
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    echo "   Please install Python 3 and try again."
    exit 1
fi

echo "✓ Python 3 found: $(python3 --version)"

# Make script executable
chmod +x osinthound.py
echo "✓ Made osinthound.py executable"

# Install globally (with sudo) or locally
if [ "$EUID" -eq 0 ]; then
    # Running as root
    cp osinthound.py /usr/local/bin/osinthound
    echo "✓ Installed to /usr/local/bin/osinthound"
else
    # Not root - try with sudo
    echo ""
    echo "Installing to /usr/local/bin/ (requires sudo)..."
    if sudo cp osinthound.py /usr/local/bin/osinthound 2>/dev/null; then
        echo "✓ Installed to /usr/local/bin/osinthound"
    else
        # Sudo failed, install locally
        echo "⚠️  Sudo not available. Installing to ~/.local/bin/"
        mkdir -p ~/.local/bin
        cp osinthound.py ~/.local/bin/osinthound
        echo "✓ Installed to ~/.local/bin/osinthound"
        
        # Check if ~/.local/bin is in PATH
        if [[ ":$PATH:" != *":$HOME/.local/bin:"* ]]; then
            echo ""
            echo "⚠️  Add ~/.local/bin to your PATH by adding this to ~/.bashrc or ~/.zshrc:"
            echo "   export PATH=\"\$HOME/.local/bin:\$PATH\""
        fi
    fi
fi

echo ""
echo "════════════════════════════════════════"
echo "  ✅ Installation Complete!"
echo "════════════════════════════════════════"
echo ""
echo "Quick Start:"
echo "  osinthound -h                    # Show help"
echo "  osinthound -u dezthejackal       # Check username"
echo "  osinthound -d example.com        # Check domain"
echo "  osinthound -e test@example.org   # Check email"
echo ""
echo "First run will prompt for consent."
echo ""
