class ClientError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return "ClientError, {0}".format(self.message)
        else:
            return "A ClientError has been raised"

class QueryError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return "QueryError, {0} ".format(self.message)
        else:
            return "A QueryError has been raised"

class P2PError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return "P2PError, {0} ".format(self.message)
        else:
            return "A P2P has been raised"

class AccountError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return "AccountError, {0} ".format(self.message)
        else:
            return "An AccountError has been raised"

class WalletError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'Wallet, {0} '.format(self.message)
        else:
            return 'A WalletError has been raised'

