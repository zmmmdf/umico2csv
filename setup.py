from setuptools import setup, find_packages

setup(
    name='umico2csv',
    version='1.2.0',
    description='This is a Python web scraper built to extract car information from umico.az, one of the most popular online seller websites in Azerbaijan.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/zmmmdf/umico2csv',
    author='Ziya Mammadov',
    author_email='ziyamm08@gmail.com',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    py_modules=['umico2csv.scraper'],
    install_requires=[
        'requests',
        'beautifulsoup4',
        'aiohttp',
        'asyncio',
        'csv',
    ],
    entry_points={
        'console_scripts': [
            'umico-scraper=scraper.scraper:Scraper.scrape',
        ],
    },
    python_requires='>=3.6',
)
