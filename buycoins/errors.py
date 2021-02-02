from requests import HTTPError

from buycoins.exceptions import ClientError


def check_response(exception, response):
    """Checks for exceptions and raises them.

    Args:
        exception (): Class of exception to be raised.
        response (): Response object to be checked against.

    Returns:

    """
    if type(response) == HTTPError:
        raise ClientError("Invalid Authentication Key!")

    if "errors" in response:
        error = response["errors"]
        raise exception(error[0]["message"])
