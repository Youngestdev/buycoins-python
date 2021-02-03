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
        message = "{}: Failed to establish a connection".format(response.__doc__)
        raise ClientError(message, 404)
    elif type(response) == HTTPError:
        status_code = response.response.status_code
        if str(status_code).startswith('4'):
            json_response = response.response.json()
            error_message = json_response['errors']
            raise ClientError(error_message, status_code)
        else:
            error_message = response.__doc__
            raise ClientError(error_message, status_code)
    elif "errors" in response:
        error = response["errors"][0]
        error_message = error["message"]
        raise exception(error_message, 404)
