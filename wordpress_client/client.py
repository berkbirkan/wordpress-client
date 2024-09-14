import requests
from urllib.parse import urlparse, urlunparse
import random

class WordPressPost:
    def __init__(self, post_data):
        self.id = post_data.get('id')
        self.post_title = post_data.get('title', {}).get('rendered', '')
        self.post_content = post_data.get('content', {}).get('rendered', '')
        self.post_date = post_data.get('date')
        self.post_url = post_data.get('link')
        self.status = post_data.get('status')
        self.author_id = post_data.get('author')
        self.categories = post_data.get('categories', [])
        self.tags = post_data.get('tags', [])
        self.comment_count = post_data.get('comment_count')
        self.excerpt = post_data.get('excerpt', {}).get('rendered', '')
        self.featured_media = post_data.get('featured_media')
        self.metadata = post_data.get('meta', {})

class WordPressCategory:
    def __init__(self, category_data):
        self.id = category_data.get('id')
        self.name = category_data.get('name', '')
        self.slug = category_data.get('slug', '')
        self.description = category_data.get('description', '')
        self.count = category_data.get('count')
        self.parent = category_data.get('parent')

class WordPressTag:
    def __init__(self, tag_data):
        self.id = tag_data.get('id')
        self.name = tag_data.get('name', '')
        self.slug = tag_data.get('slug', '')
        self.description = tag_data.get('description', '')
        self.count = tag_data.get('count')

class WordPressComment:
    def __init__(self, comment_data):
        self.id = comment_data.get('id')
        self.post = comment_data.get('post')
        self.author_name = comment_data.get('author_name', '')
        self.author_email = comment_data.get('author_email', '')
        self.content = comment_data.get('content', {}).get('rendered', '')
        self.date = comment_data.get('date')
        self.status = comment_data.get('status')

class WordPressClient:
    def __init__(self, site_url, proxy=None):
        parsed_url = urlparse(site_url)
        if not parsed_url.scheme:
            parsed_url = parsed_url._replace(scheme='https')
        elif parsed_url.scheme not in ['http', 'https']:
            raise ValueError("URL scheme must be either 'http' or 'https'")
        
        self.site_url = urlunparse(parsed_url).rstrip('/')
        self.session = requests.Session()
        if proxy:
            self.session.proxies.update(proxy)

    def _json_to_wordpress_posts(self, json_posts):
        """Convert JSON data to WordPressPost instances."""
        return [WordPressPost(post_data) for post_data in json_posts]

    def _json_to_wordpress_categories(self, json_categories):
        """Convert JSON data to WordPressCategory instances."""
        return [WordPressCategory(category_data) for category_data in json_categories]

    def _json_to_wordpress_tags(self, json_tags):
        """Convert JSON data to WordPressTag instances."""
        return [WordPressTag(tag_data) for tag_data in json_tags]

    def _json_to_wordpress_comments(self, json_comments):
        """Convert JSON data to WordPressComment instances."""
        return [WordPressComment(comment_data) for comment_data in json_comments]

    def get_recent_posts(self, post_count=5):
        url = f'{self.site_url}/wp-json/wp/v2/posts?per_page={post_count}'
        response = self.session.get(url)
        response.raise_for_status()
        return self._json_to_wordpress_posts(response.json())

    def get_categories(self):
        url = f'{self.site_url}/wp-json/wp/v2/categories'
        response = self.session.get(url)
        response.raise_for_status()
        return self._json_to_wordpress_categories(response.json())

    def get_tags(self):
        url = f'{self.site_url}/wp-json/wp/v2/tags'
        response = self.session.get(url)
        response.raise_for_status()
        return self._json_to_wordpress_tags(response.json())

    def get_posts_by_category(self, category_id, post_count=5, post_order='desc'):
        url = f'{self.site_url}/wp-json/wp/v2/posts?categories={category_id}&per_page={post_count}&orderby=date&order={post_order}'
        response = self.session.get(url)
        response.raise_for_status()
        return self._json_to_wordpress_posts(response.json())

    def get_posts_by_date_range(self, start_date, end_date, category_id=None, post_count=5):
        try:
            url = f'{self.site_url}/wp-json/wp/v2/posts?after={start_date}T00:00:00&before={end_date}T23:59:59&per_page={post_count}'
            if category_id:
                url += f'&categories={category_id}'
            response = self.session.get(url)
            response.raise_for_status()
            return self._json_to_wordpress_posts(response.json())
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")
            print(f"Response: {response.text}")
            return []

    def get_comments_by_post(self, post_id):
        url = f'{self.site_url}/wp-json/wp/v2/comments?post={post_id}'
        response = self.session.get(url)
        response.raise_for_status()
        return self._json_to_wordpress_comments(response.json())

    def get_posts_by_author(self, author_id, post_count=5):
        url = f'{self.site_url}/wp-json/wp/v2/posts?author={author_id}&per_page={post_count}'
        response = self.session.get(url)
        response.raise_for_status()
        return self._json_to_wordpress_posts(response.json())

    def get_posts_from_wordpress(self, website_categories="", post_count=1, post_order='desc'):
        # Split categories into a list if provided
        categories = website_categories.split(',') if website_categories else []
        
        # To store all fetched posts
        all_posts = []

        # Helper function to fetch posts
        def fetch_posts(category=None):
            # Build the request URL with parameters
            params = {
                'per_page': post_count,  # Number of posts to fetch
                'orderby': 'date',  # Order by date by default
                'order': 'desc' if post_order == 'desc' else 'asc',  # 'asc' for oldest first
            }
            if category:
                params['categories'] = category

            try:
                # Make the request to the WordPress REST API
                response = self.session.get(f'{self.site_url}/wp-json/wp/v2/posts', params=params)
                response.raise_for_status()  # Raise an exception for HTTP errors
                return response.json()  # Return the JSON response
            except requests.RequestException as e:
                print(f"Error fetching posts: {e}")
                return []

        # Fetch posts for each category if provided
        if categories:
            for category in categories:
                posts = fetch_posts(category)
                all_posts.extend(self._json_to_wordpress_posts(posts))
        else:
            # No categories provided, fetch latest posts
            posts = fetch_posts()
            all_posts.extend(self._json_to_wordpress_posts(posts))

        # Handle post_order (sort posts based on post_order)
        if post_order == 'random':
            random.shuffle(all_posts)
        elif post_order == 'asc':
            all_posts.sort(key=lambda x: x.post_date)
        else:
            # Default to 'desc' (latest first)
            all_posts.sort(key=lambda x: x.post_date, reverse=True)

        return all_posts
