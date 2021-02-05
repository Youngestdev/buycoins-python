from tests.utils import _mock_request
from tests.class_fixtures import wallet_user
from tests.mock_responses import network_fee, address, all_coins_balances, bitcoin_balance


def test_buy_coins(wallet_user):
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
