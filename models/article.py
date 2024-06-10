# /models/article.py
from database.connection import get_db_connection

class Article:
    def __init__(self, author, magazine, title, content):
        self.author_id = author.id
        self.magazine_id = magazine.id
        self.title = title
        self.content = content
        self._create_article()

    def _create_article(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO articles (title, content, author_id, magazine_id)
            VALUES (?, ?, ?, ?)
        """, (self.title, self.content, self.author_id, self.magazine_id))
        conn.commit()
        self.id = cursor.lastrowid
        conn.close()

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value

    @property
    def author(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors WHERE id=?", (self.author_id,))
        author = cursor.fetchone()
        conn.close()
        return author

    @property
    def magazine(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM magazines WHERE id=?", (self.magazine_id,))
        magazine = cursor.fetchone()
        conn.close()
        return magazine
