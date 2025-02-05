import os
import hashlib
import time
import json
import requests
from datetime import datetime

api = open('api-key.txt','r').read()
mail = open('mail-id.txt','r').read()
uname = open('username.txt','r').read()
FOLDER_TO_MONITOR = "/home/pavin/Panda/Python/Text"
HASH_STORAGE_FILE = "file_hashes.json"
JIRA_URL = f"https://{uname}.atlassian.net/rest/api/2/issue/"
JIRA_AUTH = (mail, api)
JIRA_PROJECT_KEY = "KAN"
JIRA_ISSUE_TYPE = "Task"
CHECK_INTERVAL = 15 


def calculate_file_hash(file_path):
    """Calculate the SHA256 hash of a given file."""
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(8192):
                sha256.update(chunk)
        return sha256.hexdigest()
    except Exception as e:
        print(f"Error calculating hash for {file_path}: {e}")
        return None


def load_stored_hashes():
    """Load stored file hashes from a JSON file."""
    if os.path.exists(HASH_STORAGE_FILE):
        with open(HASH_STORAGE_FILE, "r") as f:
            return json.load(f)
    return {}


def save_hashes(hashes):
    """Save file hashes to a JSON file."""
    with open(HASH_STORAGE_FILE, "w") as f:
        json.dump(hashes, f, indent=4)


def create_jira_ticket(file_path):
    """Create a Jira ticket for detected file integrity changes."""
    issue_data = {
        "fields": {
            "project": {"key": JIRA_PROJECT_KEY},
            "summary": f"File Integrity Alert: {os.path.basename(file_path)}",
            "description": f"File integrity change detected for {file_path} on {datetime.now()}",
            "issuetype": {"name": JIRA_ISSUE_TYPE},
        }
    }
    response = requests.post(JIRA_URL, json=issue_data, auth=JIRA_AUTH, headers={"Content-Type": "application/json"})
    if response.status_code == 201:
        print(f"Jira ticket created successfully for {file_path}.")
    else:
        print(f"Failed to create Jira ticket: {response.text}")


def monitor_files():
    """Monitor files for integrity changes."""
    stored_hashes = load_stored_hashes()
    current_hashes = {}
    
    for root, _, files in os.walk(FOLDER_TO_MONITOR):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_file_hash(file_path)
            if file_hash:
                current_hashes[file_path] = file_hash

                # Compare with stored hash values
                if file_path in stored_hashes and stored_hashes[file_path] != file_hash:
                    print(f"File integrity issue detected: {file_path}")
                    create_jira_ticket(file_path)
                else:
                    print(f"{file_path} is safe!")

    save_hashes(current_hashes)

if __name__ == "__main__":
    while True:
        print("Monitoring folder for file integrity changes...")
        monitor_files()
        print(f"Next check in {CHECK_INTERVAL} seconds...")
        time.sleep(CHECK_INTERVAL)
