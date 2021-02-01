class ClientError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
            self.error_code = args[1]
        else:
            self.message = None
            self.error_code = None # NOT_FOUND

    @property
    def response(self):
        return {
            "message": self.message,
            "status_code": self.error_code
        }

class QueryError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
            self.error_code = args[1]
        else:
            self.message = None
            self.error_code = None # NOT_FOUND

    @property
    def response(self):
        return {
            "message": self.message,
            "status_code": self.error_code
        }

class P2PError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
            self.error_code = args[1]
        else:
            self.message = None
            self.error_code = None # NOT_FOUND

    @property
    def response(self):
        return {
            "message": self.message,
            "status_code": self.error_code
        }

class AccountError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
            self.error_code = args[1]
        else:
            self.message = None
            self.error_code = None # NOT_FOUND

    @property
    def response(self):
        return {
            "message": self.message,
            "status_code": self.error_code
        }

class WalletError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
            self.error_code = args[1]
        else:
            self.message = None
            self.error_code = None # NOT_FOUND

    @property
    def response(self):
        return {
            "message": self.message,
            "status_code": self.error_code
        }