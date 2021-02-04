from buycoins.client import BuyCoinsClient
from buycoins.exceptions import P2PError, ClientError, ServerError
from buycoins.exceptions.utils import check_response


class P2P(BuyCoinsClient):
    """The P2P class handles peer-2-peer transactions."""

    supported_cryptocurrencies = ["bitcoin", "ethereum", "litecoin", "naira_token", "usd_coin", "usd_tether"]
    side = ["buy", "sell"]
    status = ["open", "completed"]

    def get_prices(self):
        """Returns the current price for supported cryptocurrencies on BuyCoins

        Returns:
            response: An array of cryptocurrency data.

        """

        try:
            self._query = """
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

            response = self._execute_request(query=self._query)
            check_response(response, P2PError)
        except (P2PError, ClientError, ServerError) as e:
            return e.response
        else:
            return response["data"]["getPrices"]

    def get_current_price(self, order_side: str = "buy", currency: str = "bitcoin"):
        """Retrieves the current `side` price for the supplied cryptocurrency.

        Args:
            order_side (str):  The order side which can either be buy or sell.
            currency (str): The cryptocurrency whose current price is to be retrieved.

        Returns:
            response: A JSON object containing response from the request.
        """
        try:
            if currency not in self.supported_cryptocurrencies:
                raise P2PError("Invalid or unsupported cryptocurrency", 400)

            if order_side not in self.side:
                raise P2PError("Invalid order side", 400)

            self._query = """
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

            _variables = {"side": order_side, "currency": currency}

            response = self._execute_request(query=self._query, variables=_variables)
            check_response(response, P2PError)
        except (P2PError, ClientError, ServerError) as e:
            return e.response
        else:
            return response["data"]["getPrices"]

    def get_dynamic_price_expiry(self, status: str = "open", side: str = "buy", currency: str = "bitcoin"):
        """Retrieves the dynamic prices for available cryptocurrencies.

        Args:
            status (str): The status of the current order.

        Returns:
            response: A JSON object containing the response from the request.

        """

        try:

            if status not in self.status:
                raise P2PError("Invalid status passed", 400)

            if side not in self.side:
                raise P2PError("Invalid side passed", 400)

            if currency not in self.supported_cryptocurrencies:
                raise P2PError("Invalid or unsupported cryptocurrency", 400)

            self._query = """
                query GetOrders($status: GetOrdersStatus!){
                    getOrders(status: $status) {
                        dynamicPriceExpiry    
                    }
                }
            """

            _variables = {
                "status": status,
            }

            response = self._execute_request(query=self._query, variables=_variables)
            check_response(response, P2PError)
        except (P2PError, ClientError, ServerError) as e:
            return e.response
        else:
            return response["data"]["getOrders"]

    def place_limit_order(self, order_side: str = "buy", coin_amount: float = 0.01, currency: str = "bitcoin", static_price: int = 100000, price_type: str = "static"):
        """Places limit order for the supplied cryptocurrency.

        Args:
            order_side (str): The side of the order. This could be `buy` or `sell`.
            coin_amount (str): The amount the limit order is based on.
            currency (str): The cryptocurrency involved in the limit order.
            static_price (str, optional): Static price for the cryptocurrency in Naira.
            price_type (str): Static or dynamic price for the cryptocurrency.

        Returns:
            response: A JSON object containing the result from the request.

        """

        try:
            if order_side not in self.side:
                raise P2PError("Invalid side passed", 400)

            if currency not in self.supported_cryptocurrencies:
                raise P2PError("Invalid or unsupported cryptocurrency", 400)

            self._query = """
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

            _variables = {"orderSide": order_side, "coinAmount": coin_amount, "cryptocurrency": currency, "staticPrice": static_price, "priceType": price_type}

            response = self._execute_request(query=self._query, variables=_variables)
            check_response(response, P2PError)
        except (P2PError, ClientError, ServerError) as e:
            return e.response
        else:
            return response["data"]["postLimitOrder"]

    def post_market_order(self, order_side: str = "buy", coin_amount: float = 0.01, currency: str = "bitcoin"):
        """Posts a market order for the supplied cryptocurrency.

        Args:
            order_side (str): The type of order to be placed. It could either be `buy` or `sell`.
            coin_amount (float): Amount of coin to be sold.
            currency (str): Cryptocurrency involved in the market order.

        Returns:
            response: A JSON object containing the response from the request.

        """

        try:
            if order_side not in self.side:
                raise P2PError("Invalid side passed", 400)

            if currency not in self.supported_cryptocurrencies:
                raise P2PError("Invalid or unsupported cryptocurrency", 400)

            self._query = """
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

            _variables = {
                "orderSide": order_side,
                "coinAmount": coin_amount,
                "cryptocurrency": currency,
            }

            response = self._execute_request(query=self._query, variables=_variables)
            check_response(response, P2PError)
        except (P2PError, ClientError, ServerError) as e:
            return e.response
        else:
            return response["data"]["postMarketOrder"]

    def get_orders(self, status: str = "open"):
        """Retrieves orders based on their status.

        Args:
            status (str): Status of the order which could either be `open` or `completed`.

        Returns:
            response: A JSON object containing the response from the request.

        """
        try:
            if status not in self.status:
                raise P2PError("Invalid status passed", 400)

            self._query = """
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

            _variables = {"status": status}

            response = self._execute_request(query=self._query, variables=_variables)
            check_response(response, P2PError)
        except (P2PError, ClientError, ServerError) as e:
            return e.response
        else:
            return response["data"]["getOrders"]

    def get_market_book(self):
        """Retrieves market history.

        Returns:
            response: A JSON object containing response from the request.

        """

        try:
            self._query = """
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

            response = self._execute_request(query=self._query)
            check_response(response, P2PError)
        except (P2PError, ClientError, ServerError) as e:
            return e.response
        return response["data"]["getMarketBook"]
