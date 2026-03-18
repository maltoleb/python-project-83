import os
import validators
from flask import Flask, render_template, request, flash, url_for, redirect
from dotenv import load_dotenv
from urllib.parse import urlparse
from .db import get_urls

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

#routes:
@app.route("/")
def index():
    return render_template('index.html')

@app.post("/urls")
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

@app.get("/urls")
def urls_index():
    urls = get_urls()
    return render_template('urls.html', urls=urls)

@app.get("/urls/<int:id>")
def urls_show(id):
    url = get_url(id)
    checks = get_checks(id)
    return render_template(
        "url.html", 
        url=url, checks=checks
        )

@app.post("/urls/<int:id>/checks")
def create_check(id):
    add_check(id)
    flash("Страница успешно проверена")
    return redirect(url_for("urls_show", id=id))

#helpers:
def normalize_url(url):
    parsed = urlparse(url)
    if not parsed.scheme:
        url = f"https://{url}"
        parsed = urlparse(url)
    return f"{parsed.scheme}://{parsed.netloc}"
