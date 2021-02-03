from decouple import config
from python_graphql_client import GraphqlClient
from requests.auth import HTTPBasicAuth
from requests.exceptions import HTTPError, ConnectionError

from buycoins.exceptions import QueryError

auth_key = config("auth_key")

class BuyCoinsClient:
    def __init__(self):
        self.__endpoint = "https://backend.buycoins.tech/api/graphql"
        self.__username = ""
        self.__password = ""
        self.__auth_key = auth_key

    def _split_auth_key(self):
        self.__username, self.__password = self.__auth_key.split(":")

    def _initiate_client(self):
        self._split_auth_key()
        try:
            self.__auth = HTTPBasicAuth(self.__username, self.__password)
            self.__client = GraphqlClient(self.__endpoint, auth=self.__auth)
        except (HTTPError, ConnectionError) as e:
            return e
        else:
            return self.__client

    def _execute_request(self, query: str, variables: dict = {}):
        if not query or query == "":
            raise QueryError("Invalid query passed!", 404)

        try:
            self._initiate_client()
            request = self.__client.execute(query=query, variables=variables)

        except HTTPError as e:
            return e
        except QueryError as e:
            return e.response
        except ConnectionError as e:
            return e
        else:
            return request
