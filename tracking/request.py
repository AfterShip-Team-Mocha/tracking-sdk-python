# coding: utf-8
#
# This code was auto generated by AfterShip SDK Generator.
# Do not edit the class manually.

import random
from functools import partial, wraps
from typing import Union, Optional
from urllib.parse import urljoin

import httpx
from pydantic import validate_call, ValidationError
from retrying import retry

from tracking.auth import Authenticator
from tracking.configuration import Configuration
from tracking.response import parse_response
from tracking.exceptions import ApiException, TimedOutError, BadRequestError, ErrorCodeEnum

_default_user_agent = "aftership-sdk-python/4.0.0 (https://www.aftership.com) httpx/0.19.0"


def validate_params(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            funcx = validate_call(func)
            return funcx(*args, **kwargs)
        except ValidationError as e:
            raise BadRequestError(code=ErrorCodeEnum.INVALID_OPTION, message=e)

    return wrapper


class ApiClient:
    """Generic API client for OpenAPI client library builds.

    :param configuration: .Configuration object for this client
    """

    _client = httpx.Client()

    def __init__(self, configuration: Optional[Configuration] = None) -> None:
        self._config = configuration

        if self._config.proxy is not None:
            self._client = httpx.Client(proxy=self._config.proxy)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self._client is not None:
            self._client.close()

    def _request(self, method, url, params=None, body=None, **kwargs) -> Union[dict, None]:
        url = urljoin(self._config.domain, url)
        user_headers = self._build_headers(body, kwargs.pop("headers", dict()))
        ssl_ctx = kwargs.pop("verify", None)

        timeout = kwargs.pop("timeout", 0)
        if timeout <= 0:
            kwargs["timeout"] = self._config.timeout / 1000.0

        request = self._client.build_request(
            method=method, url=url, params=params, data=body, headers=user_headers, **kwargs
        )
        request.headers = Authenticator(
            api_key=self._config.api_key,
            api_secret=self._config.api_secret,
            auth_type=self._config.authentication_type,
        ).sign(
            method=request.method,
            uri=request.url.raw.raw_path.decode("utf-8"),
            headers=request.headers,
            body=body,
        )
        return self._send_request_with_retry(ssl_ctx, request)

    def _build_headers(self, body, user_headers) -> dict:
        _headers = {
            "aftership-client": _default_user_agent,
            "user-agent": _default_user_agent,
        }
        if self._config.user_agent is not None:
            _headers["user-agent"] = self._config.user_agent

        if body is not None:
            _headers["content-type"] = "application/json"

        if "User-Agent" in user_headers:
            user_headers["user-agent"] = user_headers.pop("User-Agent")

        _headers.update(user_headers)
        return _headers

    @staticmethod
    def _retry_if_error(exception):
        if isinstance(exception, TimedOutError):
            return True

        if isinstance(exception, ApiException):
            if exception.status_code >= 500:
                return True
        return False

    @staticmethod
    def _retry_wait(attempts, delay):
        delay_base = 3000
        _delay = delay_base * pow(2, attempts - 1)
        jitter = delay_base * (random.random() - 0.5)
        return max(1.0, _delay + jitter)

    def _send_request_with_retry(self, ssl_context, request: httpx.Request) -> Union[dict, None]:
        retry_backoff = partial(
            retry,
            wait_func=self._retry_wait,
            stop_max_attempt_number=self._config.max_retry + 1,
            retry_on_exception=self._retry_if_error,
        )

        @retry_backoff()
        def wrap(ssl_ctx, req):
            try:
                if ssl_ctx is None:
                    response = self._client.send(req)
                else:
                    with httpx.Client(proxy=self._config.proxy, verify=ssl_ctx) as client:
                        response = client.send(req)
            except httpx.TimeoutException as e:
                raise TimedOutError(
                    code=ErrorCodeEnum.UNKNOW_ERROR,
                    meta_code=500,
                    status_code=500,
                    message=f"{e.__module__}.{e.__class__.__name__}: {e}",
                    response_body="",
                )
            return parse_response(response)

        return wrap(ssl_context, request)
