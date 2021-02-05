from unittest.mock import Mock
from buycoins import NGNT
from tests.mock_responses import createDepositAccount

NGNT = Mock()


def test_setting_account_name():
    NGNT.create_deposit_account.return_value = createDepositAccount

    response = NGNT.create_deposit_account("Buycoins Africa")
    assert response["accountName"] == "Buycoins Africa"
    assert response["accountNumber"] == 12345678901
    assert response["accountType"] == "deposit"
    assert response["bankName"] == "Providus Bank"
    assert response["accountReference"] == "abcdefgh-12v4-nu38-89ff-278974r48"


# def test_invalid_accountname():
#     invalid_deposit_account = NGNT.create_deposit_account("")
#     assert invalid_deposit_account["status"] == "AccountError"
#     assert invalid_deposit_account["code"] == 400
#     assert invalid_deposit_account["message"] == "Invalid account name passed"
