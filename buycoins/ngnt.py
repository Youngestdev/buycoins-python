from buycoins.client import BuyCoinsClient


class NGNT(BuyCoinsClient):
    def __init__(self, auth_key: str):
        super().__init__(auth_key)

    def createDepositAccount(self, accountName: str):
        """Creates a virtual deposit account under the supplied name.

        Args:
            accountName (str): Name of the new virtual deposit account.

        Returns:
            response: A JSON object containing the response from the request.

        """
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

        return request