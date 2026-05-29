import subprocess
import time
import re

API_KEY = "bu_0Jdyt448rCJtpAZGBl6u5xolw1GD19lb4-KVqASjWs4"
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

run_cmd('browser-use keys "Tab"')
run_cmd(f'browser-use type "{EMAIL}"')
time.sleep(1)

run_cmd('browser-use keys "Tab"')
run_cmd(f'browser-use type "{PASSWORD}"')
time.sleep(1)

run_cmd('browser-use keys "Enter"')
time.sleep(10)

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

print(f"\nsesids: {sesids}")
print(f"user_id: {user_id}")
