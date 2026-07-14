import os
import sys
import urllib.request
import urllib.parse
import json
import time
import random

# DEDSEC TACTICAL TERMINAL COLOR ENGINE
C_RED     = "\033[31m"
C_GREEN = "\033[38;5;28m"
C_YEL     = "\033[33m"
C_WHITE   = "\033[97m"
C_BOLD    = "\033[1m"
C_RESET   = "\033[0m"
C_DGN     = "\033[2;32m"

def print_tactical_banner():
    """Renders the high-density monolithic text logo and sub-metadata headers."""
    print(f"{C_GREEN}{C_BOLD}")
    print("                    ▓█████▄ ▓█████ ▓█████▄ ███▄ ▄███▓ ▄▄▄        ██████  ██ ▄█▀")
    print("                    ▒██▀ ██▌▓█   ▀ ▒██▀ ██▌▓██▒▀█▀ ██▒▒████▄    ▒██    ▒  ██▄█▒")
    print("                    ░██   █▌▒███   ░██   █▌▓██    ▓██░▒██  ▀█▄  ░ ▓██▄   ▓███▄░")
    print("                    ░▓█▄   ▌▒▓█  ▄ ░▓█▄   ▌▒██    ▒██ ░██▄▄▄▄██   ▒   ██▒▓██ █▄")
    print("                    ░▒████▓ ░▒████▒░▒████▓ ▒██▒   ░██▒ ▓█   ▓██▒▒██████▒▒▒██▒ █▄")
    print("                     ▒▒▓  ▒ ░░ ▒░ ░ ▒▒▓  ▒ ░ ▒░   ░  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░▒ ▒▒ ▓▒")
    print("                     ░ ▒  ▒  ░ ░  ░ ░ ▒  ▒ ░  ░      ░  ▒   ▒▒ ░░ ░▒  ░ ░░ ░▒ ▒░")
    print("                     ░ ░  ░    ░    ░ ░  ░ ░      ░     ░   ▒   ░  ░  ░  ░ ░░ ░")
    print("                       ░       ░  ░   ░           ░         ░  ░      ░  ░  ░")
    print("                     ░              ░")
    print(f"{C_YEL}{C_BOLD}                      * [DEDSEC-COMMUNITY  PRESENTS [IG : @dedseccommunity_ ] ]{C_RESET}")
    print(f"{C_RED}{C_BOLD}                      $  [DEVELOPED BY NODE: Unknownx007]{C_RESET}\n")

def get_random_shitty_joke():
    """Returns a random index string from the local database array."""
    jokes_database = [
        "Why do security nodes hate nature? There are too many bugs inside the system partition loops.",
        "A SQL query walks into a server room, approaches two database tables, and asks: 'Can I join you?'",
        "There are 10 types of people in the world: those who understand binary, and those who don't.",
        "Hardware is the part of an installation node that you can kick; software is the part you can only curse at.",
        "An infrastructure administrator has two major problems: 1. Networking drops. 2. Human staff.",
        "Why was the server asset crying? Because it had too many unhandled exceptions inside its runtime core."
    ]
    return random.choice(jokes_database)

def validate_url(url_string):
    """Ensures input matches compliant protocol structures."""
    if not url_string.startswith("http://") and not url_string.startswith("https://"):
        print(f"\n {C_RED}(0_0) [ALERT_CRITICAL]: Invalid URL format specification. Use http:// or https://{C_RESET}")
        sys.exit(1)

def shorten_target_url(destination_url):
    """Contacts external api infrastructure providers or drops back to local handling."""
    print(f" {C_DGN}[* LOG_NODE]:{C_GREEN} (⚙_⚙) Contacting upstream URL shortening API infrastructure parameters...")
    time.sleep(0.6)
    
    api_url = f"https://is.gd{urllib.parse.quote(destination_url)}"
    try:
        req = urllib.request.Request(
            api_url, 
            headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0'}
        )
        with urllib.request.urlopen(req, timeout=4) as response:
            data = json.loads(response.read().decode('utf-8'))
            if "shorturl" in data:
                print(f" {C_DGN}[🛸 LOG_NODE]:{C_GREEN} [ONLINE_MATCH]: External compression token secured via remote API link.")
                return data["shorturl"]
    except Exception:
        pass

    print(f" {C_DGN}[🛸 LOG_NODE]:{C_YEL} [!] External API handshake failed. Activating native local fallback tracking mode.")
    return destination_url

