import unittest
from models.author import Author
from models.article import Article
from models.magazine import Magazine
from database.setup import create_tables
from database.connection import get_db_connection

class TestModels(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        create_tables()

    def setUp(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM articles")
        cursor.execute("DELETE FROM authors")
        cursor.execute("DELETE FROM magazines")
        conn.commit()
        conn.close()

    def test_author_creation(self):
        author = Author("John Doe")
        self.assertEqual(author.name, "John Doe")

    def test_article_creation(self):
        author = Author("Jane Smith")
        magazine = Magazine("Science Weekly", "Science")
        article = Article(author, magazine, "Test Title", "Test Content")
        self.assertEqual(article.title, "Test Title")

    def test_magazine_creation(self):
        magazine = Magazine("Tech Weekly", "Technology")
        self.assertEqual(magazine.name, "Tech Weekly")
        self.assertEqual(magazine.category, "Technology")

    def test_author_articles(self):
        author = Author("Author A")
        magazine = Magazine("Magazine A", "Category A")
        article1 = Article(author, magazine, "Title 1", "Content 1")
        article2 = Article(author, magazine, "Title 2", "Content 2")

        articles = author.articles()
        self.assertEqual(len(articles), 2)
        self.assertEqual(articles[0][1], "Title 1")
        self.assertEqual(articles[1][1], "Title 2")

    def test_magazine_articles(self):
        author = Author("Author B")
        magazine = Magazine("Magazine B", "Category B")
        article1 = Article(author, magazine, "Title 3", "Content 3")
        article2 = Article(author, magazine, "Title 4", "Content 4")

        articles = magazine.articles()
        self.assertEqual(len(articles), 2)
        self.assertEqual(articles[0][1], "Title 3")
        self.assertEqual(articles[1][1], "Title 4")

    def test_magazine_contributors(self):
        author1 = Author("Author C")
        author2 = Author("Author D")
        magazine = Magazine("Magazine C", "Category C")
        Article(author1, magazine, "Title 5", "Content 5")
        Article(author2, magazine, "Title 6", "Content 6")

        contributors = magazine.contributors()
        self.assertEqual(len(contributors), 2)
        self.assertEqual(contributors[0][1], "Author C")
        self.assertEqual(contributors[1][1], "Author D")

if __name__ == "__main__":
    unittest.main()
