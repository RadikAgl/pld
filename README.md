# Интересные места Москвы

## Запуск проекта

   ```shell
   python -m venv my-env
   my-env\Scripts\activate
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver
   ```
## Запуск проекта

### Скачайте проект

   ```shell
   git clone https://github.com/RadikAgl/pld.git
   ```

### Настройка виртуального окружения
Перейдите в корневую папку проекта. Создайте и активируйте виртуальное окружение
   ```shell
   python -m venv my-env
   my-env\Scripts\activate
   ```

### Установка зависимостей

   ```shell   
   pip install -r requirements.txt

   ```
### Выполните миграции

   ```shell
  python manage.py migrate 
   ```

### Запустите сервер

В корне проекта создайте файл .ENV и добавьте туда SECRET_KEY.
   ```
  SECRET_KEY="secret key"
   ```
Для запуска сервера, выполните:
   ```shell
  python manage.py runserver 
   ```

Данный проект запущен на radikagl.pythonanywhere.com