import requests
import os

from config_manager import (
    PATH, API_BASE_URL, AUTH_TOKEN
)

def download_latest_backup():


    """
    Lista os backups disponíveis na API, identifica o mais recente e faz o download.
    Retorna o caminho completo do arquivo baixado em caso de sucesso.
    Se algo der errado, uma exceção será levantada.
    """

    url_list_backup = f"{API_BASE_URL}/api/v1/settings/backups"

    headers = {
        "Authorization": f"Bearer {AUTH_TOKEN}",
        "Accept": "application/zip, application/json"
    }

    # lista de backups
    print("Obtendo lista de backups da API...")
    response_list = requests.get(url_list_backup, headers=headers)

    print(f"Status Code da Resposta: {response_list.status_code}")
    print(f"Conteúdo da Resposta (Primeiros 500 caracteres): {response_list.text[:500]}")                                                                            


    response_list.raise_for_status() # Levanta um erro HTTP para status 4xx/5xx
    data = response_list.json()

    # ORDENA (mais recente primeiro)
    sorted_backups = sorted(data["rows"], key=lambda x: x["modified_value"], reverse=True)

    if not sorted_backups:
        raise ValueError("Nenhum backup encontrado na API para download.")

    # Pegando o mais recente
    latest_backup = sorted_backups[0]
    filename = latest_backup["filename"]
    url = f"{API_BASE_URL}/api/v1/settings/backups/download/{filename}"
    full_path = os.path.join(PATH, filename)

    # Garante que o diretório de destino exista
    os.makedirs(PATH, exist_ok=True)

    # Baixando o backup escolhido acima
    print(f"Tentando baixar o backup mais recente: {filename} para {full_path}")
    response = requests.get(url, headers=headers, stream=True)
    response.raise_for_status() # Levanta um erro HTTP para status 4xx/5xx

    with open(full_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

    print("Backup salvo em:", full_path)
    return full_path # Retorna o caminho completo do arquivo salvo

# Bloco de teste opcional para SalvarBackup.py
if __name__ == "__main__":
    print("--- Testando SalvarBackup.py individualmente ---")
    try:
        baixado_em = download_latest_backup()
        print(f"Teste de download ocorreu com êxito. Arquivo em: {baixado_em}")
    except Exception as e:
        print(f"Teste de download falhou: {e}")