from buycoins.client import BuyCoinsClient
from buycoins.errors import check_response
from buycoins.exceptions import AccountError, ClientError


class NGNT(BuyCoinsClient):
    """The NGNT class handles the generations of virtual bank deposit account.
    """

    def createDepositAccount(self, accountName: str):
        """Creates a virtual deposit account under the supplied name.

        Args:
            accountName (str): Name of the new virtual deposit account to be generated*.

        Returns:
            response: A JSON object containing the response from the request.

        """

        if not accountName:
            raise AccountError("Invalid account name passed")

        self.accountName = accountName

        __variables = {
            "accountName": self.accountName
        }

        self.__query = """
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
        try:
            response = self._execute_request(query=self.__query, variables=__variables)
            check_response(AccountError, response)
        except (AccountError, ClientError) as e:
            return e.args
        else:
            return response["data"]["createDepositAccount"]

    def getBalances(self):
        """Retrieves user cryptocurrency balances>

        Returns:
            response: A JSON object containing the user crypotcurrency balances.

        """

        self.__query = """
            query {
                getBalances {
                    id
                    cryptocurrency
                    confirmedBalance
                }
            }
        """

        try:
            response = self._execute_request(query=self.__query)
            check_response(AccountError, response)
        except (AccountError, ClientError) as e:
            return e.args
        else:
            return response["data"]["getBalances"]
