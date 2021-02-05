from tests.utils import _mock_request
from tests.class_fixtures import wallet_user
from buycoins import Wallet
from tests.mock_responses import (
    network_fee,
    address,
    all_coins_balances,
    bitcoin_balance,
    buy_crypto_coin,
    sell_crypto_coin,
    send_crypto_coin,
)
from unittest.mock import Mock, patch

Wallet = Mock()
price_id = "QnV5Y29pbnNQcmljZS05NjNmZTExOS02ZGVhLTRlMDItYTc3NC1lZjViYjk3YWZiNGE="
#Mock buy_crypto price_id and return value
Wallet.buy_crypto.price_id = price_id
Wallet.buy_crypto.return_value = buy_crypto_coin

#Mock sell_crypto price_id and return value
Wallet.sell_crypto.price_id = price_id
Wallet.sell_crypto.return_value = sell_crypto_coin

#Mock send_crypto return value
Wallet.send_crypto.return_value = send_crypto_coin

def test_buy_coins():
    response = Wallet.buy_crypto(currency="bitcoin", coin_amount=0.01)

    assert response["buy"]["cryptocurrency"] == "bitcoin"
    assert response["buy"]["id"] == price_id
    assert response["buy"]["totalCoinAmount"] == 0.01
    assert response["buy"]["side"] == "buy"

def test_sell_coins():
    response = Wallet.sell_crypto(currency="usd_tether", coin_amount=0.002)

    assert response["sell"]["cryptocurrency"] == "usd_tether"
    assert response["sell"]["id"] == price_id
    assert response["sell"]["totalCoinAmount"] == 0.002
    assert response["sell"]["side"] == "sell"

def test_send_coins():
    response = Wallet.send_crypto(currency="bitcoin", coin_amount=0.03, address="1MmyYvSEYLCPm45Ps6vQin1heGBv3UpNbf")

    assert response["send"]["cryptocurrency"] == "bitcoin"
    assert response["send"]["address"] == "1MmyYvSEYLCPm45Ps6vQin1heGBv3UpNbf"
    assert response["send"]["transaction"]["txhash"] == "hybuojpkllmjvvcdersxkjijmkllbvdsabl"

def test_network_fee(wallet_user):
    _mock_request(network_fee)
    response = wallet_user.get_network_fee(currency="bitcoin", coin_amount=0.01)

    assert response["estimatedFee"] == 0.00044
    assert response["total"] == 0.01044


def test_create_address(wallet_user):
    _mock_request(address)
    response = wallet_user.create_address(currency="usd_tether")

    assert response["cryptocurrency"] == "usd_tether"
    assert response["address"] == "0x3856c5511ac5344eb85d439e338ae0f1b5dbe34a"


def test_get_bitcoin_balace(wallet_user):
    _mock_request(bitcoin_balance)
    response = wallet_user.get_balances(currency="bitcoin")

    assert response[0]["id"] == "QWNjb3VudC0="
    assert response[0]["cryptocurrency"] == "bitcoin"
    assert response[0]["confirmedBalance"] == 0.009


def test_get_all_coins_balace(wallet_user):
    _mock_request(all_coins_balances)
    response = wallet_user.get_balances()

    assert response[2]["id"] == "QWNjb3VudC0="
    assert response[2]["cryptocurrency"] == "bitcoin"
    assert response[2]["confirmedBalance"] == 0.009

    assert response[3]["id"] == "QWNjb3VudC0="
    assert response[3]["cryptocurrency"] == "ethereum"
    assert response[3]["confirmedBalance"] == 1.000
