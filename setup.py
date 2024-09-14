from setuptools import setup, find_packages

setup(
    name='wordpress-client',
    version='0.1.4',
    description='A Python client for interacting with WordPress REST API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Berk Birkan',
    author_email='info@berkbirkan.com',
    url='https://github.com/berkbirkan/wordpress-client',
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
