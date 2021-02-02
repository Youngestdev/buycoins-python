from buycoins.client import BuyCoinsClient
from buycoins.exceptions import AccountError, ClientError
from buycoins.utils import check_response


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
        try:
            if not accountName:
                raise AccountError("Invalid account name passed", 404)

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
            response = self._execute_request(query=self.__query, variables=__variables)
            check_response(response, AccountError)
        except (AccountError, ClientError) as e:
            return e.response
        else:
            return response