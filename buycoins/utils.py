from requests.exceptions import HTTPError, ConnectionError

from buycoins.exceptions import ClientError


def check_response(response, exception):
    """Checks the request"s response to raise any possible exception.

    Args:
        response (): Response object
        exception (): Exception class to be raised: WalletError, P2PError, NGNTError

    Returns:
        None

    """
    if not exception:
        exception = Exception

    if type(response) == ConnectionError:
        raise ClientError(response.__doc__, 404)
    elif type(response) == HTTPError:
        error = response.response.json()
        error_message = error["errors"]
        status_code = response.response.status_code
        raise ClientError(error_message, status_code)
    elif "errors" in response:
        error = response["errors"][0]
        error_message = error["message"]
        raise exception(error_message, 404)
