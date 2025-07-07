# 🚀 Backup Automation of the Snipe-IT platform!

Code to be used in task scheduling tools, seeking to perform a backup of the Snipe-IT platform and send it to a directory on the Network. In addition, the Automation includes the sending of an automatic email containing information about the operation, that is, if it was performed successfully and, if an unexpected error occurs, the recipient is notified.

## 📖 Reference

Other versions

- [README.PT-BR](./README.pt-br.md)

## 🔑 Environment Variables

To run this project, you will need to add the following environment variables to your .env

`BACKUP_PATH` -> _Responsible for the directory where you will store the backups_

`API_BASE_URL` -> _Path to your Snipe-IT URL_

`AUTH_TOKEN` -> _API TOKEN_

* It is recommended to use a variable to eliminate repetitions of "os.getenv()", as shown in "config_manager.py"

## ⚙️ Stack used

**Back-end:** Python

## 🕵🏻‍♂️ Authors

- [@matiasmov](https://github.com/matiasmov)