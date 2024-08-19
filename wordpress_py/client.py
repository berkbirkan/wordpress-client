import requests

class WordPressClient:
    def __init__(self, site_url, proxy=None):
        self.site_url = site_url.rstrip('/')
        self.session = requests.Session()
        if proxy:
            self.session.proxies.update(proxy)

    def get_recent_posts(self):
        url = f'{self.site_url}/wp-json/wp/v2/posts'
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()

    def get_categories(self):
        url = f'{self.site_url}/wp-json/wp/v2/categories'
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()

    def get_posts_by_category(self, category_id):
        url = f'{self.site_url}/wp-json/wp/v2/posts?categories={category_id}'
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()

    def get_posts_by_date_range(self, start_date, end_date, category_id=None):
        url = f'{self.site_url}/wp-json/wp/v2/posts?after={start_date}&before={end_date}'
        if category_id:
            url += f'&categories={category_id}'
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()
