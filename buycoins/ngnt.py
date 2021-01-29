from buycoins.client import BuyCoinsClient
from buycoins.exceptions import AccountError


class NGNT(BuyCoinsClient):
    """The NGNT class handles the generations of virtual bank deposit account.

    Args:
        auth_key (str): Authentication key in `public_key:private_key` string form.


    """

    def __init__(self, auth_key: str):
        super().__init__(auth_key)

    def createDepositAccount(self, accountName: str):
        """Creates a virtual deposit account under the supplied name.

        Args:
            accountName (str): Name of the new virtual deposit account to be generated*.

        Returns:
            response: A JSON object containing the response from the request.

        """

        if not accountName:
            raise AccountError("Invalid account name passed")

        variables = {
            "accountName": accountName
        }

        self.query = """
            mutation createDepositAccount($accountName: String!) {
                createDepositAccount(accountName: $accountName) {
                    accountNumber
                    accountName
                    accountType
                    bankName
                    accountReference
              }
            }
        """

        request = self._execute_request(query=self.query, variables=variables)

        return request['data']['createDepositAccount']
