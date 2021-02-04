# BuyCoins Python Library

The BuyCoins Python library allows interactions with the BuyCoins API from applications written in Python.

## Documentation

You can view the documentation for the BuyCoins Python library [here](https://buycoins.youngest.dev).

> The official BuyCoins API documentation can be found on the [BuyCoins developer portal.](https://https://developers.buycoins.africa/).

## Installation

This package can be installed from [PyPi]() using the command:

```shell
pip install buycoins-python
```

Install from source:

```shell
python setup.py install
```

## Requirements

- Python 3.6+

## Usage

The library depends on an authentication key to communicate, send requests and receive responses from the BuyCoins API.

Create a `.env` file and set your authentication key in the format below:

```dotenv
auth_key="public key:private key"
```

If you don't have a public and private key, follow the procedures
on [How do I get access?](https://developers.buycoins.africa/#how-do-i-get-access).

Example usage of the library is:

```python
from buycoins import Wallet

buycoins_user = Wallet()

# Print the account balances of each cryptocurrency the buycoins_user have.

print(buycoins_user.getBalances())
```

## Handling Exceptions

The library comes built-in with exception handlers for unsuccessful requests. This is documented in
the [exceptions](https://buycoins.youngest.dev/exceptions) page.

## Executing your own queries

In a situtation where you need to run a query different from what is provided in the library, create an instance of
the `BuyCoinsClient` class and run your query:

```python
from buycoins import BuyCoinsClient

# Write your query

query = """
  query queryName{
    query body
  }
"""

# Write your variables if any
variables = {
    "x": x,
    "y": y
}

# Execute your request

response = BuyCoinsClient()._execute_request(query=query, variables=variables)

# Print the response from the request sent

print(response)
```

## Contributing

Check [CONTRIBUTING.MD](./CONTRIBUTING.MD)

## Authors

- [Abdulazeez Abdulazeez Adeshina](https://twitter.com/kvng_zeez)
- [Precious Ndubueze](https://twitter.com/pgabbyprecious)

## License

See [LICENCE.MD](./LICENSE).
