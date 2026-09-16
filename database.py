import sqlite3
from pathlib import Path


DB_PATH = Path("maged_atef.db")


def get_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    with get_connection() as db:

        db.execute("""
            CREATE TABLE IF NOT EXISTS accounts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                platform TEXT NOT NULL,
                username TEXT,
                profile_url TEXT,
                access_token TEXT,
                refresh_token TEXT,
                status TEXT DEFAULT 'disconnected',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        db.execute("""
            CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                platform TEXT NOT NULL,
                external_id TEXT,
                caption TEXT,
                media_path TEXT,
                status TEXT DEFAULT 'draft',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        db.execute("""
            CREATE TABLE IF NOT EXISTS schedules (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                platform TEXT NOT NULL,
                caption TEXT,
                media_path TEXT,
                publish_at TEXT,
                status TEXT DEFAULT 'scheduled'
            )
        """)

        db.execute("""
            CREATE TABLE IF NOT EXISTS activity_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                action TEXT NOT NULL,
                platform TEXT,
                details TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        db.commit()


def add_account(
    platform,
    username,
    profile_url,
    access_token=None,
    refresh_token=None
):
    with get_connection() as db:
        db.execute("""
            INSERT INTO accounts
            (platform, username, profile_url, access_token, refresh_token, status)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            platform,
            username,
            profile_url,
            access_token,
            refresh_token,
            "connected"
        ))

        db.commit()


def get_accounts():
    with get_connection() as db:
        return db.execute("""
            SELECT * FROM accounts
            ORDER BY created_at DESC
        """).fetchall()


def add_post(platform, external_id, caption, media_path, status):
    with get_connection() as db:
        db.execute("""
            INSERT INTO posts
            (platform, external_id, caption, media_path, status)
            VALUES (?, ?, ?, ?, ?)
        """, (
            platform,
            external_id,
            caption,
            media_path,
            status
        ))

        db.commit()


def get_posts(platform=None):
    with get_connection() as db:

        if platform:
            return db.execute("""
                SELECT * FROM posts
                WHERE platform = ?
                ORDER BY created_at DESC
            """, (platform,)).fetchall()

        return db.execute("""
            SELECT * FROM posts
            ORDER BY created_at DESC
        """).fetchall()


def log_activity(action, platform=None, details=None):
    with get_connection() as db:
        db.execute("""
            INSERT INTO activity_logs
            (action, platform, details)
            VALUES (?, ?, ?)
        """, (
            action,
            platform,
            details
        ))

        db.commit()
