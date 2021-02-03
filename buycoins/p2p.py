from buycoins.client import BuyCoinsClient
from buycoins.exceptions import P2PError, ClientError
from buycoins.utils import check_response


class P2P(BuyCoinsClient):
    """The P2P class handles peer-2-peer transactions.
    """

    supported_cryptocurrencies = ["bitcoin", "ethereum", "litecoin", "naira_token", "usd_coin", "usd_tether"]
    side = ["buy", "sell"]
    status = ["open", "completed"]

    def getPrices(self):
        """Returns the current price for supported cryptocurrencies on BuyCoins

        Returns:
            response: An array of cryptocurrency data.

        """

        try:
            self.__query = """
                query {
                  getPrices {
                    id
                    cryptocurrency
                    buyPricePerCoin
                    minBuy
                    maxBuy
                    expiresAt
                  }
                }    
            """

            response = self._execute_request(query=self.__query)
            check_response(response, P2PError)
        except (P2PError, ClientError) as e:
            return e.response
        else:
            return response['data']['getPrices']

    def getCurrentPrice(self, orderSide: str = "buy", currency: str = "bitcoin"):
        """Retrieves the current `side` price for the supplied cryptocurrency.

        Args:
            orderSide (str):  The order side which can either be buy or sell.
            currency (str): The cryptocurrency whose current price is to be retrieved.

        Returns:
            response: A JSON object containing response from the request.
        """
        try:
            if currency not in self.supported_cryptocurrencies:
                raise P2PError("Invalid or unsupported cryptocurrency", 404)

            if orderSide not in self.side:
                raise P2PError("Invalid order side", 404)

            self.__query = """
                query GetBuyCoinsPrices($side: OrderSide, $currency: Cryptocurrency) {
                  getPrices(side: $side, cryptocurrency: $currency){
                    buyPricePerCoin
                    cryptocurrency
                    id
                    maxBuy
                    maxSell
                    minBuy
                    minCoinAmount
                    minSell
                    sellPricePerCoin
                    status
                  }
                }
            """

            __variables = {
                "side": orderSide,
                "currency": currency
            }

            response = self._execute_request(query=self.__query, variables=__variables)
            check_response(response, P2PError)
        except (P2PError, ClientError) as e:
            return e.response
        else:
            return response["data"]["getPrices"]

    def getDynamicPriceExpiry(self, status: str = "open", side: str = "buy", currency: str = "bitcoin"):
        """Retrieves the dynamic prices for available cryptocurrencies.

        Args:
            status (str): The status of the current order.

        Returns:
            response: A JSON object containing the response from the request.

        """

        try:

            if status not in self.status:
                raise P2PError("Invalid status passed", 404)

            if side not in self.side:
                raise P2PError("Invalid side passed", 404)

            if currency not in self.supported_cryptocurrencies:
                raise P2PError("Invalid or unsupported cryptocurrency", 404)

            self.__query = """
                query GetOrders($status: GetOrdersStatus!){
                    getOrders(status: $status) {
                        dynamicPriceExpiry    
                    }
                }
            """

            __variables = {
                "status": status,
            }

            response = self._execute_request(query=self.__query, variables=__variables)
            check_response(response, P2PError)
        except (P2PError, ClientError) as e:
            return e.response
        else:
            return response["data"]["getOrders"]

    def placeLimitOrder(self, orderSide: str = "buy", coinAmount: float = 0.01, currency: str = "bitcoin",
                        staticPrice: int = 100000, priceType: str = "static"):
        """Places limit order for the supplied cryptocurrency.

        Args:
            orderSide (str): The side of the order. This could be `buy` or `sell`.
            coinAmount (str): The amount the limit order is based on.
            currency (str): The cryptocurrency involved in the limit order.
            staticPrice (str, optional): Static price for the cryptocurrency in Naira.
            priceType (str): Static or dynamic price for the cryptocurrency.

        Returns:
            response: A JSON object containing the result from the request.

        """

        try:
            if orderSide not in self.side:
                raise P2PError("Invalid side passed", 404)

            if currency not in self.supported_cryptocurrencies:
                raise P2PError("Invalid or unsupported cryptocurrency", 404)

            self.__query = """
                mutation PostLimitOrder($orderSide: OrderSide!, $coinAmount: BigDecimal!, $cryptocurrency: Cryptocurrency, $staticPrice: BigDecimal, $priceType: PriceType!){
                    postLimitOrder(orderSide: $orderSide, coinAmount: $coinAmount, cryptocurrency: $cryptocurrency, staticPrice: $staticPrice, priceType: $priceType) {
                        id
                        cryptocurrency
                        coinAmount
                        side
                        status 
                        createdAt
                        pricePerCoin
                        priceType
                        staticPrice
                        dynamicExchangeRate
                    }
                }
           """

            __variables = {
                "orderSide": orderSide,
                "coinAmount": coinAmount,
                "cryptocurrency": currency,
                "staticPrice": staticPrice,
                "priceType": priceType
            }

            response = self._execute_request(query=self.__query, variables=__variables)
            check_response(response, P2PError)
        except (P2PError, ClientError) as e:
            return e.response
        else:
            return response["data"]["postLimitOrder"]

    def postMarketOrder(self, orderSide: str = "buy", coinAmount: float = 0.01, currency: str = "bitcoin"):
        """Posts a market order for the supplied cryptocurrency.

        Args:
            orderSide (str): The type of order to be placed. It could either be `buy` or `sell`.
            coinAmount (float): Amount of coin to be sold.
            currency (str): Cryptocurrency involved in the market order.

        Returns:
            response: A JSON object containing the response from the request.

        """

        try:
            if orderSide not in self.side:
                raise P2PError("Invalid side passed", 404)

            if currency not in self.supported_cryptocurrencies:
                raise P2PError("Invalid or unsupported cryptocurrency", 404)

            self.__query = """
                mutation PostMarketOrder($orderSide: OrderSide!, $coinAmount: BigDecimal!, $cryptocurrency: Cryptocurrency){
                    postMarketOrder(orderSide: $orderSide, coinAmount: $coinAmount, cryptocurrency: $cryptocurrency){
                        id
                        cryptocurrency
                        coinAmount
                        side
                        status 
                        createdAt
                        pricePerCoin
                        priceType
                        staticPrice
                        dynamicExchangeRate
                    }
                }
            """

            __variables = {
                "orderSide": orderSide,
                "coinAmount": coinAmount,
                "cryptocurrency": currency,
            }

            response = self._execute_request(query=self.__query, variables=__variables)
            check_response(response, P2PError)
        except (P2PError, ClientError) as e:
            return e.response
        else:
            return response["data"]["postMarketOrder"]

    def getOrders(self, status: str = "open"):
        """Retrieves orders based on their status.

        Args:
            status (str): Status of the order which could either be `open` or `completed`.

        Returns:
            response: A JSON object containing the response from the request.

        """
        try:
            if status not in self.status:
                raise P2PError("Invalid status passed", 404)

            self.__query = """
                query GetOrders($status: GetOrdersStatus!){
                    getOrders(status: $status) {
                        dynamicPriceExpiry
                        orders {
                          edges {
                            node {
                              id
                              cryptocurrency
                              coinAmount
                              side
                              status
                              createdAt
                              pricePerCoin
                              priceType
                              staticPrice
                              dynamicExchangeRate
                            }
                          }
                        }
                    }
                }
            """

            __variables = {
                "status": status
            }

            response = self._execute_request(query=self.__query, variables=__variables)
            check_response(response, P2PError)
        except (P2PError, ClientError) as e:
            return e.response
        else:
            return response["data"]["getOrders"]

    def getMarketBook(self):
        """Retrieves market history.

        Returns:
            response: A JSON object containing response from the request.

        """

        try:
            self.__query = """
                query {
                  getMarketBook {
                    dynamicPriceExpiry
                    orders {
                      edges {
                        node {
                          id
                          cryptocurrency
                          coinAmount
                          side
                          status 
                          createdAt
                          pricePerCoin
                          priceType
                          staticPrice
                          dynamicExchangeRate
                        }
                      }
                    }
                  }
                }
            """

            response = self._execute_request(query=self.__query)
            check_response(response, P2PError)
        except (P2PError, ClientError) as e:
            return e.response
        return response["data"]["getMarketBook"]
