# OSINTHound
🐺 OSINTHound – Lightweight Python OSINT Recon Tool  OSINTHound is a fast, dependency-free Open-Source Intelligence (OSINT) reconnaissance tool written in Python 3. It’s designed to help cybersecurity students, researchers, and ethical hackers gather basic intelligence on usernames, domains, and emails — all without requiring external APIs 

# 🐺 OSINTHound
A lightweight, dependency-free Python 3 OSINT reconnaissance tool.

# 🐺 OSINTHound

<div align="center">

![Version](https://img.shields.io/badge/version-1.1-blue.svg)
![Python](https://img.shields.io/badge/python-3.6+-green.svg)
![License](https://img.shields.io/badge/license-MIT-orange.svg)
![Platform](https://img.shields.io/badge/platform-linux%20%7C%20macos%20%7C%20windows-lightgrey.svg)

**A lightweight, dependency-free Python 3 OSINT reconnaissance tool**

*Fast • Simple • Ethical*

</div>

---

## 📋 Table of Contents

- [About](#-about)
- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Examples](#-examples)
- [Command Reference](#-command-reference)
- [Output Explanation](#-output-explanation)
- [Legal & Ethics](#-legal--ethics)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 About

OSINTHound is a fast, lightweight Open-Source Intelligence (OSINT) reconnaissance tool designed for:

- 🔐 **Cybersecurity Students** - Learn OSINT techniques
- 🕵️ **Security Researchers** - Quick reconnaissance scans
- 👨‍💻 **Ethical Hackers** - Authorized penetration testing
- 📊 **Digital Investigators** - Open-source intelligence gathering

**No external dependencies required** - uses only Python's standard library!

---

## ✨ Features

### 🔍 Username Reconnaissance
- Search across 6+ major platforms simultaneously
- Platforms: GitHub, Reddit, Twitter/X, Instagram, Medium, LinkedIn
- Quick profile discovery
- Summary statistics

### 🌐 Domain Intelligence
- DNS resolution (A records)
- Reverse DNS lookups
- HTTPS banner grabbing
- Server identification
- Port scanning (common ports)
- Web server detection

### 📧 Email Analysis
- Email format validation (RFC compliance)
- Domain existence verification
- Mail server (MX) detection
- Domain resolution checks

### 🛡️ Security Features
- Built-in ethical use consent system
- Legal disclaimer enforcement
- Safe, read-only operations
- No invasive testing

---

## 🚀 Installation

### Prerequisites
- Python 3.6 or higher
- Internet connection
- Terminal/Command prompt access

### Quick Install

**Linux/macOS:**
```bash
git clone https://github.com/DezTheJackal/osinthound.git
cd osinthound
chmod +x setup.sh
./setup.sh
```

**Windows:**
```bash
git clone https://github.com/DezTheJackal/osinthound.git
cd osinthound
python osinthound.py -h
```

### Manual Install

```bash
# Download the script
wget https://raw.githubusercontent.com/DezTheJackal/osinthound/main/osinthound.py

# Make executable
chmod +x osinthound.py

# Move to PATH (optional)
sudo mv osinthound.py /usr/local/bin/osinthound
```

### Verify Installation

```bash
osinthound --version
# Output: OSINTHound 1.1
```

---

## 📖 Usage

### First Run - Consent

On your first use, OSINTHound will ask for consent:

```bash
osinthound -u testuser
```

You'll see:
```
⚠️  LEGAL & ETHICAL NOTICE ⚠️

OSINTHound performs open-source intelligence lookups.
Only use on assets you own or have explicit permission to test.

By continuing, you confirm:
✓ You will use this tool legally and ethically
✓ You have permission to investigate the targets
✓ You understand unauthorized access is illegal

Do you accept these terms? (yes/no):
```

Type `yes` to proceed. Consent is saved locally and won't be asked again.

### Basic Commands

```bash
# Show help
osinthound -h

# Username search
osinthound -u <username>

# Domain intelligence
osinthound -d <domain>

# Email validation
osinthound -e <email>

# Reset consent
osinthound --reset-consent

# Show version
osinthound --version
```

---

## 💡 Examples

### Example 1: Username Search

```bash
osinthound -u dezthejackal
```

**Output:**
```
╔═══════════════════════════════════════╗
║       🐺 OSINTHound v1.1           ║
║   Lightweight OSINT Recon Tool        ║
╚═══════════════════════════════════════╝

🔍 Username Reconnaissance: 'dezthejackal'
==================================================
  ✅ GitHub          FOUND → https://github.com/dezthejackal
  ❌ Reddit          Not found
  ✅ Twitter/X       FOUND → https://x.com/dezthejackal
  ❌ Instagram       Not found
  ✅ Medium          FOUND → https://medium.com/@dezthejackal
  ❌ LinkedIn        Not found

📊 Summary: Found 3/6 profiles

==================================================
✅ Scan complete!
```

### Example 2: Domain Intelligence

```bash
osinthound -d example.com
```

**Output:**
```
╔═══════════════════════════════════════╗
║       🐺 OSINTHound v1.1           ║
║   Lightweight OSINT Recon Tool        ║
╚═══════════════════════════════════════╝

🌐 Domain Intelligence: 'example.com'
==================================================
  📍 IP Address(es): 93.184.216.34
  🔄 Reverse DNS: example.com
  🌍 HTTPS Status: 200 OK
  💻 Server: ECS (dcb/7F83)

  🔌 Port Scan (common ports):
     ✅ Port    80 OPEN
     ✅ Port   443 OPEN

==================================================
✅ Scan complete!
```

### Example 3: Email Validation

```bash
osinthound -e contact@example.com
```

**Output:**
```
╔═══════════════════════════════════════╗
║       🐺 OSINTHound v1.1           ║
║   Lightweight OSINT Recon Tool        ║
╚═══════════════════════════════════════╝

📧 Email Analysis: 'contact@example.com'
==================================================
  ✅ Email format is valid
  📍 Domain: example.com
  ✅ Domain exists and resolves
  📬 Mail server appears configured

==================================================
✅ Scan complete!
```

### Example 4: Batch Investigation

```bash
# Investigate a target comprehensively
osinthound -u johndoe
osinthound -d johndoe.com
osinthound -e john@johndoe.com
```

---

## 📚 Command Reference

### Username Search (`-u`, `--username`)

**Syntax:**
```bash
osinthound -u <username>
osinthound --username <username>
```

**What it does:**
- Checks if username exists on 6+ platforms
- Shows direct links to found profiles
- Non-invasive (just checks if pages exist)

**Platforms checked:**
- GitHub (developer profiles)
- Reddit (user accounts)
- Twitter/X (social media)
- Instagram (photo sharing)
- Medium (blogging)
- LinkedIn (professional network)

**Use cases:**
- Finding social media presence
- Locating developer profiles
- Digital footprint analysis
- Account enumeration research

---

### Domain Intelligence (`-d`, `--domain`)

**Syntax:**
```bash
osinthound -d <domain.com>
osinthound --domain <domain.com>
```

**What it does:**
- Resolves domain to IP addresses
- Performs reverse DNS lookup
- Checks HTTPS configuration
- Identifies web server software
- Scans common ports

**Information gathered:**
- DNS A records (IPv4 addresses)
- Reverse DNS hostname
- HTTP/HTTPS status codes
- Server headers (nginx, Apache, etc.)
- Open ports (80, 443, 22, 21, 25, 3306, 8080)

**Use cases:**
- Website reconnaissance
- Infrastructure mapping
- Server identification
- Basic security assessment

---

### Email Analysis (`-e`, `--email`)

**Syntax:**
```bash
osinthound -e <email@domain.com>
osinthound --email <email@domain.com>
```

**What it does:**
- Validates email format (RFC compliant)
- Checks if domain exists
- Verifies DNS resolution
- Tests mail server configuration

**Checks performed:**
- Regex pattern validation
- Domain DNS resolution
- MX record existence (port 25)

**Use cases:**
- Email verification
- Domain validation
- Contact information research
- Phishing investigation prep

---

### Additional Options

**Show Help:**
```bash
osinthound -h
osinthound --help
```

**Show Version:**
```bash
osinthound -v
osinthound --version
```

**Reset Consent:**
```bash
osinthound --reset-consent
```
Use this if you need to review the legal notice again or reset consent for another user.

---

## 🔍 Output Explanation

### Status Indicators

| Icon | Meaning |
|------|---------|
| ✅ | Success / Found / Valid |
| ❌ | Not found / Failed / Invalid |
| ⚠️ | Warning / Partial success |
| 🔍 | Scanning / Searching |
| 📊 | Summary / Statistics |
| 📍 | Location / Address info |
| 🌐 | Web / HTTP related |
| 💻 | Server / Technical info |
| 🔌 | Port / Network info |
| 📧 | Email related |
| 📬 | Mail server info |

### Understanding Results

**Username Search Results:**
- `FOUND` = Profile exists and is publicly accessible
- `Not found` = No profile exists or is private/deleted
- `HTTP XXX` = Server returned an error code

**Domain Intelligence:**
- Multiple IPs = Load balancing or CDN
- `Reverse DNS` = Server's hostname
- `Server` header = Web server software version
- `OPEN` ports = Services listening on that port

**Email Analysis:**
- `Valid format` = Follows email syntax rules
- `Domain exists` = Domain has DNS records
- `Mail server configured` = Can receive emails

---

## 🛡️ Legal & Ethics

### ⚖️ Legal Disclaimer

**YOU MUST ONLY USE THIS TOOL:**
- ✅ On systems you own
- ✅ With explicit written permission
- ✅ For authorized security assessments
- ✅ For educational purposes on public data
- ✅ In compliance with local laws

**NEVER USE THIS TOOL FOR:**
- ❌ Unauthorized access attempts
- ❌ Harassment or stalking
- ❌ Illegal surveillance
- ❌ Privacy violations
- ❌ Any malicious purposes

### 🎓 Ethical Guidelines

1. **Permission First** - Always get authorization
2. **Public Data Only** - Don't attempt to access private info
3. **Respect Privacy** - Don't use findings to harm others
4. **Report Responsibly** - Follow responsible disclosure
5. **Stay Legal** - Know your local laws

### 🚨 Consequences of Misuse

Unauthorized use of reconnaissance tools may violate:
- Computer Fraud and Abuse Act (CFAA) - USA
- Computer Misuse Act - UK
- Similar laws in your jurisdiction

**Penalties may include:**
- Criminal prosecution
- Fines
- Imprisonment
- Civil liability

**The authors and contributors are not responsible for misuse.**

---

## 🔧 Troubleshooting

### Common Issues

**Issue: "Command not found"**
```bash
# Solution 1: Use full path
python3 osinthound.py -u testuser

# Solution 2: Add to PATH (Linux/Mac)
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

# Solution 3: Run from current directory
./osinthound.py -u testuser
```

**Issue: "Permission denied"**
```bash
# Make executable
chmod +x osinthound.py
```

**Issue: Timeouts or connection errors**
- Check your internet connection
- Some sites may block automated requests
- Try again with a VPN if in restricted region
- Increase timeout in code if needed

**Issue: No results for username**
- Username may not exist on those platforms
- Account may be private or deleted
- Rate limiting by the website
- Try different capitalization

**Issue: Domain not resolving**
- Check domain spelling
- Domain may not exist
- DNS issues (try `nslookup domain.com`)
- Firewall blocking DNS requests

**Issue: Python version error**
```bash
# Check version
python3 --version

# Upgrade if needed (Linux)
sudo apt update && sudo apt install python3

# macOS
brew install python3
```

---

## 📊 Advanced Usage

### Scripting with OSINTHound

**Bash script to check multiple targets:**
```bash
#!/bin/bash
# multi-check.sh

echo "Running OSINT on multiple targets..."

# List of usernames
usernames=("user1" "user2" "user3")

for user in "${usernames[@]}"; do
    echo "Checking: $user"
    osinthound -u "$user" >> results.txt
    echo "---" >> results.txt
done

echo "Results saved to results.txt"
```

**Python wrapper:**
```python
import subprocess
import json

def check_username(username):
    result = subprocess.run(
        ['osinthound', '-u', username],
        capture_output=True,
        text=True
    )
    return result.stdout

# Use it
output = check_username("testuser")
print(output)
```

### Output Redirection

```bash
# Save to file
osinthound -u testuser > results.txt

# Append to file
osinthound -d example.com >> scan_log.txt

# Save errors separately
osinthound -e test@example.com 2> errors.log

# Save everything
osinthound -u testuser &> complete_log.txt
```

### Automated Scanning

```bash
# Cron job (daily scan)
# Add to crontab: crontab -e
0 2 * * * /usr/local/bin/osinthound -d mysite.com >> /var/log/osint.log
```

---

## 🤝 Contributing

We welcome contributions! Here's how:

### Reporting Bugs

1. Check existing issues
2. Create detailed bug report including:
   - OS and Python version
   - Command you ran
   - Expected vs actual behavior
   - Error messages

### Suggesting Features

- Open an issue with `[Feature Request]` tag
- Describe the feature and use case
- Explain why it would be useful

### Code Contributions

```bash
# Fork the repository
# Clone your fork
git clone https://github.com/YOUR-USERNAME/osinthound.git

# Create feature branch
git checkout -b feature-name

# Make changes
# Test thoroughly

# Commit with clear message
git commit -m "Add: feature description"

# Push and create pull request
git push origin feature-name
```

### Coding Standards

- Follow PEP 8 style guide
- Add docstrings to functions
- Include error handling
- Test on multiple platforms
- Update README if needed

---

## 🗺️ Roadmap

**Version 1.2 (Planned)**
- [ ] More social platforms
- [ ] JSON output format
- [ ] Colored terminal output
- [ ] Configuration file support
- [ ] Batch processing mode

**Version 2.0 (Future)**
- [ ] API integration (optional)
- [ ] Database storage
- [ ] Web interface
- [ ] Report generation
- [ ] Plugin system

---

## 📄 License

```
MIT License

Copyright (c) 2025 DezTheJackal

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 🔗 Resources

**OSINT Learning:**
- [OSINT Framework](https://osintframework.com/) - Comprehensive OSINT tools collection
- [IntelTechniques](https://inteltechniques.com/) - OSINT training and resources
- [Bellingcat's Guide](https://www.bellingcat.com/category/resources/how-tos/) - Open-source investigations

**Security Standards:**
- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)

**Ethical Hacking:**
- [EC-Council Code of Ethics](https://www.eccouncil.org/code-of-ethics/)
- [Bug Bounty Programs](https://www.bugcrowd.com/)

---

## 👤 Author

**DezTheJackal**

- GitHub: [@DezTheJackal](https://github.com/DezTheJackal)
- Email: Contact via GitHub

---

## 🙏 Acknowledgments

- Python Software Foundation
- OSINT community
- Security researchers worldwide
- All contributors

---

## ⭐ Support

If you find OSINTHound useful:
- ⭐ Star the repository
- 🐛 Report bugs
- 💡 Suggest features
- 📢 Share with others
- 🤝 Contribute code

---

<div align="center">

**Made with 🐺 for the cybersecurity community**

*Stay ethical. Stay legal. Stay curious.*

</div>
