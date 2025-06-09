import os
import base64
import json
import requests

TOKEN = os.environ.get('GITHUB_TOKEN')
if not TOKEN:
    raise SystemExit("GITHUB_TOKEN environment variable not set")

REPO = "FortiTest999/Test"
FILE_PATH = "data/result.json"
API_URL = f"https://api.github.com/repos/{REPO}/contents/{FILE_PATH}"

headers = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github+json",
}

# Get the current file SHA
sha_resp = requests.get(API_URL, headers=headers)
sha_resp.raise_for_status()
current_sha = sha_resp.json().get("sha")

# Prepare new JSON payload
payload = {
    "ha_match": True,
    "license_match": False,
    "timestamp": "2025-06-08T20:00:00Z"
}
encoded_content = base64.b64encode(json.dumps(payload).encode()).decode()

update_data = {
    "message": "Update health check result",
    "content": encoded_content,
    "sha": current_sha
}

update_resp = requests.put(API_URL, headers=headers, json=update_data)
print(update_resp.status_code, update_resp.reason)
