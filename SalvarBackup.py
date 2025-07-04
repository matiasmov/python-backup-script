import requests
import os
from config_manager import PATH, API_BASE_URL, AUTH_TOKEN

url_list_backup = f"{API_BASE_URL}/api/v1/settings/backups"

headers = {
    "Authorization": f"Bearer {AUTH_TOKEN}",
    "Accept": "application/zip, application/json"
}

# lista de backups
response_list = requests.get(url_list_backup, headers=headers)
data = response_list.json()

# ORDENA (mais recente primeiro)
sorted_backups = sorted(data["rows"], key=lambda x: x["modified_value"], reverse=True)

# Pegando o mais recente
latest_backup = sorted_backups[0]
filename = latest_backup["filename"]
url = f"http://10.1.0.251:8081/api/v1/settings/backups/download/{filename}"
full_path = os.path.join(PATH, filename)

# Baixando o backup escolhido acima
response = requests.get(url, headers=headers, stream=True)
with open(full_path, "wb") as f:
    for chunk in response.iter_content(chunk_size=8192):
        if chunk:
            f.write(chunk)

print("Backup salvo em:", full_path)
