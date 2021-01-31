from buycoins.client import BuyCoinsClient
from buycoins.exceptions import WalletError
from buycoins.p2p import P2P

class Wallet(BuyCoinsClient):
    """The Wallet class handles buying, selling, recieving and sending transactions.
    Also handles Wallet Account Creation

    Args:
        auth_key (str): Authentication key in `public_key:private_key` string form.
    """

    def __init__(self, auth_key: str):
        super().__init__(auth_key)
        self.supported_cryptocurrencies = ["bitcoin", "ethereum", "litecoin", "naira_token", "usd_coin", "usd_tether"]
        self.status = ["open", "completed"]

    def BuyCrypto(self, currency: str = "bitcoin", coin_amount: float = 0.01):
        """Buys a cryptocurrency, for the given amount passed.

        Args:
            currency (str): The cryptocurrency to be bought.
            coin_amount(float): Amount of currency to be bought.

        Returns:
            response: A JSON object containing response from the request.
        """

        if currency not in self.supported_cryptocurrencies:
            raise WalletError("Invalid or unsupported cryptocurrency")

        p2p = P2P(self.auth_key)
        price_info = p2p.getCurrentPrice(side="buy", currency=currency)
        price = price_info['data']['getPrices'][0]['id']
        self.__query = """
            mutation BuyCoin($price: ID!, $coin_amount: BigDecimal!, $currency: Cryptocurrency){
                    buy(price: $price, coin_amount: $coin_amount, cryptocurrency: $currency) {
                        id
                        cryptocurrency
                        status
                        totalCoinAmount
                        side
                    }
                }
            """

        __variables = {
            "price": price ,
            "coin_amount": coin_amount,
            "currency": currency
        }

        response = self._execute_request(self.__query, variables=__variables)
        return response
    
    def SellCrypto(self, currency: str = "bitcoin", coin_amount: float = 0.01):
        """Sells a cryptocurrency, for the given amount passed.

        Args:
            currency (str): The cryptocurrency to be sold.
            coin_amount(float): Amount of currency to be bought.

        Returns:
            response: A JSON object containing response from the request.
        """

        if currency not in self.supported_cryptocurrencies:
            raise WalletError("Invalid or unsupported cryptocurrency")

        p2p = P2P(self.auth_key)
        price_info = p2p.getCurrentPrice(side="sell", currency=currency)
        price = price_info['data']['getPrices'][0]['id']
        self.__query = """
            mutation SellCoin($price: ID!, $coin_amount: BigDecimal!, $currency: Cryptocurrency){
                    sell(price: $price, coin_amount: $coin_amount, cryptocurrency: $currency) {
                        id
                        cryptocurrency
                        status
                        totalCoinAmount
                        side
                    }
                }
            """

        __variables = {
            "price": price ,
            "coin_amount": coin_amount,
            "currency": currency
        }

        response = self._execute_request(self.__query, variables=__variables)
        return response
    
    def NetworkFee(self, currency: str = "bitcoin", amount: str = 0.01):
        """Retrieves NetworkFee for the supplied cryptocurrency.

        Args:
            currency (str): The cryptocurrency whose network fee is been checked.
            amount(float): Amount of currency.

        Returns:
            response: A JSON object containing response from the request.
        """

        if currency not in self.supported_cryptocurrencies:
            raise WalletError("Invalid or unsupported cryptocurrency")

        self.__query = """
            query NetworkFee($currency: Cryptocurrency, $amount: BigDecimal!) {
                getEstimatedNetworkFee(cryptocurrency: $currency, amount: $amount) {
                    estimatedFee
                    total
                }
            }
        """

        __variables = {
            "currency": currency,
            "amount": amount
        }

        response = self._execute_request(self.__query, variables=__variables)
        return response
    
    def CreateAddress(self, currency: str = "bitcoin"):
        """Creates a wallet address for the supplied cryptocurrency.

        Args:
            currency (str): The cryptocurrency wallet address to be created.

        Returns:
            response: A JSON object containing response from the request.
        """

        if currency not in self.supported_cryptocurrencies:
            raise WalletError("Invalid or unsupported cryptocurrency")

        self.__query = """
            mutation CreateWalletAddress($currency: Cryptocurrency) {
                createAddress(cryptocurrency: $currency) {
                    cryptocurrency
                    address
                }
            }
        """

        __variables = {
            "currency": currency
        }

        response = self._execute_request(self.__query, variables=__variables)
        return response
    
    def GetAccountBalance(self, currency: str = "bitcoin"):
        """Retrieves a wallet address for the supplied cryptocurrency.

        Args:
            currency (str): The cryptocurrency wallet address to be retrieved.

        Returns:
            response: A JSON object containing response from the request.
        """

        if currency not in self.supported_cryptocurrencies:
            raise WalletError("Invalid or unsupported cryptocurrency")

        self.__query = """
            query GetAccountBalance($currency: Cryptocurrency) {
                getBalances(cryptocurrency: $currency){
                    id
                    cryptocurrency
                    confirmedBalance
                }
            }
        """

        __variables = {
            "currency": currency
        }

        response = self._execute_request(self.__query, variables=__variables)
        return response

