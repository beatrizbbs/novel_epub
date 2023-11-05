from setuptools import *

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setup(
    name = "novel_epub",
    version = "1.0.0",
    author = "Beatriz Batista",
    author_email = "beaatrizbatista@hotmail.com",
    description = "Convert novel chapters to an EPUB file.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "URL",
    packages = find_packages(),
    python_requires = ">=3.8",
    keywords="wescraping, novel, epub",
    entry_points={
    'console_scripts': [
        'novel_epub = novel_epub:main',
        ],
    },
    install_requires=[ 
        'beautifulsoup4>=4.12.2',
        'ebooklib>=0.18',
        'cloudscraper>=1.2.71',
    ]
)