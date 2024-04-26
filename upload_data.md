# Описание работы модуля upload_data.py
## Предварительные работы
1. Должна быть создана база SQLite
2. В базе предварительно должны быть созданы все необходимые таблицы
3. Создана отдельная папка под сырые данные

## Формирование [upload_data_db_config.yml](utils%2Fconfig%2Fupload_data_db_config.yml)
**db_name** - абсолютный путь до файла БД \
**[path][raw_data]** - путь до дирректории где лежат сырые csv файлы \
**[tables]** - перечисление всех таблиц \
**[tables][{filename}][db_table_name]** - имя обрабатываемого файла в папке с сырыми данными \
**[tables][{filename}][model_name]** - имя таблицы в БД куда должны быть записаны данные \
**[tables][{filename}][column]** - тут прописано сопоставление колонок \
**key** - имя столбца в raw файле **value** - имя столбца в БД. \
Если указать сопоставление не всех столбцов, то запишутся только те, для которых указано сопоставление

## Запуск модуля
Модуль можно запустить из коммандной строки, либо инициируя class UploadDataToDatabase() в коде проекта \
### Коммандная строка
Имеется обязательный CLI параметр _config_ объявляется -c либо --config параметр должени принять путь до конфиг файла \
Пример: \
`python upload_data.py --config C:\py_project\fdata\utils\config\upload_data_db_config.yml` \
`python upload_data.py -c C:\py_project\fdata\utils\config\upload_data_db_config.yml`