### Page Analyzer

https://python-project-83-xzst.onrender.com

## Описание

Page Analyzer — это веб-приложение, которое позволяет добавлять сайты и анализировать их на базовые SEO-показатели.

Сервис принимает URL, проверяет его корректность, сохраняет в базу данных и выполняет HTTP-запрос к странице. В ответ он определяет ключевые характеристики страницы: статус-код, заголовок (title), основной заголовок (h1) и мета-описание.

Проект демонстрирует работу с веб-запросами, парсингом HTML и хранением данных в базе.

### Hexlet tests and linter status:
[![Actions Status](https://github.com/maltoleb/python-project-83/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/maltoleb/python-project-83/actions)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=maltoleb_python-project-83&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=maltoleb_python-project-83)



## Возможности

- Добавление URL для анализа
- Валидация введённого URL
- Нормализация адреса (приведение к корректному виду)
- Отображение уведомлений (flash-сообщений) об успешных и ошибочных действиях
- Хранение URL в базе данных
- Проверка сайта по запросу пользователя
- Отображение результатов проверки:
  - HTTP статус-код
  - Заголовок страницы (title)
  - Основной заголовок (h1)
  - Мета-описание (description)

## Стек:

| Инструмент | Описание |
|-----------|---------|
| **Python** | Основной язык разработки |
| **Flask** | Веб-фреймворк для обработки HTTP-запросов |
| **PostgreSQL** | База данных для хранения URL и результатов |
| **psycopg** | Драйвер для работы с PostgreSQL |
| **requests** | Выполнение HTTP-запросов к сайтам |
| **BeautifulSoup** | Парсинг HTML и извлечение SEO-данных |
| **validators** | Проверка корректности URL |
| **python-dotenv** | Работа с переменными окружения |
| **Gunicorn** | Production-сервер для запуска приложения |
| **uv** | Менеджер зависимостей |
| **ruff** | Линтер для проверки качества кода |
| **Bootstrap** | Стилизация интерфейса |

## Установка

**1. Клонируйте репозиторий:**

git clone `git@github.com:maltoleb/python-project-83.git`

cd python-project-83

**2. Установите зависимости:**

make install

**3. Создайте файл `.env` и добавьте переменные окружения:**

DATABASE_URL=your_database_url

SECRET_KEY=your_secret_key

## Запуск

### Запуск в production режиме:

make start

Приложение будет запущено через Gunicorn (production WSGI-сервер).

### Запуск в режиме разработки:

make dev

После запуска приложение будет доступно по адресу:
http://127.0.0.1:5000