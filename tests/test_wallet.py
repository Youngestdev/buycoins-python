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
#Mock buy_crypto price_id and return value

#Mock sell_crypto return value

#Mock send_crypto return value



def test_buy_coins():
    Wallet.buy_crypto.return_value = buy_crypto_coin
    response = Wallet.buy_crypto(currency="bitcoin", coin_amount=0.01)

    assert response["buy"]["cryptocurrency"] == "bitcoin"
    assert response["buy"]["id"] == "QnV5Y29pbnNQcmljZS05NjNmZTExOS02ZGVhLTRlMDItYTc3NC1lZjViYjk3YWZiNGE="
    assert response["buy"]["totalCoinAmount"] == 0.01
    assert response["buy"]["side"] == "buy"

def test_sell_coins():
    Wallet.sell_crypto.return_value = sell_crypto_coin
    response = Wallet.sell_crypto(currency="usd_tether", coin_amount=0.002)

    assert response["sell"]["cryptocurrency"] == "usd_tether"
    assert response["sell"]["id"] == "QnV5Y29pbnNQcmljZS05NjNmZTExOS02ZGVhLTRlMDItYTc3NC1lZjViYjk3YWZiNGE="
    assert response["sell"]["totalCoinAmount"] == 0.002
    assert response["sell"]["side"] == "sell"

def test_send_coins():
    Wallet.send_crypto.return_value = send_crypto_coin
    response = Wallet.send_crypto(currency="bitcoin", coin_amount=0.03, address="1MmyYvSEYLCPm45Ps6vQin1heGBv3UpNbf")

    assert response["send"]["cryptocurrency"] == "bitcoin"
    assert response["send"]["address"] == "1MmyYvSEYLCPm45Ps6vQin1heGBv3UpNbf"
    assert response["send"]["transaction"]["txhash"] == "hybuojpkllmjvvcdersxkjijmkllbvdsabl"

def test_network_fee():
    Wallet.get_network_fee.return_value = network_fee
    response = Wallet.get_network_fee(currency="bitcoin", coin_amount=0.01)

    assert response["getEstimatedNetworkFee"]["estimatedFee"] == 0.00044
    assert response["getEstimatedNetworkFee"]["total"] == 0.01044


def test_create_address():
    Wallet.create_address.return_value = address
    response = Wallet.create_address(currency="usd_tether")

    assert response["createAddress"]["cryptocurrency"] == "usd_tether"
    assert response["createAddress"]["address"] == "0x3856c5511ac5344eb85d439e338ae0f1b5dbe34a"


def test_get_bitcoin_balace():
    Wallet.get_balances.return_value = bitcoin_balance
    response = Wallet.get_balances(currency="bitcoin")

    assert response["getBalances"][0]["id"] == "QWNjb3VudC0="
    assert response["getBalances"][0]["cryptocurrency"] == "bitcoin"
    assert response["getBalances"][0]["confirmedBalance"] == 0.009
    assert len(response["getBalances"]) == 1


def test_get_all_coins_balace():
    Wallet.get_balances.return_value = all_coins_balances
    response = Wallet.get_balances()

    assert response["getBalances"][2]["id"] == "QWNjb3VudC0="
    assert response["getBalances"][2]["cryptocurrency"] == "bitcoin"
    assert response["getBalances"][2]["confirmedBalance"] == 0.009

    assert response["getBalances"][3]["id"] == "QWNjb3VudC0="
    assert response["getBalances"][3]["cryptocurrency"] == "ethereum"
    assert response["getBalances"][3]["confirmedBalance"] == 1.000
