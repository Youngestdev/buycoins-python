from requests import HTTPError
from requests.models import Response


def check_response(exception, response, error_code):
    """Checks for exceptions and raises them.

    Args:
        exception (): Class of exception to be raised.
        response (): Response object to be checked against.

    Returns:

    """
    if type(response) == Response:
        return {
            "status_code": response.status_code,
            "message": response.reason
        }

    if "errors" in response:
        error = response["errors"]
        raise exception(error[0]["message"], error_code)

    return None