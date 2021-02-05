from unittest.mock import Mock

from buycoins import P2P
from tests.mock_responses import (
    coins_price,
    coin_price,
    get_orders,
    get_market_book,
    open_status_dynamic_price,
    completed_status_dynamic_price,
    post_market_order,
    place_limit_order,
)

P2P = Mock()


def test_coins_price():
    P2P.get_prices.return_value = coins_price
    response = P2P.get_prices()
    assert response["getPrices"][0]["id"] == "QnV5Y29pbnNQcmljZS0wMTdjYzBlMS05NWFjLTQ5N2YtODg4Mi0yNjU1NDRiNGRmODM="
    assert response["getPrices"][0]["cryptocurrency"] == "bitcoin"
    assert response["getPrices"][0]["buyPricePerCoin"] == "18073103.62"
    assert response["getPrices"][0]["minBuy"] == "0.001"
    assert response["getPrices"][0]["maxBuy"] == "2.37516974"
    assert response["getPrices"][0]["expiresAt"] == 1612430322

    assert response["getPrices"][1]["id"] == "QnV5Y29pbnNQcmljZS0wOTM1NmM1Mi0zZTAyLTRjMjgtYWIzMy00Y2Q0ZDY3OGMzMGM="
    assert response["getPrices"][1]["cryptocurrency"] == "ethereum"
    assert response["getPrices"][1]["buyPricePerCoin"] == "782639.91"
    assert response["getPrices"][1]["minBuy"] == "0.02"
    assert response["getPrices"][1]["maxBuy"] == "54.84837368"
    assert response["getPrices"][1]["expiresAt"] == 1612430323

    assert response["getPrices"][2]["id"] == "QnV5Y29pbnNQcmljZS1hODdhZmE3Ny02OGI2LTQ2N2ItYjhkNS05OWI4N2QzZTlhMzE="
    assert response["getPrices"][2]["cryptocurrency"] == "litecoin"
    assert response["getPrices"][2]["buyPricePerCoin"] == "71365.489"
    assert response["getPrices"][2]["minBuy"] == "0.1"
    assert response["getPrices"][2]["maxBuy"] == "601.50258679"
    assert response["getPrices"][2]["expiresAt"] == 1612430327

    assert response["getPrices"][3]["id"] == "QnV5Y29pbnNQcmljZS0zYmU5Yzk5NC0zYmY4LTQ3MmItYjEwZi0wNTk5NWM3ZmMzZmM="
    assert response["getPrices"][3]["cryptocurrency"] == "usd_coin"
    assert response["getPrices"][3]["buyPricePerCoin"] == "485.81"
    assert response["getPrices"][3]["minBuy"] == "5"
    assert response["getPrices"][3]["maxBuy"] == "88360.73"
    assert response["getPrices"][3]["expiresAt"] == 1612430325


def test_coin_price():
    P2P.get_current_price.return_value = coin_price

    response = P2P.get_current_price(order_side="buy", currency="bitcoin")
    assert response["getPrices"]["buyPricePerCoin"] == "17164294"
    assert response["getPrices"]["cryptocurrency"] == "bitcoin"
    assert response["getPrices"]["id"] == "QnV5Y29pbnNQcmljZS05NjNmZTExOS02ZGVhLTRlMDItYTc3NC1lZjViYjk3YWZiNGE="
    assert response["getPrices"]["maxBuy"] == "24.90738193"
    assert response["getPrices"]["maxSell"] == "12.6217372"
    assert response["getPrices"]["minBuy"] == "0.001"
    assert response["getPrices"]["minCoinAmount"] == "0.001"
    assert response["getPrices"]["minSell"] == "0.001"
    assert response["getPrices"]["sellPricePerCoin"] == "16824359.1781"
    assert response["getPrices"]["status"] == "active"


def test_open_dynamic_price():
    P2P.get_dynamic_price_expiry.return_value = open_status_dynamic_price

    response = P2P.get_dynamic_price_expiry()
    assert response["dynamicPriceExpiry"] == 1612305372


def test_completed_dynamic_price():
    P2P.get_dynamic_price_expiry.return_value = completed_status_dynamic_price

    response = P2P.get_dynamic_price_expiry(status="completed")
    assert response["dynamicPriceExpiry"] == 1612304472


def test_place_limit_order():
    P2P.place_limit_order.return_value = place_limit_order

    response = P2P.place_limit_order("buy", 1, "bitcoin", 16000000)
    assert response["id"] == "UG9zdE9yZGVyLTgwY2M3MjdmLWQzYjEtNDE0OS04MDg3LTJkNjI0MDdhMWMzMw"
    assert response["cryptocurrency"] == "bitcoin"
    assert response["coinAmount"] == 1.0
    assert response["side"] == "buy"
    assert response["status"] == "inactive"
    assert response["createdAt"] == 1612307038
    assert response["pricePerCoin"] == "16000000.0"
    assert response["priceType"] == "static"
    assert response["dynamicExchangeRate"] == None


def test_post_market_order():
    P2P.post_market_order.return_value = post_market_order

    response = P2P.post_market_order("sell", 0.01, "bitcoin")
    assert response["id"] == "UG9zdE9yZGVyLTgwY2M3MjdmLWQzYjEtNDE0OS04MDg3LTJkNjI0MDdhMWMzMw"
    assert response["cryptocurrency"] == "bitcoin"
    assert response["coinAmount"] == 0.01
    assert response["side"] == "sell"
    assert response["status"] == "inactive"
    assert response["createdAt"] == 1612307038
    assert response["pricePerCoin"] == "16000000.0"
    assert response["priceType"] == None
    assert response["staticPrice"] == None
    assert response["dynamicExchangeRate"] == None


def test_get_orders():
    P2P.get_orders.return_value = get_orders

    response = P2P.get_orders("open")
    assert response["dynamicPriceExpiry"] == 1612308792
    assert response["orders"] == {"edges": []}


def test_get_market_book():
    P2P.get_market_book.return_value = get_market_book

    response = P2P.get_market_book()
    assert response["dynamicPriceExpiry"] == 1612309392
    assert response["orders"] == {
        "edges": [
            {
                "node": {
                    "id": "UG9zdE9yZGVyLTdjZmIxMTFiLTIyMjEtNGEyNS1iMTUwLTI2YmRhZjdlY2RiMw==",
                    "cryptocurrency": "bitcoin",
                    "coinAmount": "0.003196",
                    "side": "buy",
                    "status": "active",
                    "createdAt": 1612308511,
                    "pricePerCoin": "1650000000",
                    "priceType": "static",
                    "staticPrice": "1650000000",
                    "dynamicExchangeRate": None,
                }
            }
        ]
    }
