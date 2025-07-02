import requests
import os
from dotenv import load_dotenv

load_dotenv() # carregando env

path = os.getenv("BACKUP_PATH")
api_base_url = os.getenv("API_BASE_URL")
auth_token = os.getenv("AUTH_TOKEN")

url_list_backup = f"{api_base_url}/api/v1/settings/backups"

headers = {
    "Authorization": f"Bearer {auth_token}",
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
full_path = os.path.join(path, filename)

# Baixando o backup escolhido acima
response = requests.get(url, headers=headers, stream=True)
with open(full_path, "wb") as f:
    for chunk in response.iter_content(chunk_size=8192):
        if chunk:
            f.write(chunk)

print("Backup salvo em:", full_path)
