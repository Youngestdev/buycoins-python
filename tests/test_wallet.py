from unittest.mock import Mock

from buycoins import Wallet
from tests.mock_responses import (
    getEstimatedNetworkFee,
    createAddress,
    all_coins_balances,
    bitcoin_balance,
    buy,
    sell,
    send,
)


Wallet = Mock()


def test_buy_coins():
    Wallet.buy_crypto.return_value = buy
    response = Wallet.buy_crypto(currency="bitcoin", coin_amount=0.01)

    assert response["cryptocurrency"] == "bitcoin"
    assert response["id"] == "QnV5Y29pbnNQcmljZS05NjNmZTExOS02ZGVhLTRlMDItYTc3NC1lZjViYjk3YWZiNGE="
    assert response["totalCoinAmount"] == 0.01
    assert response["side"] == "buy"


def test_sell_coins():
    Wallet.sell_crypto.return_value = sell
    response = Wallet.sell_crypto(currency="usd_tether", coin_amount=0.002)

    assert response["cryptocurrency"] == "usd_tether"
    assert response["id"] == "QnV5Y29pbnNQcmljZS05NjNmZTExOS02ZGVhLTRlMDItYTc3NC1lZjViYjk3YWZiNGE="
    assert response["totalCoinAmount"] == 0.002
    assert response["side"] == "sell"


def test_send_coins():
    Wallet.send_crypto.return_value = send
    response = Wallet.send_crypto(currency="bitcoin", coin_amount=0.03, address="1MmyYvSEYLCPm45Ps6vQin1heGBv3UpNbf")

    assert response["cryptocurrency"] == "bitcoin"
    assert response["address"] == "1MmyYvSEYLCPm45Ps6vQin1heGBv3UpNbf"
    assert response["transaction"]["txhash"] == "hybuojpkllmjvvcdersxkjijmkllbvdsabl"


def test_network_fee():
    Wallet.get_network_fee.return_value = getEstimatedNetworkFee
    response = Wallet.get_network_fee(currency="bitcoin", coin_amount=0.01)

    assert response["estimatedFee"] == 0.00044
    assert response["total"] == 0.01044


def test_create_address():
    Wallet.create_address.return_value = createAddress
    response = Wallet.create_address(currency="usd_tether")

    assert response["cryptocurrency"] == "usd_tether"
    assert response["address"] == "0x3856c5511ac5344eb85d439e338ae0f1b5dbe34a"


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
