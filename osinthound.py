#!/usr/bin/env python3
"""
OSINTHound - Lightweight OSINT Reconnaissance Tool
MIT License - Copyright (c) 2025 DezTheJackal
"""

import re
import sys
import socket
import ssl
import http.client
from urllib import request, error
from datetime import datetime
import argparse

CONSENT_FILE = ".osinthound_consent"
VERSION = "1.1"

# ============ Banner ============
def print_banner():
    print("""
╔═══════════════════════════════════════╗
║       🐺 OSINTHound v{}              ║
║   Lightweight OSINT Recon Tool 
║   Dev: DezTheJackal
╚═══════════════════════════════════════╝
    """.format(VERSION))

# ============ Consent Management ============
def check_consent():
    """Check if user has given consent"""
    try:
        with open(CONSENT_FILE, "r") as f:
            return "ack" in f.read()
    except FileNotFoundError:
        return False

def show_consent_prompt():
    """Show consent prompt and handle user response"""
    print("""
⚠️  LEGAL & ETHICAL NOTICE ⚠️

OSINTHound performs open-source intelligence lookups.
Only use on assets you own or have explicit permission to test.

By continuing, you confirm:
✓ You will use this tool legally and ethically
✓ You have permission to investigate the targets
✓ You understand unauthorized access is illegal

Do you accept these terms? (yes/no): """, end="")
    
    response = input().strip().lower()
    if response in ['yes', 'y']:
        with open(CONSENT_FILE, "w") as f:
            f.write(f"ack:{datetime.utcnow().isoformat()}\n")
        print("\n✅ Consent recorded. You can now use OSINTHound.\n")
        return True
    else:
        print("\n❌ Consent required to use OSINTHound. Exiting.\n")
        return False

def require_consent():
    """Ensure user has given consent before proceeding"""
    if not check_consent():
        return show_consent_prompt()
    return True

# ============ Username Reconnaissance ============
SITES = {
    "GitHub": "https://github.com/{username}",
    "Reddit": "https://www.reddit.com/user/{username}",
    "Twitter/X": "https://x.com/{username}",
    "Instagram": "https://www.instagram.com/{username}/",
    "Medium": "https://medium.com/@{username}",
    "LinkedIn": "https://www.linkedin.com/in/{username}",
}

def check_username(username):
    """Check username across multiple platforms"""
    print(f"\n🔍 Username Reconnaissance: '{username}'")
    print("=" * 50)
    
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    found_count = 0
    
    for site, url_template in SITES.items():
        url = url_template.format(username=username)
        req = request.Request(url, headers=headers)
        
        try:
            with request.urlopen(req, timeout=8) as resp:
                if resp.status == 200:
                    print(f"  ✅ {site:15} FOUND → {url}")
                    found_count += 1
        except error.HTTPError as e:
            if e.code == 404:
                print(f"  ❌ {site:15} Not found")
            else:
                print(f"  ⚠️  {site:15} HTTP {e.code}")
        except Exception as e:
            print(f"  ⚠️  {site:15} Error: {str(e)[:30]}")
    
    print(f"\n📊 Summary: Found {found_count}/{len(SITES)} profiles")

# ============ Domain Intelligence ============
def domain_info(domain):
    """Gather basic intelligence on a domain"""
    print(f"\n🌐 Domain Intelligence: '{domain}'")
    print("=" * 50)
    
    # DNS Lookup
    try:
        ip_list = socket.gethostbyname_ex(domain)[2]
        print(f"  📍 IP Address(es): {', '.join(ip_list)}")
        
        # Reverse DNS
        try:
            hostname = socket.gethostbyaddr(ip_list[0])[0]
            print(f"  🔄 Reverse DNS: {hostname}")
        except:
            pass
    except Exception as e:
        print(f"  ❌ DNS lookup failed: {e}")
        return

    # HTTPS Banner Grab
    try:
        ctx = ssl.create_default_context()
        conn = http.client.HTTPSConnection(domain, 443, context=ctx, timeout=8)
        conn.request("HEAD", "/")
        resp = conn.getresponse()
        
        print(f"  🌍 HTTPS Status: {resp.status} {resp.reason}")
        
        server = resp.getheader("Server")
        if server:
            print(f"  💻 Server: {server}")
        
        powered_by = resp.getheader("X-Powered-By")
        if powered_by:
            print(f"  ⚡ Powered By: {powered_by}")
        
        conn.close()
    except Exception as e:
        print(f"  ⚠️  HTTPS check failed: {e}")

    # Port Check (common ports)
    print("\n  🔌 Port Scan (common ports):")
    common_ports = [80, 443, 22, 21, 25, 3306, 8080]
    for port in common_ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            result = sock.connect_ex((domain, port))
            if result == 0:
                print(f"     ✅ Port {port:5} OPEN")
            sock.close()
        except:
            pass

# ============ Email Validation ============
EMAIL_RE = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$")

def check_email(email):
    """Validate email format and check domain"""
    print(f"\n📧 Email Analysis: '{email}'")
    print("=" * 50)
    
    # Format validation
    if EMAIL_RE.match(email):
        print("  ✅ Email format is valid")
        
        # Extract domain
        domain = email.split('@')[1]
        print(f"  📍 Domain: {domain}")
        
        # Check if domain resolves
        try:
            mx_records = socket.getaddrinfo(domain, None)
            print(f"  ✅ Domain exists and resolves")
        except:
            print(f"  ⚠️  Warning: Domain may not exist or resolve")
        
        # MX Record check
        try:
            answers = socket.getaddrinfo(domain, 25)
            print(f"  📬 Mail server appears configured")
        except:
            print(f"  ⚠️  No mail server detected")
    else:
        print("  ❌ Invalid email format")

# ============ Main CLI ============
def main():
    parser = argparse.ArgumentParser(
        description="🐺 OSINTHound - Lightweight OSINT Reconnaissance Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  osinthound -u dezthejackal          # Check username
  osinthound -d example.com           # Domain intel
  osinthound -e test@example.org      # Email check
  osinthound --reset-consent          # Reset consent
        """
    )
    
    parser.add_argument('-u', '--username', help='Check username across platforms')
    parser.add_argument('-d', '--domain', help='Gather domain intelligence')
    parser.add_argument('-e', '--email', help='Validate and analyze email')
    parser.add_argument('--reset-consent', action='store_true', help='Reset consent acknowledgment')
    parser.add_argument('-v', '--version', action='version', version=f'OSINTHound {VERSION}')
    
    # If no arguments, show banner and help
    if len(sys.argv) == 1:
        print_banner()
        parser.print_help()
        sys.exit(0)
    
    args = parser.parse_args()
    
    # Handle consent reset
    if args.reset_consent:
        try:
            import os
            os.remove(CONSENT_FILE)
            print("✅ Consent reset. You'll be prompted again on next use.")
        except FileNotFoundError:
            print("ℹ️  No consent file found.")
        sys.exit(0)
    
    # Require consent for all operations
    if not require_consent():
        sys.exit(1)
    
    print_banner()
    
    # Execute requested operation
    if args.username:
        check_username(args.username)
    elif args.domain:
        domain_info(args.domain)
    elif args.email:
        check_email(args.email)
    else:
        print("⚠️  Please specify an operation. Use -h for help.")
        sys.exit(1)
    
    print("\n" + "=" * 50)
    print("✅ Scan complete!\n")

if __name__ == "__main__":
    main()
