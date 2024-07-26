# coding: utf-8
#
# This code was auto generated by AfterShip SDK Generator.
# Do not edit the class manually.

import base64
import hashlib
import hmac
from typing import Dict
from datetime import datetime
from urllib3.util import url

from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_PSS
from Crypto.Hash import SHA256

ApiKey = "API_KEY"
Aes = "AES"
Rsa = "RSA"


class Authenticator:
    def __init__(self, api_key: str, api_secret: str, auth_type: str):
        self._api_key: str = api_key
        self._api_secret: str = api_secret
        self._kind: str = auth_type

    def sign(self, method: str, uri: str, headers: dict, body: str) -> Dict:
        """
        The SignString is generated by Method, Uri, Headers, Body from a HTTP(s) request.

        :param method: str - request method.
        :param uri: str - request URI.
        :param headers: dict - request headers.
        :param body: str - request body.
        """
        headers["as-api-key"] = self._api_key

        if self._kind == ApiKey:
            return headers

        if self._kind != ApiKey:
            headers["date"] = datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT")
            concat_header = self.canonical_header(headers)
            concat_rs = self.canonical_resource(uri)
            request_date = headers.get("date")
            sign_str = self.sign_str(method, body, request_date, concat_header, concat_rs)

            if self._kind == Aes:
                headers["as-signature-hmac-sha256"] = self.hmac_signature(
                    sign_str, self._api_secret
                )

            if self._kind == Rsa:
                headers["as-signature-rsa-sha256"] = self.rsa_encrypt(sign_str, self._api_secret)

        return headers

    @classmethod
    def sign_str(
        cls, method: str, body: str, date: str, concat_header: str, concat_resource: str
    ) -> str:
        content_md5 = ""
        content_type = ""

        if body is not None and body != "":
            content_type = "application/json"
            content_md5 = cls.md5_encode(body)

        return "\n".join([method, content_md5, content_type, date, concat_header, concat_resource])

    @classmethod
    def canonical_header(cls, headers: Dict) -> str:
        """
        :param headers: dict.

        To generate the canonicalized_headers:

        1. Extract all request headers with the as- prefix key. Kindly note that the headers with the as- prefix
            are not limited to as-api-key, but also include other as- prefixed key such as as-store-id.
        2. Convert all the request header key to lowercase (except the header values case),
            and sort the headers in ASCII code order.
        3. Remove leading spaces and trailing spaces from the header key and value.
        4. Concatenate each of the header key and value with :, to form a header pair
            header_pair = header_key + ":" + header_value
        5. Concatenate all header pairs with the new line character (ASCII code 10).
        """
        if headers is None or len(headers) == 0:
            return ""

        result = {k.lower(): v.lstrip() for k, v in headers.items() if k.lower().startswith("as-")}
        result = dict(sorted(result.items()))

        return "\n".join([f"{k}:{v}" for k, v in result.items()])

    @classmethod
    def canonical_resource(cls, raw_url: str) -> str:
        """
        :param raw_url: str - raw request url.
            Example : https://api.aftership.com/tracking/2024-04/trackings?key2=value2&key1=value1

        :return canonical_url: str - canonical request url.
            Example :/tracking/2024-04/trackings?key1=value1&key2=value2
        """
        u = url.parse_url(raw_url)
        resource = u.path

        if u.query is not None and u.query != "":
            resource += "?" + u.query

        return resource

    @staticmethod
    def md5_encode(source: str) -> str:
        return hashlib.md5(source.encode("utf-8")).hexdigest().upper()

    @staticmethod
    def rsa_encrypt(sign_str: str, api_secret: str) -> str:
        private_key = RSA.importKey(api_secret.encode("utf-8"))
        cipher = PKCS1_PSS.new(private_key)
        h = SHA256.new()
        h.update(sign_str.encode("utf-8"))
        signature = cipher.sign(h)
        return base64.b64encode(signature).decode("utf-8")

    @staticmethod
    def hmac_signature(sign_str: str, api_secret: str) -> str:
        signature = hmac.new(
            bytes(api_secret, "utf-8"), msg=bytes(sign_str, "utf-8"), digestmod=hashlib.sha256
        ).digest()
        return base64.b64encode(signature).decode("utf-8")
