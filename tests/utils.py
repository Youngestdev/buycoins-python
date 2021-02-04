import json

import httpretty

from buycoins.client import ENDPOINT


def _build_response(response: dict):
    """Builds response from mocked request

    Args:
        response (): HTTP mocked request.

    Returns:
        A dictionary object containing mocked response from mocked request.
    """
    return json.dumps(dict(data=response))


def _mock_request(response: dict):
    """Creates and sends a mock request

    Args:
        response (): a dictionary containing the body for the mocked request

    Returns:


    """
    httpretty.register_uri(httpretty.POST, ENDPOINT, body=_build_response(response))
