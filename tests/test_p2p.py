from tests.class_fixtures import p2p_user
from tests.mock_responses import coins_price, coin_price, get_orders, get_market_book, open_status_dynamic_price, completed_status_dynamic_price, post_market_order, place_limit_order
from tests.utils import _mock_request


def test_coins_price(p2p_user):
    _mock_request(coins_price)
    all_coins_price = p2p_user.get_prices()
    assert all_coins_price[0]["id"] == "QnV5Y29pbnNQcmljZS0wMTdjYzBlMS05NWFjLTQ5N2YtODg4Mi0yNjU1NDRiNGRmODM="
    assert all_coins_price[0]["cryptocurrency"] == "bitcoin"
    assert all_coins_price[0]["buyPricePerCoin"] == "18073103.62"
    assert all_coins_price[0]["minBuy"] == "0.001"
    assert all_coins_price[0]["maxBuy"] == "2.37516974"
    assert all_coins_price[0]["expiresAt"] == 1612430322

    assert all_coins_price[1]["id"] == "QnV5Y29pbnNQcmljZS0wOTM1NmM1Mi0zZTAyLTRjMjgtYWIzMy00Y2Q0ZDY3OGMzMGM="
    assert all_coins_price[1]["cryptocurrency"] == "ethereum"
    assert all_coins_price[1]["buyPricePerCoin"] == "782639.91"
    assert all_coins_price[1]["minBuy"] == "0.02"
    assert all_coins_price[1]["maxBuy"] == "54.84837368"
    assert all_coins_price[1]["expiresAt"] == 1612430323

    assert all_coins_price[2]["id"] == "QnV5Y29pbnNQcmljZS1hODdhZmE3Ny02OGI2LTQ2N2ItYjhkNS05OWI4N2QzZTlhMzE="
    assert all_coins_price[2]["cryptocurrency"] == "litecoin"
    assert all_coins_price[2]["buyPricePerCoin"] == "71365.489"
    assert all_coins_price[2]["minBuy"] == "0.1"
    assert all_coins_price[2]["maxBuy"] == "601.50258679"
    assert all_coins_price[2]["expiresAt"] == 1612430327

    assert all_coins_price[3]["id"] == "QnV5Y29pbnNQcmljZS0zYmU5Yzk5NC0zYmY4LTQ3MmItYjEwZi0wNTk5NWM3ZmMzZmM="
    assert all_coins_price[3]["cryptocurrency"] == "usd_coin"
    assert all_coins_price[3]["buyPricePerCoin"] == "485.81"
    assert all_coins_price[3]["minBuy"] == "5"
    assert all_coins_price[3]["maxBuy"] == "88360.73"
    assert all_coins_price[3]["expiresAt"] == 1612430325


def test_coin_price(p2p_user):
    _mock_request(coin_price)
    current_bitcoin_price = p2p_user.get_current_price(order_side="buy", currency="bitcoin")
    assert current_bitcoin_price["buyPricePerCoin"]
    assert current_bitcoin_price["cryptocurrency"] == "bitcoin"
    assert current_bitcoin_price["id"] == "QnV5Y29pbnNQcmljZS05NjNmZTExOS02ZGVhLTRlMDItYTc3NC1lZjViYjk3YWZiNGE="
    assert current_bitcoin_price["maxBuy"] == "24.90738193"
    assert current_bitcoin_price["maxSell"] == "12.6217372"
    assert current_bitcoin_price["minBuy"] == "0.001"
    assert current_bitcoin_price["minCoinAmount"] == "0.001"
    assert current_bitcoin_price["minSell"] == "0.001"
    assert current_bitcoin_price["sellPricePerCoin"] == "16824359.1781"
    assert current_bitcoin_price["status"] == "active"


def test_open_dynamic_price(p2p_user):
    _mock_request(open_status_dynamic_price)
    open_dynamic_price = p2p_user.get_dynamic_price_expiry()
    assert open_dynamic_price["dynamicPriceExpiry"] == 1612305372


def test_completed_dynamic_price(p2p_user):
    _mock_request(completed_status_dynamic_price)
    completed_dynamic_price = p2p_user.get_dynamic_price_expiry(status="completed")
    assert completed_dynamic_price["dynamicPriceExpiry"] == 1612304472


def test_place_limit_order(p2p_user):
    _mock_request(place_limit_order)
    bitcoin_limit_order = p2p_user.place_limit_order("buy", 1, "bitcoin", 16000000)
    assert bitcoin_limit_order["id"] == "UG9zdE9yZGVyLTgwY2M3MjdmLWQzYjEtNDE0OS04MDg3LTJkNjI0MDdhMWMzMw"
    assert bitcoin_limit_order["cryptocurrency"] == "bitcoin"
    assert bitcoin_limit_order["coinAmount"] == 1.0
    assert bitcoin_limit_order["side"] == "buy"
    assert bitcoin_limit_order["status"] == "inactive"
    assert bitcoin_limit_order["createdAt"] == 1612307038
    assert bitcoin_limit_order["pricePerCoin"] == "16000000.0"
    assert bitcoin_limit_order["priceType"] == "static"
    assert bitcoin_limit_order["dynamicExchangeRate"] == None


def test_post_market_order(p2p_user):
    _mock_request(post_market_order)
    bitcoin_market_order = p2p_user.post_market_order("sell", 0.01, "bitcoin")
    assert bitcoin_market_order["id"] == "UG9zdE9yZGVyLTgwY2M3MjdmLWQzYjEtNDE0OS04MDg3LTJkNjI0MDdhMWMzMw"
    assert bitcoin_market_order["cryptocurrency"] == "bitcoin"
    assert bitcoin_market_order["coinAmount"] == 0.01
    assert bitcoin_market_order["side"] == "sell"
    assert bitcoin_market_order["status"] == "inactive"
    assert bitcoin_market_order["createdAt"] == 1612307038
    assert bitcoin_market_order["pricePerCoin"] == "16000000.0"
    assert bitcoin_market_order["priceType"] == None
    assert bitcoin_market_order["staticPrice"] == None
    assert bitcoin_market_order["dynamicExchangeRate"] == None


def test_get_orders(p2p_user):
    _mock_request(get_orders)
    open_orders = p2p_user.get_orders("open")
    assert open_orders["dynamicPriceExpiry"] == 1612308792
    assert open_orders["orders"] == {"edges": []}


def test_get_market_book(p2p_user):
    _mock_request(get_market_book)
    market_history = p2p_user.get_market_book()
    assert market_history["dynamicPriceExpiry"] == 1612309392
    assert market_history["orders"] == {
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
