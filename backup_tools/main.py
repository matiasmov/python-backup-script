from backup_tools.services.email_service import email_report
from backup_tools.core.engine import list_backups

def run():
    print("starting...")

    filename, dataCode = list_backups()
    email_report(filename, dataCode)

if __name__ == "__main__":
    run()