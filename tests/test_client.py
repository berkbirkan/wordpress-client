import unittest
from wordpress_client.client import WordPressClient, WordPressPost, WordPressCategory, WordPressTag, WordPressComment
class TestWordPressClient(unittest.TestCase):
    def setUp(self):
        self.client = WordPressClient('https://kelimelerbenim.com')

    def test_get_recent_posts(self):
        print("\nRunning test_get_recent_posts...")
        posts = self.client.get_recent_posts()
        self.assertIsInstance(posts, list)
        self.assertGreater(len(posts), 0)
        self.assertIsInstance(posts[0], WordPressPost)

        # Print details about fetched posts
        for post in posts[:3]:  # Only print details for the first 3 posts for brevity
            print(f"Post Title: {post.post_title}")
            print(f"Post URL: {post.post_url}")
            print(f"Post Date: {post.post_date}")
            print(f"Post Content (excerpt): {post.post_content[:100]}...")  # Print the first 100 characters

    def test_get_categories(self):
        print("\nRunning test_get_categories...")
        categories = self.client.get_categories()
        self.assertIsInstance(categories, list)
        self.assertGreater(len(categories), 0)
        self.assertIsInstance(categories[0], WordPressCategory)

        # Print details about fetched categories
        for category in categories[:3]:  # Only print details for the first 3 categories
            print(f"Category Name: {category.name}")
            print(f"Category ID: {category.id}")
            print(f"Category Slug: {category.slug}")

    def test_get_tags(self):
        print("\nRunning test_get_tags...")
        tags = self.client.get_tags()
        self.assertIsInstance(tags, list)
        self.assertGreater(len(tags), 0)
        self.assertIsInstance(tags[0], WordPressTag)

        # Print details about fetched tags
        for tag in tags[:3]:  # Only print details for the first 3 tags
            print(f"Tag Name: {tag.name}")
            print(f"Tag ID: {tag.id}")
            print(f"Tag Slug: {tag.slug}")

    def test_get_posts_by_category(self):
        print("\nRunning test_get_posts_by_category...")
        category_id = 1  # Example category ID
        posts = self.client.get_posts_by_category(category_id)
        self.assertIsInstance(posts, list)
        self.assertGreater(len(posts), 0)
        self.assertIsInstance(posts[0], WordPressPost)

        # Print details about posts in the category
        for post in posts[:3]:  # Only print details for the first 3 posts
            print(f"Post Title: {post.post_title}")
            print(f"Post Categories: {post.categories}")
            print(f"Post Date: {post.post_date}")

    def test_get_posts_by_date_range(self):
        print("\nRunning test_get_posts_by_date_range...")
        posts = self.client.get_posts_by_date_range('2010-01-01', '2024-12-31', category_id=1)
        self.assertIsInstance(posts, list)
        self.assertGreater(len(posts), 0)
        self.assertIsInstance(posts[0], WordPressPost)

        # Print details about posts within the date range
        for post in posts[:3]:  # Only print details for the first 3 posts
            print(f"Post Title: {post.post_title}")
            print(f"Post Date: {post.post_date}")
            print(f"Post URL: {post.post_url}")

    def test_get_comments_by_post(self):
        print("\nRunning test_get_comments_by_post...")
        post_id = 7567  # Example post ID
        comments = self.client.get_comments_by_post(post_id)
        self.assertIsInstance(comments, list)
        self.assertGreater(len(comments), 0)
        self.assertIsInstance(comments[0], WordPressComment)

        # Print details about comments on the post
        for comment in comments[:3]:  # Only print details for the first 3 comments
            print(f"Comment by: {comment.author_name}")
            print(f"Comment Date: {comment.date}")
            print(f"Comment Content: {comment.content[:100]}...")  # Print the first 100 characters

    def test_get_posts_by_author(self):
        print("\nRunning test_get_posts_by_author...")
        author_id = 1  # Example author ID
        posts = self.client.get_posts_by_author(author_id)
        self.assertIsInstance(posts, list)
        self.assertGreater(len(posts), 0)
        self.assertIsInstance(posts[0], WordPressPost)

        # Print details about posts by the author
        for post in posts[:3]:  # Only print details for the first 3 posts
            print(f"Post Title: {post.post_title}")
            print(f"Post Author ID: {post.author_id}")
            print(f"Post Date: {post.post_date}")

    def test_get_posts_from_wordpress(self):
        print("\nRunning test_get_posts_from_wordpress...")
        # Test with categories
        posts = self.client.get_posts_from_wordpress(website_categories="1,2", post_count=5, post_order='desc')
        self.assertIsInstance(posts, list)
        self.assertGreater(len(posts), 0)
        self.assertIsInstance(posts[0], WordPressPost)

        # Print details about posts fetched with specific categories
        for post in posts[:3]:  # Only print details for the first 3 posts
            print(f"Post Title: {post.post_title}")
            print(f"Post Categories: {post.categories}")
            print(f"Post Date: {post.post_date}")

        # Test without categories (latest posts)
        posts = self.client.get_posts_from_wordpress(post_count=5, post_order='asc')
        self.assertIsInstance(posts, list)
        self.assertGreater(len(posts), 0)
        self.assertIsInstance(posts[0], WordPressPost)

        # Print details about the latest posts
        for post in posts[:3]:  # Only print details for the first 3 posts
            print(f"Post Title: {post.post_title}")
            print(f"Post Date: {post.post_date}")
            print(f"Post URL: {post.post_url}")

if __name__ == '__main__':
    unittest.main()
