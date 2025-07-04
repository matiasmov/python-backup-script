import datetime
import sys 

from email_utils import send_email, EMAIL_RECEIVER
from SalvarBackup import download_latest_backup # download_latest_backup agora retorna APENAS o caminho em sucesso, ou levanta exceção

def run_full_backup_process():
    today_date = datetime.date.today().strftime("%Y-%m-%d")
    email_subject = f"Status do Backup - {today_date}"
    email_body = ""

    print("Iniciando processo de backup...")

    try:
        # Executa o download do backup
        # Vai ter apenas um retorno (o caminho do arquivo baixado).
        downloaded_path = download_latest_backup()

        email_subject = f"SUCESSO no Backup - {today_date}"
        email_body += f"Resultado do Download:\n  - Backup baixado com sucesso em: {downloaded_path}\n"
        print("Download do backup concluído com sucesso.")
        
    except Exception as e:
        # Qualquer exceção que ocorra em download_latest_backup (ou em outro lugar) será capturada aqui.
        email_subject = f"FALHA no Backup - {today_date}"
        email_body += f"Um erro ocorreu durante o backup:\n"
        email_body += f"Tipo de Erro: {type(e).__name__}\n"
        email_body += f"Detalhes do Erro: {e}\n"
        print(f"O processo de backup falhou: {e}")

    finally:
        # Este bloco é executado SEMPRE, independentemente de ter ocorrido um erro ou não.
        # Garante que o e-mail seja enviado.
        print("Processo de backup concluído. Enviando notificação por e-mail...")
        send_email(email_subject, email_body, EMAIL_RECEIVER)

if __name__ == "__main__":
    run_full_backup_process()