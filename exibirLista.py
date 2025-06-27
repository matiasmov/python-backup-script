import requests
import os

path = r"T:\_ESTAGIÁRIOS\SniperBackup"
url_list_backup = "http://10.1.0.251:8081/api/v1/settings/backups"

headers = {
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiMjg1ZWUxNzZiN2UxMWJjMjZlZGUxY2YxY2U0ZmM1ZjE3ZDMzZjU3Y2FiODE1YWE5MDAxZGMyNGI5OTIzM2Q2Yjg2MWZhZmRkOTBlMGJkYmEiLCJpYXQiOjE3NDg4ODMwMjEuMTM5NTksIm5iZiI6MTc0ODg4MzAyMS4xMzk1OTYsImV4cCI6MzAxMTE4NzAyMS4xMTQyNjUsInN1YiI6IjkwNiIsInNjb3BlcyI6W119.r47ZK2FW9GMM4SvCoB6UFT_jlzLrwmnmThSKu9ePdDmgWTY_YB--dnDTgIXSoqkqM9z4sIXD_u2HpOYBwz9P0mYrqk9mvBTQyIzcxcl9Oe_1aYfbBnJ8ko8PAWzcfwNVLPShBQUl2lHvQJvQ_6NjsMhbhcsAhhk7hFrMnxtkQcEAx18LROHxDCryxz2HGhjtcVNrhJYhcKJTVvyGuraHbS4q3sex-ZOnngvU1eDY139IPFsDZasrYnUuu63kKQiCY3qKK_SXtBmgWTsL6K8E6EiXzamltBdWaH-W5iuu-ylRTE3ywhrvzuKT9yI5WSzJlwRty_E0o7JjGHfIrg77GFxH-hQxka2WbP5y_4wHs3lViH155sodDu2m0erT0nFJGuG02YgR3c6-X4D_U7huzOrf-RnoJjSePQGcFZd9AznLeFAz0v-ufx9uAlQZTJUQfNxTnvRf-PE2llFk6OyOE_ch1F4cWPGF0z2ezlIixNjkNAMtnqBDr2YKfRh9ZCyt9X2M5hAOds0ysyLCkMCJquPjH5A3kfkhIggctttQgMz0tloqDFWugVSK8-SZbdAy8X188ThEandxbGnO_3L5yGbRQqj7mudfjpXbkG3oCbZnJ3ikSPVHges6aQ3cwWiQiayCCBKEnp_ifukhWyoi3OBiG07n7_XDqs49FNIuP0Q",
    "Accept": "application/zip, application/json"
}

# Obtém a lista de backups
response_list = requests.get(url_list_backup, headers=headers)
data = response_list.json()

# Ordena pela data de modificação (mais recente primeiro)
sorted_backups = sorted(data["rows"], key=lambda x: x["modified_value"], reverse=True)

# Seleciona o mais recente
latest_backup = sorted_backups[0]
filename = latest_backup["filename"]
url = f"http://10.1.0.251:8081/api/v1/settings/backups/download/{filename}"
full_path = os.path.join(path, filename)

# Baixa o arquivo
response = requests.get(url, headers=headers, stream=True)
with open(full_path, "wb") as f:
    for chunk in response.iter_content(chunk_size=8192):
        if chunk:
            f.write(chunk)

print("Backup salvo em:", full_path)
