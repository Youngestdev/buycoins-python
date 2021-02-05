from tests.class_fixtures import buycoins_user
from tests.mock_responses import ngnt_account
from tests.utils import _mock_request


def test_setting_accountname(buycoins_user):
    _mock_request(ngnt_account)
    create_deposit_account = buycoins_user.create_deposit_account("Buycoins Africa")
    assert create_deposit_account["accountName"] == "Buycoins Africa"
    assert create_deposit_account["accountNumber"] == 12345678901
    assert create_deposit_account["accountType"] == "deposit"
    assert create_deposit_account["bankName"] == "Providus Bank"
    assert create_deposit_account["accountReference"] == "abcdefgh-12v4-nu38-89ff-278974r48"


def test_invalid_accountname(buycoins_user):
    invalid_deposit_account = buycoins_user.create_deposit_account("")
    assert invalid_deposit_account["status"] == "AccountError"
    assert invalid_deposit_account["code"] == 400
    assert invalid_deposit_account["message"] == "Invalid account name passed"
