import hashlib
import hmac


class Webhook:
    """The Webhook class is responsible for verifying requests sent to your BuyCoins webhook URL.

    """

    def __init__(self, body: bytes, token: str, header_signature: str = "X-Webhook-Signature"):
        """

        Args:
            body (): request body from BuyCoins
            token (): BuyCoins generated webhook token
            header_signature (): "X-Webhook-Signature header"
        """
        self.token = token
        self.body = body
        self.header_signature = header_signature

    def verifyRequest(self):
        """Verify the supplied request.

        Returns:
            Bool: `True` if the request originated from BuyCoins or `False ` if the request didn't originate from BuyCoins
        """
        signed_key = self.token.encode("utf-8")
        if type(self.body) != bytes:
            self.body = bytes(self.body)

        supplied_value = hmac.new(signed_key, self.body, hashlib.sha1)
        return supplied_value == self.header_signature
