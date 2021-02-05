import pytest
from buycoins import *


@pytest.fixture(autouse=True)
def buycoins_user():
    """

    Returns: An authenticated instance of the `NGNT` class.

    """

    buycoins_user = NGNT()
    return buycoins_user


@pytest.fixture(autouse=True)
def p2p_user():
    """

    Returns: An authenticated instance of the `P2P` class

    """

    p2p_user = P2P()
    return p2p_user


@pytest.fixture(autouse=True)
def wallet_user():
    """

    Returns: An authenticated instance of the `Wallet` class

    """

    wallet_user = Wallet()
    return wallet_user
