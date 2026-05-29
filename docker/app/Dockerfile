# легкий образ debian
FROM python:3.13-slim

LABEL authors="BeBop"

# Отключаем буферизацию stdout и stderr
ENV PYTHONUNBUFFERED=1

# Запрещает создавать .pyc файлы
ENV PYTHONDONTWRITEBYTECODE=1

# Запрещает pip хранить cash wheels
ENV PIP_NO_CACHE_DIR=1


# Рабочая директория внутри контейнера. Все команды выполняются от неё
WORKDIR /app

# Копируем req в корень app, устанавливаем зависимости
COPY ./requirements.txt ./
RUN pip install -r ./requirements.txt

# Копируем файлы app (не ломаем структуру проекта)
COPY ./app ./app

ENTRYPOINT ["python", "-m", "app.main"]