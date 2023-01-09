from setuptools import setup, find_packages

setup(
    name='dbapp',
    version='0.1.0',
    packages= find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
        'python-dotenv'
    ],
    entry_points={
        'console_scripts': [
            'db_app = app.webapp:main',
        ],
    },
)