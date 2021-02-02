from buycoins.client import BuyCoinsClient
from buycoins.errors import check_response
from buycoins.exceptions import P2PError, ClientError


class P2P(BuyCoinsClient):
    """The P2P class handles peer-2-peer transactions.
    """

    supported_cryptocurrencies = ["bitcoin", "ethereum", "litecoin", "naira_token", "usd_coin", "usd_tether"]
    side = ["buy", "sell"]
    status = ["open", "completed"]

    def getCurrentPrice(self, side: str = "buy", currency: str = "bitcoin"):
        """Retrieves the current `side` price for the supplied cryptocurrency.

        Args:
            side (str):  The order side which can either be buy or sell.
            currency (str): The cryptocurrency whose current price is to be retrieved.

        Returns:
            response: A JSON object containing response from the request.
        """

        if currency not in self.supported_cryptocurrencies:
            raise P2PError("Invalid or unsupported cryptocurrency")

        if side not in self.side:
            raise P2PError("Invalid order side")

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
            "side": side,
            "currency": currency
        }

        try:
            response = self._execute_request(query=self.__query, variables=__variables)
            check_response(P2PError, response)
        except (P2PError, ClientError) as e:
            return e.args
        else:
            return response["data"]["getPrices"]

    def getDynamicPriceExpiry(self, status: str = "open", side: str = "buy", currency: str = "bitcoin"):
        """Retrieves the dynamic price for the supplied cryptocurrency.

        Args:
            status (str): The status of the current order.
            side (str): The order side which can either be buy or sell.
            currency (str): The cryptocurrency whose price is to be retrieved.

        Returns:
            response: A JSON object containing the response from the request.

        """

        if status not in self.status:
            raise P2PError("Invalid status passed")

        if side not in self.side:
            raise P2PError("Invalid side passed")

        if currency not in self.supported_cryptocurrencies:
            raise P2PError("Invalid or unsupported cryptocurrency")

        self.__query = """
            query GetOrders($status: GetOrdersStatus!, $side: OrderSide, $currency: Cryptocurrency){
                getOrders(status: $status, side: $side, cryptocurrency: $currency) {
                    dynamicPriceExpiry    
                }
            }
        """

        __variables = {
            "status": status,
            "side": side,
            "currency": currency
        }

        try:
            response = self._execute_request(query=self.__query, variables=__variables)
            check_response(P2PError, response)
        except (P2PError, ClientError) as e:
            return e.args
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

        if orderSide not in self.side:
            raise P2PError("Invalid side passed")

        if currency not in self.supported_cryptocurrencies:
            raise P2PError("Invalid or unsupported cryptocurrency")

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

        try:
            response = self._execute_request(query=self.__query, variables=__variables)
            check_response(P2PError, response)
        except (P2PError, ClientError) as e:
            return e.args
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
        if orderSide not in self.side:
            raise P2PError("Invalid side passed")

        if currency not in self.supported_cryptocurrencies:
            raise P2PError("Invalid or unsupported cryptocurrency")

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

        try:
            response = self._execute_request(query=self.__query, variables=__variables)
            check_response(P2PError, response)
        except (P2PError, ClientError) as e:
            return e.args
        else:
            return response["data"]["postMarketOrder"]

    def getOrders(self, status: str = "open"):
        """Retrieves orders based on their status.

        Args:
            status (str): Status of the order which could either be `open` or `completed`.

        Returns:
            response: A JSON object containing the response from the request.

        """

        if status not in self.status:
            raise P2PError("Invalid status passed")

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

        try:
            response = self._execute_request(query=self.__query, variables=__variables)
            check_response(P2PError, response)
        except (P2PError, ClientError) as e:
            return e.args
        else:
            return response["data"]["getOrders"]

    def getMarketBook(self):
        """Retrieves market history.

        Returns:
            response: A JSON object containing response from the request.

        """
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

        try:
            response = self._execute_request(query=self.__query)
            check_response(P2PError, response)
        except (P2PError, ClientError) as e:
            return e.args
        return response['data']['getMarketBook']
