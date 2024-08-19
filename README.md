
# WordPressClient Python Package Documentation

---

## Overview

`WordPressClient` is a Python client library designed to interact with the WordPress REST API. This package allows you to easily retrieve posts, categories, comments, and perform various operations by integrating seamlessly with any WordPress site. It's built with simplicity and flexibility in mind, allowing developers to easily manage WordPress content programmatically.

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
from wordpress_client import WordPressClient

client = WordPressClient('https://berkbirkan.com')
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

This returns a JSON array of recent posts.

### Retrieving Categories

To fetch all categories from the WordPress site:

```python
categories = client.get_categories()
```

This returns a JSON array of categories available on the site.

### Retrieving Posts by Category

To fetch posts within a specific category, optionally filtered by a date range:

```python
category_posts = client.get_posts_by_category(category_id=1, start_date='2020-01-01', end_date='2021-01-01')
```

This will return posts in the specified category that were published within the given date range.

### Retrieving Posts by Date Range

To fetch posts within a specific date range, optionally filtered by category:

```python
date_range_posts = client.get_posts_by_date_range(start_date='2020-01-01', end_date='2021-01-01', category_id=1)
```

This will return posts published between the specified dates, optionally filtered by the given category.

### Retrieving Comments by Post

To fetch comments associated with a specific post:

```python
post_comments = client.get_comments_by_post(post_id=1)
```

This returns a JSON array of comments for the specified post.

### Retrieving Posts by Author

To fetch posts written by a specific author:

```python
author_posts = client.get_posts_by_author(author_id=1)
```

This returns a JSON array of posts by the specified author.

---

## Examples

Here is a simple example to demonstrate the usage:

```python
from wordpress_client import WordPressClient

client = WordPressClient('https://criptoexperto.com')

# Fetch recent posts
recent_posts = client.get_recent_posts()
print(recent_posts)

# Fetch categories
categories = client.get_categories()
print(categories)

# Fetch posts by category within a date range
category_posts = client.get_posts_by_category(category_id=2, start_date='2024-01-01', end_date='2024-12-31')
print(category_posts)

# Fetch comments for a specific post
comments = client.get_comments_by_post(post_id=5)
print(comments)

# Fetch posts by a specific author
author_posts = client.get_posts_by_author(author_id=3)
print(author_posts)
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
