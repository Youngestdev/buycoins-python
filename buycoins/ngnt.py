from buycoins.client import BuyCoinsClient
from buycoins.exceptions import AccountError, ClientError, ServerError
from buycoins.exceptions.utils import check_response


class NGNT(BuyCoinsClient):
    """The NGNT class handles the generations of virtual bank deposit account."""

    def create_deposit_account(self, account_name: str):
        """Creates a virtual deposit account under the supplied name.

        Args:
            account_name (str): Name of the new virtual deposit account to be generated*.

        Returns:
            response: A JSON object containing the response from the request.

        """
        try:
            if not account_name:
                raise AccountError("Invalid account name passed", 400)

            self.account_name = account_name

            _variables = {"accountName": self.account_name}

            self._query = """
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
            response = self._execute_request(query=self._query, variables=_variables)
            check_response(response, AccountError)
        except (AccountError, ClientError, ServerError) as e:
            return e.response
        else:
            return response["data"]["createDepositAccount"]
