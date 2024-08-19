import unittest
from wordpress_py.client import WordPressClient

class TestWordPressClient(unittest.TestCase):
    def setUp(self):
        self.client = WordPressClient('https://kelimelerbenim.com')

    def test_get_recent_posts(self):
        posts = self.client.get_recent_posts()
        self.assertIsInstance(posts, list)
        self.assertGreater(len(posts), 0)

    def test_get_categories(self):
        categories = self.client.get_categories()
        self.assertIsInstance(categories, list)

    def test_get_posts_by_category(self):
        category_id = 1  # Example category ID
        posts = self.client.get_posts_by_category(category_id)
        self.assertIsInstance(posts, list)

    def test_get_posts_by_date_range(self):
        posts = self.client.get_posts_by_date_range('2010-01-01', '2024-12-31', category_id=1)
        self.assertIsInstance(posts, list)

    def test_get_comments_by_post(self):
        post_id = 7567  # Example post ID
        comments = self.client.get_comments_by_post(post_id)
        self.assertIsInstance(comments, list)
        

    def test_get_posts_by_author(self):
        author_id = 1  # Example author ID
        posts = self.client.get_posts_by_author(author_id)
        self.assertIsInstance(posts, list)
       


if __name__ == '__main__':
    unittest.main()
