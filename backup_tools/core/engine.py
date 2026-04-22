import requests
import os

from backup_tools.config_manager import (
    PATH, API_BASE_URL, AUTH_TOKEN
)

def list_backups():

    url = f"{API_BASE_URL}settings/backups"

    headers ={
        "accept": "application/json",
        "Authorization": f"Bearer {AUTH_TOKEN}",
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    data = response.json()
    dataCode = response.status_code

    if response.ok:
        dataCode = "Sucesso"

    sorted_backups = sorted(data["rows"], key=lambda x: x["modified_value"], reverse=True)

    if not sorted_backups:
        raise ValueError("No backups found available for download.")

    latest_backup = sorted_backups[0]
    filename = latest_backup["filename"]

    download_backups(filename)
    
    return filename, dataCode

## DOWNLOAD

def download_backups(filename):
    url = f"http://10.1.0.251:8081/api/v1/settings/backups/download/{filename}"

    if not os.path.exists(PATH):
        os.makedirs(PATH)

    full_path = os.path.join(PATH, filename)

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {AUTH_TOKEN}",
        "Accept": "application/json"
    }

    print(f"starting download and save: {full_path}")

    response_download = requests.get(url, headers=headers, stream=True)

    with open(full_path, "wb") as f:
        for chunk in response_download.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

    print("Download finish!")

    return full_path

if __name__ == "__main__":
    print("starting test")
    list_backups()