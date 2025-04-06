# Используем официальный образ Python
FROM python:3.11
LABEL authors="vladelo"

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY . .

# Устанавливаем зависимости
RUN pip install -r requirements.txt

# Команда запуска
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]