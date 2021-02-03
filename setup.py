import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="buycoins-python",
    version="0.3.4",
    description="Python SDK for the BuyCoin\"s API",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Youngestdev/BuyCoins-Python",
    author="Abdulazeez Abdulazeez Adeshina",
    author_email="youngestdev@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    install_requires=["python-graphql-client", "requests", "python-decouple"],
    packages=find_packages(),
    python_requires=">=3.6"
)
