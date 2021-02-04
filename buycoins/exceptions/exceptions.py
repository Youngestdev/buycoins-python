"""
The Exception classes below are child classes of Python's `Exception` class.

Returns:
    A JSON object containing the message and status code.
"""


class ServerError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
            self.code = args[1]
        else:
            self.message = None
            self.code = 500

    @property
    def response(self):
        return {"status": "ServerError", "code": self.code, "message": self.message}


class ClientError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
            self.code = args[1]
        else:
            self.message = None
            self.code = 401

    @property
    def response(self):
        return {"status": "ClientError", "code": self.code, "message": self.message}


class QueryError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
            self.code = args[1]
        else:
            self.message = None
            self.code = 404

    @property
    def response(self):
        return {"status": "QueryError", "code": self.code, "message": self.message}


class P2PError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
            self.code = args[1]
        else:
            self.message = None
            self.code = 404

    @property
    def response(self):
        return {"status": "P2PError", "code": self.code, "message": +self.message}


class AccountError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
            self.code = args[1]
        else:
            self.message = None
            self.code = 404

    @property
    def response(self):
        return {"status": "AccountError", "code": self.code, "message": self.message}


class WalletError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
            self.code = args[1]
        else:
            self.message = None
            self.code = 404

    @property
    def response(self):
        return {"status": "WalletError", "code": self.code, "message": self.message}
