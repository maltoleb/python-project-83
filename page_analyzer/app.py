import os
import validators
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, flash, url_for, redirect
from dotenv import load_dotenv
from urllib.parse import urlparse
from .db import (
    get_urls,
    get_url,
    add_url,
    find_url,
    add_check,
    get_checks,
)

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
        flash("Некорректный URL", "danger")
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
    url = get_url(id)
    site_name = url[1]
    try:
        response = requests.get(site_name, timeout=5)
        response.raise_for_status()
        status_code = response.status_code
        h1 = extract_h1(response.text)
        title = extract_title(response.text)
        description = extract_description(response.text)
        add_check(id, status_code, h1, title, description)
        flash("Страница успешно проверена", "success")
    except requests.exceptions.RequestException:
        flash("Произошла ошибка при проверке", "danger")
    return redirect(url_for("urls_show", id=id))

#helpers:
def normalize_url(url):
    parsed = urlparse(url)
    if not parsed.scheme:
        url = f"https://{url}"
        parsed = urlparse(url)
    return f"{parsed.scheme}://{parsed.netloc}"

def extract_h1(html):
    soup = BeautifulSoup(html, "html.parser")
    h1 = soup.find("h1")
    if h1:
        return h1.get_text(strip=True)
    return None

def extract_title(html):
    soup = BeautifulSoup(html, "html.parser")
    title = soup.find("title")
    if title:
        return title.get_text(strip=True)
    return None

def extract_description(html):
    soup = BeautifulSoup(html, "html.parser")
    meta = soup.find("meta", attrs={"name": "description"})
    if meta:
        return meta.get("content")
    return None
