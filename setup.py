from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as readme:
    long_description = readme.read()

setup(
    name='buycoins',
    version='0.1.1',
    description='Python SDK for the BuyCoin\'s API',
    url='https://github.com/Youngestdev/BuyCoins-Python',
    author="Abdulazeez Abdulazeez Adeshina",
    author_email='youngestdev@gmail.com',
    license = 'LICENSE',
    install_requires=['python-graphql-client', 'requests'],
    packages=find_packages(),
    python_requires='>=3.6'
)