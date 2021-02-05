from buycoins.client import BuyCoinsClient
from buycoins.exceptions import WalletError, ClientError, ServerError
from buycoins.p2p import P2P
from buycoins.exceptions.utils import check_response


class Wallet(BuyCoinsClient):
    """The Wallet class handles the buying, selling, buy transactions and the generation of wallet address
    for receiving cryptocurrencies.
    """

    supported_cryptocurrencies = ["bitcoin", "ethereum", "litecoin", "naira_token", "usd_coin", "usd_tether"]
    status = ["open", "completed"]

    def buy_crypto(self, currency: str = "bitcoin", coin_amount: float = 0.01):
        """Buys a cryptocurrency, for the given amount passed.

        Args:
            currency (str): The cryptocurrency to be bought.
            coin_amount(float): Amount of currency to be bought.

        Returns:
            response: A JSON object containing response from the request.
        """

        try:
            if currency not in self.supported_cryptocurrencies:
                raise WalletError("Invalid or unsupported cryptocurrency", 400)

            p2p = P2P()
            price_info = p2p.get_current_price(order_side="buy", currency=currency)
            price_id = price_info[0]["id"]
            self._query = """
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

            _variables = {"price": price_id, "coin_amount": coin_amount, "currency": currency}
            response = self._execute_request(query=self._query, variables=_variables)
            check_response(response, WalletError)
        except (WalletError, ClientError, ServerError) as e:
            return e.response
        else:
            return response["data"]["buy"]

    def sell_crypto(self, currency: str = "bitcoin", coin_amount: float = 0.01):
        """Sells a cryptocurrency, for the given amount passed.

        Args:
            currency (str): The cryptocurrency to be sold.
            coin_amount(float): Amount of currency to be bought.

        Returns:
            response: A JSON object containing response from the request.
        """

        try:
            if currency not in self.supported_cryptocurrencies:
                raise WalletError("Invalid or unsupported cryptocurrency", 400)

            p2p = P2P()
            price_info = p2p.get_current_price(order_side="sell", currency=currency)
            price_id = price_info[0]["id"]
            self._query = """
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

            _variables = {"price": price_id, "coin_amount": coin_amount, "currency": currency}

            response = self._execute_request(query=self._query, variables=_variables)
            check_response(response, WalletError)
        except (WalletError, ClientError, ServerError) as e:
            return e.response
        else:
            return response["data"]["sell"]

    def get_network_fee(self, currency: str = "bitcoin", coin_amount: float = 0.01):
        """Retrieves NetworkFee for the supplied cryptocurrency.

        Args:
            currency (str): The cryptocurrency whose network fee is been checked.
            coin_amount(float): Amount of currency.

        Returns:
            response: A JSON object containing response from the request.
        """

        try:
            if currency not in self.supported_cryptocurrencies:
                raise WalletError("Invalid or unsupported cryptocurrency", 400)

            self._query = """
                query NetworkFee($currency: Cryptocurrency, $amount: BigDecimal!) {
                    getEstimatedNetworkFee(cryptocurrency: $currency, amount: $amount) {
                        estimatedFee
                        total
                    }
                }
            """

            _variables = {"currency": currency, "amount": coin_amount}

            response = self._execute_request(query=self._query, variables=_variables)
            check_response(response, WalletError)
        except (WalletError, ClientError, ServerError) as e:
            return e.response
        else:
            return response["data"]["getEstimatedNetworkFee"]

    def create_address(self, currency: str = "bitcoin"):
        """Creates a wallet address for the supplied cryptocurrency.

        Args:
            currency (str): The cryptocurrency wallet address to be created.

        Returns:
            response: A JSON object containing response from the request.
        """

        try:
            if currency not in self.supported_cryptocurrencies:
                raise WalletError("Invalid or unsupported cryptocurrency", 400)

            self._query = """
                mutation CreateWalletAddress($currency: Cryptocurrency) {
                    createAddress(cryptocurrency: $currency) {
                        cryptocurrency
                        address
                    }
                }
            """

            _variables = {"currency": currency}

            response = self._execute_request(query=self._query, variables=_variables)
            check_response(response, WalletError)
        except (WalletError, ClientError, ServerError) as e:
            return e.response
        else:
            return response["data"]["createAddress"]

    def send_crypto(self, address: str, currency: str = "bitcoin", coin_amount: float = 0.01):
        """Sells a cryptocurrency, for the given amount passed.

        Args:
            currency (str): The cryptocurrency to be sold.
            coin_amount(float): Amount of currency to be bought.

        Returns:
            response: A JSON object containing response from the request.
        """

        try:
            if currency not in self.supported_cryptocurrencies:
                raise WalletError("Invalid or unsupported cryptocurrency", 400)

            if not address:
                raise WalletError("Invalid address", 400)

            self._query = """
                mutation SendCrypto($amount: BigDecimal!, $currency: Cryptocurrency, $address: String!){
                    send(cryptocurrency: $currency, amount: $amount, address: $address) {
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

            _variables = {"address": address, "amount": coin_amount, "currency": currency}

            response = self._execute_request(query=self._query, variables=_variables)
            check_response(response, WalletError)
        except (WalletError, ClientError, ServerError) as e:
            return e.response
        else:
            return response["data"]["SendCoin"]

    def get_balances(self, currency=None):
        """Retrieves user cryptocurrency balances

        Returns:
            response: A JSON object containing the user cryptocurrency balances.

        """

        try:
            if currency:
                self._query = """
                query($currency: Cryptocurrency) {
                    getBalances(cryptocurrency: $currency) {
                        id
                        cryptocurrency
                        confirmedBalance
                    }
                }
            """

                _variables = {"currency": currency}
                response = self._execute_request(query=self._query, variables=_variables)
                check_response(response, WalletError)

            else:
                self._query = """
                    query {
                        getBalances {
                            id
                            cryptocurrency
                            confirmedBalance
                        }
                    }
                """
                response = self._execute_request(query=self._query)
                check_response(response, WalletError)
        except (WalletError, ClientError, ServerError) as e:
            return e.response
        else:
            return response["data"]["getBalances"]