def main():
    os.system("clear")
    print_tactical_banner()
    
    print(f"{C_DGN}☠️ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ☠️{C_RESET}")
    print(f" {C_GREEN}(0_0) {C_BOLD}[TACTICAL PANEL STEP 1]: IDENTIFY DESTINATION LAYER TARGET{C_RESET}")
    phish = input(f" {C_YEL}Input Target URL Link (with http/https):{C_RESET} ").strip()
    validate_url(phish)
    
    # Process link compression routines
    short_link = shorten_target_url(phish)
    shorter = short_link.replace("https://", "").replace("http://", "")
    
    print(f"\n {C_GREEN}(0_0) {C_BOLD}[TACTICAL PANEL STEP 2]: DEFINE FRONT PRETEXTING MASK DOMAIN{C_RESET}")
    print(f" {C_DGN}e.g., https://facebook.com, https://youtube.com, https://google.com{C_RESET}")
    mask = input(f" {C_YEL}Input Mask Domain Link:{C_RESET} ").strip()
    validate_url(mask)
    
    print(f"\n {C_GREEN}(0_0) {C_BOLD}[TACTICAL PANEL STEP 3]: MANIFEST SOCIAL ENGINEERING METADATA{C_RESET}")
    print(f" {C_DGN}Do not use spaces inside variables; insert '-' dashes between text arrays.{C_RESET}")
    words = input(f" {C_YEL}Input Custom Bait Keywords:{C_RESET} ").strip()
    
    # LIVE SIMULATION LOGGING PANEL HUB BLOCK
    print(f"\n{C_DGN}┌── [ LIVE EXPLOIT SUBVERSION PROGRESS RECON LOGS ENGINE ] ──────────────────────────────────────────────────┐")
    print(f"│ {C_GREEN}[⚙ TIMELINE CORE]{C_WHITE} Mapping structural memory boundary frames allocation offsets...              │")
    time.sleep(0.4)
    print(f"│ {C_GREEN}[⚙ TIMELINE CORE]{C_WHITE} Stripping explicit remote server header caches layout profiles...             │")
    time.sleep(0.4)
    print(f"│ {C_GREEN}[⚙ TIMELINE CORE]{C_WHITE} Injecting UserInfo spec delimiter anchors into final protocol string...      │")
    time.sleep(0.5)
    
    if not words or " " in words:
        if " " in words:
            print(f"│ {C_RED}[⚠ WARN_ANOMALY]{C_WHITE} Spaces intercepted. Forcing inline truncation for compliance routines.        │")
        final_url = f"{mask}@{shorter}"
    else:
        clean_words = words.replace(" ", "-")
        final_url = f"{mask}-{clean_words}@{shorter}"
        
    print(f"│ {C_GREEN}[⚙ TIMELINE CORE]{C_WHITE} Exploitation matrix structural compilation pass complete.                    │")
    print(f"{C_DGN}└────────────────━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┘{C_RESET}")
    
    # VERDICT DISPLAY READOUT MODULE
    print(f"\n{C_DGN}☠━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ☠{C_RESET}")
    print(f" {C_GREEN}{C_BOLD}[# WEAPONIZED MASKED LINK COMPILED SUCCESSFULLY]{C_RESET}")
    print(f" {C_YEL}{C_BOLD}{final_url}{C_RESET}")
    print(f"{C_DGN}☠ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ☠{C_RESET}")
    
    # SYSTEM SHITTY JOKE RANDOM TERMINAL BASE PRINTER
    print(f"\n {C_DGN}[$ DEDSEC SYSTEM HUMOR]: \"{get_random_shitty_joke()}\"{C_RESET}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)

