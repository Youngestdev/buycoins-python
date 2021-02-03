"""
The Exception classes below are child classes of Python's `Exception` class.

Returns:
    A JSON object containing the message and status code.
"""

class ClientError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
            self.status_code = args[1]
        else:
            self.message = None
            self.status_code = 401

    @property
    def response(self):
        return {
            "status_code": self.status_code,
            "message": "ClientError: " + self.message
        }


class QueryError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
            self.status_code = args[1]
        else:
            self.message = None
            self.status_code = 404

    @property
    def response(self):
        return {
            "status_code": self.status_code,
            "message": "QueryError: " + self.message
        }


class P2PError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
            self.status_code = args[1]
        else:
            self.message = None
            self.status_code = 404

    @property
    def response(self):
        return {
            "status_code": self.status_code,
            "message": "P2PError: " + self.message
        }


class AccountError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
            self.status_code = args[1]
        else:
            self.message = None
            self.status_code = 404

    @property
    def response(self):
        return {
            "status_code": self.status_code,
            "message": "AccountError: " + self.message
        }


class WalletError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
            self.status_code = args[1]
        else:
            self.message = None
            self.status_code = 404

    @property
    def response(self):
        return {
            "status_code": self.status_code,
            "message": "WalletError" + self.message
        }