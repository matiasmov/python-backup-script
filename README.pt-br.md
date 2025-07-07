
# 🚀 Automação de Backup da plataforma Snipe-IT!

 Código para se por em ferramentas de agendamento de tarefas, buscando realizar o backup da plataforma Snipe-IT e enviar para um diretório da Rede. Além disso, a Automação conta com o envio de email automático contendo as informações da operação, ou seja, se foi realizada com sucesso e, caso ocorra um erro inesperado, o destinatário seja avisado.


## 📖 Referência

Outras versões

 - [README.ME](./README.md)

## 🔑 Variáveis de Ambiente

Para rodar esse projeto, você vai precisar adicionar as seguintes variáveis de ambiente no seu .env

`BACKUP_PATH` -> _Responsável pelo diretório onde armazenará os backups_

`API_BASE_URL` -> _Caminho da URL do seu Snipe-IT_

`AUTH_TOKEN` -> _TOKEN de API_

* Recomendável o uso de uma varíavel para eliminar as repetições de "os.getenv()", assim como exposto no "config_manager.py"




## ⚙️ Stack utilizada

**Back-end:** Python


## 🕵🏻‍♂️ Autores 

- [@matiasmov](https://github.com/matiasmov)

