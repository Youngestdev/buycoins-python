import pytest

createDepositAccount = dict(
    accountNumber=12345678901,
    accountName="Buycoins Africa",
    accountType="deposit",
    bankName="Providus Bank",
    accountReference="abcdefgh-12v4-nu38-89ff-278974r48",
)


coins_price = dict(
    getPrices=[
        dict(
            id="QnV5Y29pbnNQcmljZS0wMTdjYzBlMS05NWFjLTQ5N2YtODg4Mi0yNjU1NDRiNGRmODM=",
            cryptocurrency="bitcoin",
            buyPricePerCoin="18073103.62",
            minBuy="0.001",
            maxBuy="2.37516974",
            expiresAt=1612430322,
        ),
        dict(
            id="QnV5Y29pbnNQcmljZS0wOTM1NmM1Mi0zZTAyLTRjMjgtYWIzMy00Y2Q0ZDY3OGMzMGM=",
            cryptocurrency="ethereum",
            buyPricePerCoin="782639.91",
            minBuy="0.02",
            maxBuy="54.84837368",
            expiresAt=1612430323,
        ),
        dict(
            id="QnV5Y29pbnNQcmljZS1hODdhZmE3Ny02OGI2LTQ2N2ItYjhkNS05OWI4N2QzZTlhMzE=",
            cryptocurrency="litecoin",
            buyPricePerCoin="71365.489",
            minBuy="0.1",
            maxBuy="601.50258679",
            expiresAt=1612430327,
        ),
        dict(
            id="QnV5Y29pbnNQcmljZS0zYmU5Yzk5NC0zYmY4LTQ3MmItYjEwZi0wNTk5NWM3ZmMzZmM=",
            cryptocurrency="usd_coin",
            buyPricePerCoin="485.81",
            minBuy="5",
            maxBuy="88360.73",
            expiresAt=1612430325,
        ),
    ]
)

coin_price = dict(
    getPrices=dict(
        buyPricePerCoin="17164294",
        cryptocurrency="bitcoin",
        id="QnV5Y29pbnNQcmljZS05NjNmZTExOS02ZGVhLTRlMDItYTc3NC1lZjViYjk3YWZiNGE=",
        maxBuy="24.90738193",
        maxSell="12.6217372",
        minBuy="0.001",
        minCoinAmount="0.001",
        minSell="0.001",
        sellPricePerCoin="16824359.1781",
        status="active",
    )
)

open_status_dynamic_price = dict(dynamicPriceExpiry=1612305372)

completed_status_dynamic_price = dict(dynamicPriceExpiry=1612304472)

place_limit_order = dict(
    id="UG9zdE9yZGVyLTgwY2M3MjdmLWQzYjEtNDE0OS04MDg3LTJkNjI0MDdhMWMzMw",
    cryptocurrency="bitcoin",
    coinAmount=1.0,
    side="buy",
    status="inactive",
    createdAt=1612307038,
    pricePerCoin="16000000.0",
    priceType="static",
    staticPrice="16000000",
    dynamicExchangeRate=None,
)

post_market_order = dict(
    id="UG9zdE9yZGVyLTgwY2M3MjdmLWQzYjEtNDE0OS04MDg3LTJkNjI0MDdhMWMzMw",
    cryptocurrency="bitcoin",
    coinAmount=0.01,
    side="sell",
    status="inactive",
    createdAt=1612307038,
    pricePerCoin="16000000.0",
    priceType=None,
    staticPrice=None,
    dynamicExchangeRate=None,
)

get_orders = dict(dynamicPriceExpiry=1612308792, orders=dict(edges=[]))

get_market_book = dict(
    dynamicPriceExpiry=1612309392,
    orders=dict(
        edges=[
            dict(
                node=dict(
                    id="UG9zdE9yZGVyLTdjZmIxMTFiLTIyMjEtNGEyNS1iMTUwLTI2YmRhZjdlY2RiMw==",
                    cryptocurrency="bitcoin",
                    coinAmount="0.003196",
                    side="buy",
                    status="active",
                    createdAt=1612308511,
                    pricePerCoin="1650000000",
                    priceType="static",
                    staticPrice="1650000000",
                    dynamicExchangeRate=None,
                )
            )
        ]
    ),
)

buy = dict(
    id="QnV5Y29pbnNQcmljZS05NjNmZTExOS02ZGVhLTRlMDItYTc3NC1lZjViYjk3YWZiNGE=",
    cryptocurrency="bitcoin",
    status="processing",
    totalCoinAmount=0.01,
    side="buy",
)

sell = dict(
    id="QnV5Y29pbnNQcmljZS05NjNmZTExOS02ZGVhLTRlMDItYTc3NC1lZjViYjk3YWZiNGE=",
    cryptocurrency="usd_tether",
    status="processing",
    totalCoinAmount=0.002,
    side="sell",
)


send = dict(
    id="QnV5Y29pbnNQ=",
    address="1MmyYvSEYLCPm45Ps6vQin1heGBv3UpNbf",
    amount=0.02,
    cryptocurrency="bitcoin",
    fee=0.01,
    status="processing",
    transaction=dict(
        txhash="hybuojpkllmjvvcdersxkjijmkllbvdsabl",
        id="QnV5Y29pbnNQ=",
    ),
)

getEstimatedNetworkFee = dict(
    estimatedFee=0.00044,
    total=0.01044,
)

createAddress = dict(cryptocurrency="usd_tether", address="0x3856c5511ac5344eb85d439e338ae0f1b5dbe34a")

bitcoin_balance = dict(getBalances=[dict(id="QWNjb3VudC0=", cryptocurrency="bitcoin", confirmedBalance=0.009)])

all_coins_balances = dict(
    getBalances=[
        dict(id="QWNjb3VudC0=", cryptocurrency="usd_tether", confirmedBalance=0.0),
        dict(id="QWNjb3VudC0=", cryptocurrency="naira_token", confirmedBalance=0.0),
        dict(id="QWNjb3VudC0=", cryptocurrency="bitcoin", confirmedBalance=0.009),
        dict(id="QWNjb3VudC0=", cryptocurrency="ethereum", confirmedBalance=1.000),
        dict(id="QWNjb3VudC0=", cryptocurrency="litecoin", confirmedBalance=0.0),
        dict(id="QWNjb3VudC0=", cryptocurrency="usd_coin", confirmedBalance=0.0),
    ]
)
