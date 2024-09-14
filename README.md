
# WordPressClient Python Package Documentation

---

## Overview

`WordPressClient` is a Python client library designed to interact with the WordPress REST API. This package allows you to easily retrieve posts, categories, tags, comments, and perform various operations by integrating seamlessly with any WordPress site. It's built with simplicity and flexibility in mind, allowing developers to easily manage WordPress content programmatically.

---

## Installation

To install the `WordPressClient` package, you can use pip:

```bash
pip install wordpress-client
```

---

## Usage

### Initializing the Client

The `WordPressClient` class requires a WordPress site URL to initialize. It also accepts an optional `proxy` parameter if you need to route requests through a proxy.

```python
from wordpress_client.client import WordPressClient

client = WordPressClient('https://criptoexperto.com')
```

### Supported URL Formats

The `WordPressClient` supports various URL formats:
- `https://criptoexperto.com`
- `http://criptoexperto.com`
- `criptoexperto.com` (defaults to HTTPS)

### Retrieving Recent Posts

To fetch the most recent posts from the WordPress site:

```python
recent_posts = client.get_recent_posts()
```

This returns a list of `WordPressPost` instances, each containing detailed information about the posts, such as title, content, date, URL, categories, tags, and more.

### Retrieving Categories

To fetch all categories from the WordPress site:

```python
categories = client.get_categories()
```

This returns a list of `WordPressCategory` instances, each containing detailed information about the categories, such as name, slug, description, and ID.

### Retrieving Tags

To fetch all tags from the WordPress site:

```python
tags = client.get_tags()
```

This returns a list of `WordPressTag` instances, each containing detailed information about the tags, such as name, slug, description, and ID.

### Retrieving Posts by Category

To fetch posts within a specific category:

```python
category_posts = client.get_posts_by_category(category_id=1, post_count=5, post_order='desc')
```

This returns a list of `WordPressPost` instances in the specified category.

### Retrieving Posts by Date Range

To fetch posts within a specific date range, optionally filtered by category:

```python
date_range_posts = client.get_posts_by_date_range(start_date='2020-01-01', end_date='2021-01-01', category_id=1)
```

This returns a list of `WordPressPost` instances published between the specified dates, optionally filtered by the given category.

### Retrieving Comments by Post

To fetch comments associated with a specific post:

```python
post_comments = client.get_comments_by_post(post_id=1)
```

This returns a list of `WordPressComment` instances for the specified post, each containing details like author, content, and date.

### Retrieving Posts by Author

To fetch posts written by a specific author:

```python
author_posts = client.get_posts_by_author(author_id=1)
```

This returns a list of `WordPressPost` instances authored by the specified author.

### Retrieving Posts with Advanced Filtering

To fetch posts with advanced filtering options, such as multiple categories and custom sorting:

```python
filtered_posts = client.get_posts_from_wordpress(website_categories="1,2", post_count=5, post_order='asc')
```

This returns a list of `WordPressPost` instances, filtered by the specified categories and ordered as requested.

---

## Examples

Here is a simple example to demonstrate the usage:

```python
from wordpress_client.client import WordPressClient

client = WordPressClient('https://criptoexperto.com')

# Fetch recent posts
recent_posts = client.get_recent_posts()
for post in recent_posts:
    print(f"Title: {post.post_title}, Date: {post.post_date}, URL: {post.post_url}")

# Fetch categories
categories = client.get_categories()
for category in categories:
    print(f"Category: {category.name}, ID: {category.id}")

# Fetch tags
tags = client.get_tags()
for tag in tags:
    print(f"Tag: {tag.name}, ID: {tag.id}")

# Fetch comments for a specific post
comments = client.get_comments_by_post(post_id=5)
for comment in comments:
    print(f"Comment by {comment.author_name}: {comment.content[:50]}")

# Fetch posts by a specific author
author_posts = client.get_posts_by_author(author_id=3)
for post in author_posts:
    print(f"Title: {post.post_title}, Date: {post.post_date}")
```

---

## Error Handling

The library handles HTTP errors gracefully. If a request fails due to an HTTP error (e.g., 404 or 500), it prints the error and the server response. You can further customize error handling as needed.

```python
try:
    posts = client.get_recent_posts()
except Exception as e:
    print("An error occurred:", e)
```

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contributing

Contributions are welcome! Please see the [CONTRIBUTING](CONTRIBUTING.md) file for more information on how to contribute to this project.

---

## Contact

For any inquiries or issues, please open an issue on [GitHub](https://github.com/berkbirkan/wordpress-client) or contact the maintainer directly.

---

This documentation is designed to be clear and easy to follow, ensuring that users of all skill levels can utilize the `WordPressClient` package effectively. It can be displayed on both the GitHub repository and the PyPI page, providing consistent and accessible information across platforms.