from buycoins.client import BuyCoinsClient
from buycoins.exceptions import WalletError, ClientError
from buycoins.errors import check_response
from buycoins.p2p import P2P

class Wallet(BuyCoinsClient):
    """The Wallet class handles the buying, selling, buy transactions and the generation of wallet address 
    for receiving cryptocurrencies.
    """


    supported_cryptocurrencies = ["bitcoin", "ethereum", "litecoin", "naira_token", "usd_coin", "usd_tether"]
    status = ["open", "completed"]

    def buyCrypto(self, currency: str = "bitcoin", coin_amount: float = 0.01):
        """Buys a cryptocurrency, for the given amount passed.

        Args:
            currency (str): The cryptocurrency to be bought.
            coin_amount(float): Amount of currency to be bought.

        Returns:
            response: A JSON object containing response from the request.
        """

        if currency not in self.supported_cryptocurrencies:
            raise WalletError("Invalid or unsupported cryptocurrency")

        p2p = P2P()
        price_info = p2p.getCurrentPrice(side="buy", currency=currency)
        price_id = price_info[0]['id']
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
            "price": price_id,
            "coin_amount": coin_amount,
            "currency": currency
        }
        try:
            response = self._execute_request(query=self.__query, variables=__variables)
            check_response(WalletError, response)
        except (WalletError, ClientError) as e:
            return e.args
        else:
            return response["data"]["buy"]
    
    def sellCrypto(self, currency: str = "bitcoin", coin_amount: float = 0.01):
        """Sells a cryptocurrency, for the given amount passed.

        Args:
            currency (str): The cryptocurrency to be sold.
            coin_amount(float): Amount of currency to be bought.

        Returns:
            response: A JSON object containing response from the request.
        """

        if currency not in self.supported_cryptocurrencies:
            raise WalletError("Invalid or unsupported cryptocurrency")

        p2p = P2P()
        price_info = p2p.getCurrentPrice(side="sell", currency=currency)
        price_id = price_info[0]['id']
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
            "price": price_id,
            "coin_amount": coin_amount,
            "currency": currency
        }

        try:
            response = self._execute_request(query=self.__query, variables=__variables)
            check_response(WalletError, response)
        except (WalletError, ClientError) as e:
            return e.args
        else:
            return response["data"]["sell"]
    
    def getNetworkFee(self, currency: str = "bitcoin", amount: str = 0.01):
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

        try:
            response = self._execute_request(query=self.__query, variables=__variables)
            check_response(WalletError, response)
        except (WalletError, ClientError) as e:
            return e.args
        else:
            return response["data"]["getEstimatedNetworkFee"]
    
    def createAddress(self, currency: str = "bitcoin"):
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

        try:
            response = self._execute_request(query=self.__query, variables=__variables)
            check_response(WalletError, response)
        except (WalletError, ClientError) as e:
            return e.args
        else:
            return response["data"]["createAddress"]   
    
    def sendCrypto(self, address: str, currency: str = "bitcoin", amount: float = 0.01):
        """Sells a cryptocurrency, for the given amount passed.

        Args:
            currency (str): The cryptocurrency to be sold.
            coin_amount(float): Amount of currency to be bought.

        Returns:
            response: A JSON object containing response from the request.
        """

        if currency not in self.supported_cryptocurrencies:
            raise WalletError("Invalid or unsupported cryptocurrency")

        if len(address) < 34 or len(address) > 34:
            raise WalletError("Invalid address")

        self.__query = """
            mutation SendCrypto($amount: BigDecimal!, $currency: Cryptocurrency, $address:String!){
                send SendCoin(cryptocurrency: $currency, amount:$amount, address:address) {
                    id
                    address
                    amount
                    cryptocurrency
                    fee
                    status
                    transaction {
                        txhash
                        id
                    }
                }
            }
            """

        __variables = {
            "address": address,
            "amount": amount,
            "currency": currency
        }

        try:
            response = self._execute_request(query=self.__query, variables=__variables)
            check_response(WalletError, response)
        except (WalletError, ClientError) as e:
            return e.args
        else:
            return response["data"]["SendCoin"]
