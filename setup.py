from setuptools import setup, find_packages

setup(
    name='wordpress-py',
    version='0.1.0',
    description='A Python client for interacting with WordPress REST API',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/wordpress-py',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
