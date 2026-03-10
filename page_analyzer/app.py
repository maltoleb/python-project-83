import os
import psycopg
import validators
from flask import Flask, render_template, request, flash, url_for, redirect
from dotenv import load_dotenv
from datetime import datetime
from urllib.parse import urlparse

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

#routes:
@app.route("/")
def index():
    return render_template('index.html')

@app.post('/urls')
def create_url():
    url = request.form.get('url')
    if not url:
        flash("URL обязателен")
        return render_template("index.html"), 422

    normalized_url = normalize_url(url)
    if not validators.url(normalized_url):
        flash("Некорректный URL")
        return render_template("index.html"), 422

    existing = find_url(normalized_url)

    if existing:
        url_id = existing[0]
    else:
        add_url(normalized_url)
        existing = find_url(normalized_url)
        url_id = existing[0]

    flash("Страница успешно добавлена", "success")

    return redirect(url_for("urls_show", id=url_id))

#DB functions:
def get_urls():
    with psycopg.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM urls ORDER BY id DESC")
            rows = cur.fetchall()
            return rows

def add_url(name):
    created_at = datetime.now()
    with psycopg.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO urls (name, created_at) VALUES (%s, %s)",
                (name, created_at)
            )

def find_url(name):
    with psycopg.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT id FROM urls WHERE name = %s",
                (name,)
            )
            return cur.fetchone()

#helpers:
def normalize_url(url):
    parsed = urlparse(url)
    if not parsed.scheme:
        url = f"https://{url}"
        parsed = urlparse(url)
    return f"{parsed.scheme}://{parsed.netloc}"
