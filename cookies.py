import subprocess
import time
import re
import sys

API_KEY = "bu_JYnkD1Cb0tJocGEB1HIf4Gn_F-gYqih15YpQWRYyJpY"
EMAIL = "sandrominori50+ulugarecexisa@gmail.com"
PASSWORD = "DDnmVV45!!"

def run_cmd(cmd, capture=False):
    if capture:
        return subprocess.run(cmd, shell=True, capture_output=True, text=True)
    else:
        subprocess.run(cmd, shell=True)

print("🚀 Login EasyHits4U", flush=True)

run_cmd("browser-use close --all")
time.sleep(2)

run_cmd(f"browser-use config set api_key {API_KEY}")
run_cmd("browser-use cloud connect")
run_cmd("browser-use open https://www.easyhits4u.com/logon/")
time.sleep(5)

# Invece di eval, usiamo state per vedere l'URL
print("📋 Stato pagina...", flush=True)
run_cmd("browser-use state")
time.sleep(2)

# Clicca Sign In (indice 2)
print("🔓 Clicco su Sign In...", flush=True)
run_cmd("browser-use click 2")
time.sleep(3)

# Compila form
run_cmd('browser-use keys "Tab"')
run_cmd(f'browser-use type "{EMAIL}"')
time.sleep(1)

run_cmd('browser-use keys "Tab"')
run_cmd(f'browser-use type "{PASSWORD}"')
time.sleep(1)

# Login
run_cmd('browser-use keys "Enter"')
time.sleep(20)

# Invece di eval, usiamo state per vedere l'URL finale
print("\n📋 Stato finale...", flush=True)
run_cmd("browser-use state")
time.sleep(2)

# Cookie
result = run_cmd("browser-use cookies get", capture=True)
print(result.stdout, flush=True)

# Estrai sesids e user_id
sesids = None
user_id = None
for line in result.stdout.split('\n'):
    if "'sesids':" in line:
        match = re.search(r"'sesids': '([^']+)'", line)
        if match:
            sesids = match.group(1)
    if "'user_id':" in line:
        match = re.search(r"'user_id': '([^']+)'", line)
        if match:
            user_id = match.group(1)

print(f"\nsesids: {sesids}")
print(f"user_id: {user_id}")
