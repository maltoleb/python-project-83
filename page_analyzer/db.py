import os
import psycopg
from dotenv import load_dotenv
from datetime import datetime


load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')


def get_urls():
    with psycopg.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cur.execute('''SELECT
                urls.id,
                urls.name,
                urls.created_at,
                checks.created_at AS last_check_date,
                checks.status_code
            FROM urls
            LEFT JOIN (
                SELECT DISTINCT ON (url_id) *
                FROM url_checks
                ORDER BY url_id, created_at DESC
            ) AS checks
            ON urls.id = checks.url_id
            ORDER BY urls.id DESC;
            ''')
            return cur.fetchall()
        
def get_url(id):
    with psycopg.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cur.execute(
            "SELECT id, name, created_at FROM urls WHERE id=%s",
            (id,)
            )
            return cur.fetchone()

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

def add_check(url_id, status_code, h1, title, description):
    created_at = datetime.now()
    with psycopg.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cur.execute(
                '''INSERT INTO url_checks 
                (url_id, status_code, h1, title, description, created_at)
                VALUES (%s, %s, %s, %s, %s, %s)''', 
                (url_id, status_code, h1, title, description, created_at)
            )

def get_checks(url_id):
    with psycopg.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cur.execute(
                '''SELECT id, status_code, h1, title, description, created_at
                FROM url_checks
                WHERE url_id = %s
                ORDER by id DESC''', (url_id,)
            )
            return cur.fetchall()