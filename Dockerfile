FROM python:3.14-slim

# Установка uv
RUN pip install uv

# Установка рабочей директории
WORKDIR /

# Копирование файлов с зависимостями из корня проекта
COPY pyproject.toml uv.lock ./

# Установка зависимостей через uv
RUN uv sync --frozen

# Добавляем путь к виртуальному окружению в PATH
ENV PATH="/.venv/bin:$PATH"

# Устанавливаем Python путь для импортов
ENV PYTHONPATH="${PYTHONPATH}:/"

# Создаем директорию для приложения
WORKDIR /app

# Копирование остальных файлов проекта
COPY ./app .


WORKDIR /

# Команда по умолчанию (будет переопределена в docker-compose)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
