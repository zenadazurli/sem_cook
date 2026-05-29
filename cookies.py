import subprocess
import time
import re
import sys

API_KEY = "bu_JYnkD1Cb0tJocGEB1HIf4Gn_F-gYqih15YpQWRYyJpY"
EMAIL = "sandrominori50+ulugarecexisa@gmail.com"
PASSWORD = "DDnmVV45!!"

def run_cmd(cmd, capture=False):
    print(f"📌 {cmd[:50]}...", flush=True)
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

# Prima otteniamo lo stato per trovare l'indice corretto
print("📋 Stato della pagina...", flush=True)
run_cmd("browser-use state", capture=False)
time.sleep(2)

# Clicca su "Sign In" (usa l'indice che vedi nello state, di solito 2)
print("🔓 Clicco su Sign In...", flush=True)
run_cmd("browser-use click 2")
time.sleep(3)

# Compila form
print("📝 Compilo form...", flush=True)
run_cmd('browser-use keys "Tab"')
run_cmd(f'browser-use type "{EMAIL}"')
time.sleep(1)

run_cmd('browser-use keys "Tab"')
run_cmd(f'browser-use type "{PASSWORD}"')
time.sleep(1)

# Login
print("🚪 Invio login...", flush=True)
run_cmd('browser-use keys "Enter"')

# Attesa
print("⏳ Attesa login (20 secondi)...", flush=True)
time.sleep(20)

# Verifica URL
result = run_cmd('browser-use eval "window.location.href"', capture=True)
url = result.stdout.strip()
print(f"📍 URL finale: {url}", flush=True)

# Cookie
result = run_cmd("browser-use cookies get", capture=True)
print(result.stdout, flush=True)

# Estrazione
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

print(f"\n========== RISULTATO ==========", flush=True)
print(f"sesids: {sesids if sesids else '❌'}", flush=True)
print(f"user_id: {user_id if user_id else '❌'}", flush=True)
print("=================================", flush=True)
