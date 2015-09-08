try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

config = {
    'description': '3 Corner',
    'author': 'Juan Montemayor',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'jam1@alum.mit.edu',
    'version': '0.1',
    'packages': find_packages(),
    'name': 'threecorner',
}

setup(**config)