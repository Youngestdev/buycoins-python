from buycoins.client import BuyCoinsClient


class P2P(BuyCoinsClient):
    """The P2P class handles peer-2-peer transactions.

    Args:
        auth_key (str): Authentication key in `public_key:private_key` string form.
    """

    def __init__(self, auth_key: str):
        super().__init__(auth_key)

    def getCurrentPrice(self, side: str = "buy", currency: str = "bitcoin"):
        """Retrieves the current `side` price for the supplied cryptocurrency.

        Args:
            side (str):  The order side which can either be buy or sell.
            currency (str): The cryptocurrency whose current price is to be retrieved.

        Returns:
            response: A JSON object containing response from the request.
        """
        if not side:
            side = "buy"
        if not currency:
            currency = "bitcoin"

        self.query = """
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

        variables = {
            "side": side,
            "currency": currency
        }

        response = self._execute_request(self.query, variables)
        return response

    def getDynamicPriceExpiry(self, status: str = "open", side: str = "buy", currency: str = "bitcoin"):
        """Retrieves the dynamic price for the supplied cryptocurrency.

        Args:
            status (str): The status of the current order.
            side (str): The order side which can either be buy or sell.
            currency (str): The cryptocurrency whose price is to be retrieved.

        Returns:
            response: A JSON object containing the response from the request.

        """
        self.query = """
            query GetOrders($status: GetOrdersStatus!, $side: OrderSide, $currency: Cryptocurrency){
                getOrders(status: $status, side: $side, cryptocurrency: $currency) {
                    dynamicPriceExpiry    
                }
            }
        """

        variables = {
            "status": status,
            "side": side,
            "currency": currency
        }

        response = self._execute_request(query=self.query, variables=variables)
        return response

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
        self.query = """
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

        variables = {
            "orderside": orderSide,
            "coinAmount": coinAmount,
            "cryptocurrency": currency,
            "staticPrice": staticPrice,
            "priceType": priceType
        }

        response = self._execute_request(query=self.query, variables=variables)
        return response

    def postMarketOrder(self, orderSide: str = "buy", coinAmount: float = 0.01, currency: str = "bitcoin"):
        """Posts a market order for the supplied cryptocurrency.

        Args:
            orderSide (str): The type of order to be placed. It could either be `buy` or `sell`.
            coinAmount (float): Amount of coin to be sold.
            currency (str): Cryptocurrency involved in the market order.

        Returns:
            response: A JSON object containing the response from the request.

        """
        self.query = """
            mutation PostMarketOrder($ordersSide: OrderSide!, $coinAmount: BigDecimal!, $cryptocurrency: Cryptocurrency){
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

        variables = {
            "orderside": orderSide,
            "coinAmount": coinAmount,
            "cryptocurrency": currency,
        }

        response = self._execute_request(query=self.query, variables=variables)
        return response

    def getOrders(self, status: str = "open"):
        """Retrieves orders based on their status.

        Args:
            status (str): Status of the order which could either be `open` or `completed`.

        Returns:
            response: A JSON object containing the response from the request.

        """
        self.query = """
            query GetOrders($status: GetOrdersStatus!){
                getOrders(status: $status, side: $side, cryptocurrency: $currency) {
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

        variables = {
            "status": status
        }

        response = self._execute_request(query=self.query, variables=variables)
        return response

    def getMarketBook(self):
        """Retrieves market history.

        Returns:
            response: A JSON object containing response from the request.

        """
        self.query = """
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

        response = self._execute_request(query=self.query)
        return response
