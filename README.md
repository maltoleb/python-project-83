### Page Analyzer

https://python-project-83-xzst.onrender.com

## Description

Page Analyzer — это веб-приложение, которое позволяет добавлять сайты и анализировать их на базовые SEO-показатели.

Сервис принимает URL, проверяет его корректность, сохраняет в базу данных и выполняет HTTP-запрос к странице. В ответ он определяет ключевые характеристики страницы: статус-код, заголовок (title), основной заголовок (h1) и мета-описание.

Проект демонстрирует работу с веб-запросами, парсингом HTML и хранением данных в базе.

### Hexlet tests and linter status:
[![Actions Status](https://github.com/maltoleb/python-project-83/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/maltoleb/python-project-83/actions)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=maltoleb_python-project-83&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=maltoleb_python-project-83)



## Features

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

## Technologies Used:

- **Python** — основной язык разработки  
- **Flask** — веб-фреймворк для обработки HTTP-запросов и маршрутизации  
- **PostgreSQL** — база данных для хранения URL и результатов проверок  
- **psycopg** — драйвер для работы с PostgreSQL  
- **requests** — выполнение HTTP-запросов к сайтам  
- **BeautifulSoup** — парсинг HTML и извлечение SEO-данных  
- **validators** — проверка корректности URL  
- **python-dotenv** — работа с переменными окружения  
- **Gunicorn** — production-сервер для запуска приложения  
- **uv** — менеджер зависимостей и окружения  
- **ruff** — линтер для проверки качества кода  
- **Bootstrap** — стилизация интерфейса

## Installation

1. Клонируйте репозиторий:
git clone git@github.com:maltoleb/python-project-83.git
cd python-project-83

2. Установите зависимости:
make install

3. Создайте файл `.env` и добавьте переменные окружения:
DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key
---

## Run

### Запуск в режиме разработки:
make dev
После запуска приложение будет доступно по адресу:
http://127.0.0.1:5000